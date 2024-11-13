FROM python:3.12-slim

WORKDIR /telebot

COPY requirements.txt /telebot/

RUN pip install --upgrade pip && pip install -r /telebot/requirements.txt

EXPOSE 8081

CMD ["python", "telebot_main.py"]