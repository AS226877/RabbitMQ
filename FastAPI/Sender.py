import os

from fastapi import FastAPI, HTTPException
import pika
import uvicorn

app = FastAPI()

# Establish a connection to the RabbitMQ server
# Get RabbitMQ connection details from environment variables
# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Declare a queue named 'operations'
channel.queue_declare(queue='operations')

# Declare a queue named 'invalid_queue'
channel.queue_declare(queue='invalid_queue')


def send_message(queue, message):
    channel.basic_publish(exchange='', routing_key=queue, body=message)


@app.post("/calculate/{operation}")
async def calculate(operation: str, num1: float, num2: float):
    if operation not in ["sum", "divide", "multiply", "subtract"]:
        invalid_message = f"Invalid operation: {operation}"
        send_message('invalid_queue', invalid_message)
        raise HTTPException(status_code=400, detail="Invalid operation")

    message = f"{operation}:{num1}:{num2}"
    send_message('operations', message)

    return {"message": "Calculation request sent to the receiver."}


# If this file is meant to be run independently, you can start the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
