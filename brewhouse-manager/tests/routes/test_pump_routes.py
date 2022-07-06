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
    res_dict = response.json()
    water_pump = res_dict.get("water_pump")
    assert water_pump is not None
    assert water_pump["name"] == "Mock Pump"
    res_dict["wort_pump"]["name"] == "Mock Pump"
