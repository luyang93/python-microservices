import json

import pika

from .models import Product

params = pika.URLParameters('amqp://guest:guest@192.168.3.28:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    product = Product.object.get(id=id)
    product.likes += 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
