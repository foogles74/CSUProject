FROM python:3.12-slim

WORKDIR /telebot

COPY requirements.txt /telebot/

RUN pip install --upgrade pip
RUN pip install -r /telebot/requirements.txt

CMD ["python", "telebot_main.py"]