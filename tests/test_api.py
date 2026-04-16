from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


import time

def get_token():
    email = f"test{int(time.time())}@example.com"

    # signup first
    client.post("/auth/signup", params={
        "email": email,
        "password": "123456"
    })

    # login
    response = client.post("/auth/login", params={
        "email": email,
        "password": "123456"
    })

    return response.json()["access_token"]


def test_calculate_protected():
    token = get_token()

    payload = {
        "dob": "1995-05-10",
        "gender": "Male",
        "premium": 20000,
        "pt": 15,
        "ppt": 10,
        "frequency": "Yearly",
        "sum_assured": 500000
    }

    response = client.post(
        "/policy/calculate",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert "data" in data