FROM python:3.12-slim
RUN pip install virtualenv
RUN virtualenv /telebot/venv
ADD app /telebot
WORKDIR /telebot


RUN . /telebot/venv/bin/activate && pip install --upgrade pip && pip install -r /telebot/requirements.txt

ENV PATH="/telebot/venv/bin:$PATH"

ENTRYPOINT ["python"]
CMD ["telebot_main.py"]
EXPOSE 8080