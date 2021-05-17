from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'otus',
     bootstrap_servers=['192.168.50.12:9092', '192.168.50.13:9092', '192.168.50.14:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    print(f'Got the message {message}')
