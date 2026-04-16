from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def get_token():
    email = f"test{int(time.time())}@example.com"

    client.post("/auth/signup", params={
        "email": email,
        "password": "123456"
    })

    res = client.post("/auth/login", params={
        "email": email,
        "password": "123456"
    })

    return res.json()["access_token"]


def test_history():
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

    # create calculation
    client.post(
        "/policy/calculate",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    # fetch history
    response = client.get(
        "/policy/history",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["count"] >= 1
    assert isinstance(data["data"], list)