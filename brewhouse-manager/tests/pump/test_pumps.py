import pytest
from app.pump.pump import create,  StandardPump, initalize_pumps, register
from app.pins.pin import MockPin, Pin


def test_create():
    context = {

    }

    register("STANDARD", StandardPump)

    args = {
        "pump_type": "STANDARD",
        "name": "Standard Pump",
        "pin": MockPin(pin_num=1)
    }

    pump = create(args)
    assert pump is not None
    assert isinstance(pump, StandardPump)
    assert isinstance(pump.pin, Pin)


def test_initalize_pumps():

    config = {
        "pumps": {
            "water_pump": {
                "pump_type": "MOCK",
                "pin": "water_pump_pin"
            }
        }
    }

    test_pin = MockPin()
    context = {
        "pins": {
            "water_pump_pin": test_pin
        }
    }

    pumps = initalize_pumps(config=config, context=context)
    assert pumps is not None
    assert len(pumps) == 1
    water_pump = pumps.get("water_pump")
    assert water_pump is not None
    assert water_pump.pin is not None
    assert water_pump.pin == test_pin
    assert isinstance(water_pump.pin, Pin)


def test_standard_pump():
    mock_pin = MockPin(pin_num=18)

    standard_pump = StandardPump(name="Test Standard", pin=mock_pin)

    assert standard_pump is not None

    standard_pump.pump_on()
    assert mock_pin.get_state() is True

    standard_pump.pump_off()
    assert mock_pin.get_state() is False

    assert standard_pump.get_state() is False
