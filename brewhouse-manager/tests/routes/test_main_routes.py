from app.main import app
from fastapi.testclient import TestClient


def test_home_route():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data["home_route"] == "Hello from the home route"
