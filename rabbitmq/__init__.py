import pika
import json
import os
from dotenv import load_dotenv
load_dotenv()


def publish_to_rabbit_mq(data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=os.getenv("RABBIT_MQ_HOST_NAME") or 'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=data,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    connection.close()


def create_rabbit_mq_payload(action: str, path: str, agent: str, payload):
    return json.dumps({"action": action, "path": path, "agent": agent,
                       "payload": payload})
