FROM python:3.12-slim

WORKDIR /telelog

COPY requirements.txt /telelog/

RUN pip install --upgrade pip
RUN pip install -r /telelog/requirements.txt

CMD ["python", "telebot_main.py"]