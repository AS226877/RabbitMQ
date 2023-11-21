from fastapi.testclient import TestClient
from Sender import app


def test_calculate_sum():
    with TestClient(app) as client:
        response = client.post("/calculate/sum?num1=2.5&num2=3.5")
        assert response.status_code == 200
        assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_subtract():
    with TestClient(app) as client:
        response = client.post("/calculate/subtract?num1=5.5&num2=2.5")
        assert response.status_code == 200
        assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_multiply():
    with TestClient(app) as client:
        response = client.post("/calculate/multiply?num1=2.5&num2=3.5")
        assert response.status_code == 200
        assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_divide():
    with TestClient(app) as client:
        response = client.post("/calculate/divide?num1=10&num2=2")
        assert response.status_code == 200
        assert response.json() == {"message": "Calculation request sent to the receiver."}


def test_calculate_invalid_operation():
    with TestClient(app) as client:
        response = client.post("/calculate/invalid?num1=2.5&num2=3.5")
        assert response.status_code == 400
        assert "Invalid operation" in response.text


def test_calculate_send_to_invalid_queue():
    with TestClient(app) as client:
        response = client.post("/calculate/invalid_operation?num1=2.5&num2=3.5")
        assert response.status_code == 400
        assert "Invalid operation" in response.text