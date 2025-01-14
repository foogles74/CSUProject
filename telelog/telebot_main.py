import time

import telebot
from tools.settings import get_settings
from telebot import types
import requests
import pika

# bot = telebot.TeleBot("7265649424:AAG28DGnIcvdRJgRxpx7QEfv_oZS0ARyAJA")
# @bot.message_handler(commands=['start'])
# def start_bot(message):
#     TOKEN = get_settings().BOT_TOKEN
#     url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#     print(message)

# bot.infinity_polling()
chat_id = "459701131"
time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=get_settings().SERVER_IP,  # Замените на адрес вашего RabbitMQ сервера
    port=5672,          # Порт по умолчанию для RabbitMQ
    virtual_host='/',   # Виртуальный хост (обычно '/')
    credentials=pika.PlainCredentials(
        username=get_settings().SERVER_USER,  # Имя пользователя по умолчанию
        password=get_settings().SERVER_PASS   # Пароль по умолчанию
    ),
    heartbeat=30,
    blocked_connection_timeout=2
))
channel = connection.channel()

def process_log(ch, method, properties, body):
    log_message = body.decode('utf-8')
    url = f"https://api.telegram.org/bot{get_settings().BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={log_message}"
    print(requests.get(url).json())
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='logger', on_message_callback=process_log)
channel.start_consuming()