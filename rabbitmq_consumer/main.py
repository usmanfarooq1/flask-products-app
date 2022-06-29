#!/venv/bin/ python
import json
import pika
import time
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

load_dotenv()


engine = create_engine(os.getenv('LOGS_DATABASE_URI')
                       or 'sqlite:///:memory:')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    action = Column(String)
    path = Column(String)
    agent = Column(String)
    payload = Column(String)

    def __repr__(self):
        return f'User {self.name}'


Base.metadata.create_all(engine)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.getenv("RABBIT_MQ_HOST_NAME") or 'localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    raw_body = body.decode()
    log_raw_object = json.loads(raw_body)
    log = Log(action=log_raw_object.get("action"), path=log_raw_object.get("path"),
              agent=log_raw_object.get("agent"), payload=json.dumps(log_raw_object.get("payload")))
    session.add(log)
    print(" [x] Received a message \n")
    # time.sleep()

    session.commit()

    query_get_count = session.query(Log).filter_by(action='GET')
    query_post_count = session.query(Log).filter_by(action='POST')

    print(" [x] Number of requests made with [GET] METHOD",
          query_get_count.count())
    print(
        " [x] Number of requests made with [POST] METHOD", query_post_count.count())
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
