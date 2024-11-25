import telebot
from tools.settings import get_settings
from telebot import types
import requests

bot = telebot.TeleBot(get_settings().BOT_TOKEN)


@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\n Что ты хочешь?"
  r = requests.post("http://127.0.0.1:8080/signup", json={"login": message.from_user.username,"email": message.from_user.id,"password": "value"})
  markup = types.InlineKeyboardMarkup()
  button_balance = types.InlineKeyboardButton(text = 'Узнать Баланс', callback_data='balance')
  markup.add(button_balance)
  button_add_balance= types.InlineKeyboardButton(text = 'Пополнить Баланс', callback_data='add_balance')
  markup.add(button_add_balance)
  button_add_request= types.InlineKeyboardButton(text = 'Сделать запрос', callback_data='add_request')
  markup.add(button_add_request)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


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
            req = requests.post(f"http://127.0.0.1:8080/change_balance", json={"login": message.from_user.username,"value": text})
            if req.status_code == 200:
                r = requests.get(f"http://127.0.0.1:8080/get_balance_route/{message.from_user.id}")
                second_mess = f"Ваш Баланс : {r.text}"
                bot.send_message(message.chat.id, second_mess)
            else:
                second_mess = "Что то пошло не так"
                bot.send_message(message.chat.id, second_mess)
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
    req = requests.get(f"http://127.0.0.1:8080/request_model",
                        params={"text": text,"user": message.from_user.username,"chat_name": "main"})
    if req.status_code == 200:
        bot.send_message(message.chat.id, req.text)
    else:
        second_mess = "Что то пошло не так"
        bot.send_message(message.chat.id, second_mess)


bot.infinity_polling()