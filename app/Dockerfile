FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip install websockets
ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["python", "main.py"]