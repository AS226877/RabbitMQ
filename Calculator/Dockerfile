# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files for the Receiver
COPY pyproject.toml poetry.lock ./
RUN pip install pika

COPY Calculator /app/Calculator

# Command to run the Receiver
CMD ["python", "/app/Calculator/Receiver.py"]
