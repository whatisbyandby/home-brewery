from app.main import app
from fastapi.testclient import TestClient
from app.brewery_controller.brewery_controller import BreweryController


def test_get_kettle(context: dict):

    client = TestClient(app)

    app.brewery_controller = BreweryController(components=context)
    response = client.get("/brewhouse/kettles")

    assert response.status_code == 200
