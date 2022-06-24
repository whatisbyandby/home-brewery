import json
from app.context import initialize_context


def test_initialize_context():

    config = None
    with open("./tests/config/test.json", "r") as config_file:
        config = json.load(config_file)

    context = initialize_context(config)


    # Assert the pumps were initialized
    pumps = context.get("pumps")
    assert pumps is not None

    pump_one = pumps.get("pump_one") 
    assert pump_one is not None

    pump_one = pumps.get("pump_two") 
    assert pump_one is not None