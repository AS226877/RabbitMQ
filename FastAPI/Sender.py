import os

from fastapi import FastAPI, HTTPException
import pika

app = FastAPI()

# Establish a connection to the RabbitMQ server
# Get RabbitMQ connection details from environment variables
rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
rabbitmq_port = int(os.getenv("RABBITMQ_PORT", 5672))

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, socket_timeout=30, heartbeat=30))
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
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)