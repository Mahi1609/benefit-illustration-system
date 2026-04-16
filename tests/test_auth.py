from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_signup():
    response = client.post("/auth/signup", params={
        "email": "test@example.com",
        "password": "123456"
    })

    assert response.status_code in [200, 400]  # allow duplicate case


def test_login():
    response = client.post("/auth/login", params={
        "email": "test@example.com",
        "password": "123456"
    })

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data