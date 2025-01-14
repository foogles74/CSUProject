import pika
from db.settings import get_settings


def send_log(log_message):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=get_settings().RABBIT_HOST,
            port=5672,
            virtual_host='/',
            credentials=pika.PlainCredentials(
                username=get_settings().DB_USER,
                password=get_settings().DB_PASS
            ),
            heartbeat=30,
            blocked_connection_timeout=2
        ))
        channel = connection.channel()
        channel.queue_declare(queue='logger', durable=True)

        channel.basic_publish(
            exchange='',
            routing_key='logger',
            body=log_message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
    except Exception as e:
        print(e)

