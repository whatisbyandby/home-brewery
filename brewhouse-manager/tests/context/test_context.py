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

    kettles = context.get('kettles')

    hlt = kettles.get("hlt")
    assert hlt is not None
    assert hlt.name == "Hot Liquor Tank"

    assert hlt.temperature_controller is not None

    mash_tun = kettles.get("mash_tun")
    assert mash_tun is not None
    assert mash_tun.name == "Mash Tun"

    boil = kettles.get("boil")
    assert boil is not None
    assert boil.name == "Boil Kettle"