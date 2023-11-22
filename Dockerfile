FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-dev

COPY . .

EXPOSE 8000
EXPOSE 5672

CMD ["sh", "-c", "poetry run uvicorn FastAPI.Sender:app --host 0.0.0.0 --port 8000 && python Calculator/Receiver.py"]
