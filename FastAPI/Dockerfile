# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files for FastAPI
RUN pip install fastAPI
RUN pip install "uvicorn[standard]"
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

COPY Sender.py .

# Expose the necessary ports
EXPOSE 8000

# Command to run FastAPI
CMD ["python", "Sender.py"]
