# tests/test_sender.py

from fastapi.testclient import TestClient
from Sender import app

client = TestClient(app)


def test_calculate_sum():
    response = client.post("/calculate/sum", json={"num1": 2, "num2": 3})
    assert response.status_code == 200
    assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_subtract():
    response = client.post("/calculate/subtract", json={"num1": 5, "num2": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_multiply():
    response = client.post("/calculate/multiply", json={"num1": 4, "num2": 3})
    assert response.status_code == 200
    assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_divide():
    response = client.post("/calculate/divide", json={"num1": 10, "num2": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_invalid_operation():
    response = client.post("/calculate/invalid_operation", json={"num1": 1, "num2": 2})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid operation"}
