import json
from app.context import initialize_context
from app.pump.pump import Pump


def test_initialize_context():

    config = None
    with open("./tests/config/test.json", "r") as config_file:
        config = json.load(config_file)

    context = initialize_context(config)

    # Assert the pumps were initialized
    pumps = context.get("pumps")

    assert pumps is not None
    assert len(pumps.keys()) == 2

    water_pump = pumps.get("water_pump")
    assert water_pump is not None

    wort_pump = pumps.get("wort_pump")
    assert wort_pump is not None

    temp_sensors = context.get("temp_sensors")

    assert temp_sensors is not None
    assert len(temp_sensors.keys()) == 4

    heaters = context.get("heaters")
    assert heaters is not None
    assert len(heaters.keys()) == 3

    kettles = context.get("kettles")
    hlt = kettles.get("hlt")
    assert hlt is not None
    assert hlt.name == "Hot Liquor Tank"

    assert hlt.temperature_controller is not None

    mash_tun = kettles.get("mash_tun")
    assert mash_tun is not None
    assert mash_tun.name == "Mash Tun"

    assert mash_tun.temperature_controller is not None

    boil = kettles.get("boil")
    assert boil is not None
    assert boil.name == "Boil Kettle"

    assert boil.temperature_controller is not None
