from fastapi.testclient import TestClient
from pydantic import ValidationError
from app.main import app
from app.brewery_controller.brewery_controller import KettleUpdate
from dataclasses import asdict
from app.pump.pump import PumpStateRequest


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


"""Test the Brewhouse Routes"""


def test_get_brewhouse_state():
    response = client.get("/brewhouse/state")
    assert response.status_code == 200


def test_get_brewhouse_kettles():
    response = client.get("/brewhouse/kettles")
    assert response.status_code == 200


def test_get_brewhouse_kettles_details():
    response = client.get("/brewhouse/kettles/hlt")
    assert response.status_code == 200


def test_get_brewhouse_kettles_details():

    kettle_update = KettleUpdate(set_temperature=90.0)

    response = client.put("/brewhouse/kettles/hlt", json=asdict(kettle_update))
    assert response.status_code == 200


def test_get_pumps():
    response = client.get("/brewhouse/pumps")
    assert response.status_code == 200
    assert response.json() is not None


def test_update_pumps():

    pump_state = PumpStateRequest(new_state=True)

    response = client.put("/brewhouse/pumps/water", json=asdict(pump_state))
    assert response.status_code == 200
    assert response.json() is not None
