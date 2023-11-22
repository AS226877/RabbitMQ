import pika


def callback(ch, method, properties, body):
    decoded_message = body.decode('utf-8')
    print(f" [x] Received {decoded_message}")
    # Separate the message by ":"
    parts = decoded_message.split(':')

    print(f"The message failed because {parts[0]} is not a permitted operation")


# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='invalid_queue')

# Set up the callback function to be called when a message is received
channel.basic_consume(queue='invalid_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for invalid messages. To exit press CTRL+C')
channel.start_consuming()
