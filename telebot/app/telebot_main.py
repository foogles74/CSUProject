import telebot
from tools.settings import get_settings
from telebot import types
import requests

bot = telebot.TeleBot(get_settings().BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
  main_menu(message, True)


@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.message:
        if function_call.data == "balance":
            r = requests.get(f"http://127.0.0.1:8080/get_balance_route/{function_call.from_user.id}")
            second_mess = f"Ваш Баланс : {r.text}"
            bot.send_message(function_call.message.chat.id, second_mess)
            bot.answer_callback_query(function_call.id)
        elif function_call.data == "add_balance":
            second_mess = "Введите сумму доната!"
            bot.send_message(function_call.message.chat.id, second_mess)
            bot.answer_callback_query(function_call.id)
            bot.register_next_step_handler_by_chat_id(function_call.from_user.id, change_balance)
        elif function_call.data == "add_request":
            second_mess = "Напишите сообщение которое хотите отправить!"
            bot.send_message(function_call.message.chat.id, second_mess)
            bot.answer_callback_query(function_call.id)
            bot.register_next_step_handler_by_chat_id(function_call.from_user.id, do_request)

def change_balance(message):
    text = message.text
    print(text)
    try:
        if type(int(text)) == int:
            req = requests.post(f"http://127.0.0.1:8080/change_balance", json={"login": message.from_user.id,"value": text})
            if req.status_code == 200:
                r = requests.get(f"http://127.0.0.1:8080/get_balance_route/{message.from_user.id}")
                second_mess = f"Ваш Баланс : {r.text}"
                bot.send_message(message.chat.id, second_mess)
            else:
                main_error(message)
        else:
            error = f"Напиши циферку"
            bot.send_message(message.chat.id, error)
            bot.register_next_step_handler_by_chat_id(message.from_user.id, change_balance)
    except:
        error = f"Напиши циферку"
        bot.send_message(message.chat.id, error)
        bot.register_next_step_handler_by_chat_id(message.from_user.id, change_balance)

def do_request(message):
    text = message.text
    if text != "/exit":
        req = requests.get(f"http://127.0.0.1:8080/request_model",
                            params={"text": text,"user": message.from_user.id,"chat_name": "main"})
        if req.status_code == 200:
            bot.send_message(message.chat.id, str(req.text[1:-1]).replace("\\n","\n"), parse_mode = 'HTML')
            bot.register_next_step_handler_by_chat_id(message.from_user.id, do_request)
        else:
            main_error(message)
    else:
        main_menu(message)

def main_menu(message, reg : bool = False):
    first_mess = f"<b>{message.from_user.first_name} </b>, привет!\nЧто ты хочешь?"
    if reg:
        requests.post("http://127.0.0.1:8080/signup",
                      json={"login": message.from_user.id, "email": message.from_user.id, "password": "value"})
    markup = types.InlineKeyboardMarkup()
    button_balance = types.InlineKeyboardButton(text='Посмотреть в мисочку', callback_data='balance')
    markup.add(button_balance)
    button_add_balance = types.InlineKeyboardButton(text='Пополнить Кормушку', callback_data='add_balance')
    markup.add(button_add_balance)
    button_add_request = types.InlineKeyboardButton(text='Написать котику', callback_data='add_request')
    markup.add(button_add_request)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

def main_error(message):
    second_mess = "Что то пошло не так"
    bot.send_message(message.chat.id, second_mess)


bot.infinity_polling()