import os

import pika
from datetime import datetime

#  from get_elasticsearch import get_elasticsearch_connection

#  es = get_elasticsearch_connection()


def index_to_elasticsearch(index_name, operation_type, text):
    document = {
        'type': operation_type,
        'text': text,
        'timestamp': datetime.now().isoformat(),
    }

    # Index the document into Elasticsearch
    #  es.index(index=index_name, body=document)


def callback(ch, method, properties, body):
    decoded_message = body.decode('utf-8')
    print(f" [x] Received {decoded_message}")

    # Separate the message by ":"
    parts = decoded_message.split(':')

    if len(parts) == 3:
        operation, num1, num2 = parts

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation.lower() == 'sum':
                result = num1 + num2
                text = f"{num1} + {num2} = {result}"
            elif operation.lower() == 'subtract':
                result = num1 - num2
                text = f"{num1} - {num2} = {result}"
            elif operation.lower() == 'multiply':
                result = num1 * num2
                text = f"{num1} * {num2} = {result}"
            elif operation.lower() == 'divide':
                result = num1/ num2
                text = f"{num1} / {num2} = {result}"
            else:
                print(f"Unknown operation: {operation}")
                text = "Unknown operation"
        except ValueError as e:
            print(f"Error parsing numbers: {e}")
            text = "Error parsing numbers"
    else:
        print("Invalid message format")
        text = "Invalid message format"

    try:
        # Generate an index name (you can modify this logic as needed)
        index_name = f"operations_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Index the document into Elasticsearch
        #  index_to_elasticsearch(index_name, 'Valid_operations', text)
        print(f"Text indexed to Elasticsearch: {text}")
    except Exception as e:
        print(f"Error indexing to Elasticsearch: {e}")


# Establish a connection to the RabbitMQ server
# Get RabbitMQ connection details from environment variables
rabbitmq_host = os.getenv("RABBITMQ_HOST", "172.17.0.1")
rabbitmq_port = int(os.getenv("RABBITMQ_PORT", 5672))

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, rabbitmq_port))
channel = connection.channel()

# Declare the 'operations' queue
channel.queue_declare(queue='operations')

# Set up the callback function to be called when a message is received
channel.basic_consume(queue='operations', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
