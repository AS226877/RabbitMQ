# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the poetry files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-dev

# Copy the entire project directory
COPY . .

# Expose the ports
EXPOSE 8000
EXPOSE 5672  # RabbitMQ

# Start the FastAPI application and RabbitMQ receiver
CMD ["poetry", "run", "uvicorn", "FastAPI.Sender:app", "--host", "0.0.0.0", "--port", "8000"] && \
    python Calculator/Receiver.py
