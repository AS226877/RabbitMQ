# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files for the Receiver
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

COPY Receiver.py .

# Command to run the Receiver
CMD ["python", "Receiver.py"]
