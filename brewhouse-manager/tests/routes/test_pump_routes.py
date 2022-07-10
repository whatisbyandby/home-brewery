import json
from app.main import app
from app.brewery_controller.brewery_controller import BreweryController
from fastapi.testclient import TestClient
from app.pump.pump import MockPump


def test_get_pumps():
    client = TestClient(app)

    components = {}
    components["pumps"] = {}
    components["pumps"]["water_pump"] = MockPump()
    components["pumps"]["wort_pump"] = MockPump()

    app.brewery_controller = BreweryController(components=components)

    response = client.get("/brewhouse/pumps")

    assert response.status_code == 200
    res_list = response.json()
    assert len(res_list) == 2
