from app.pins.pin import MockPin, initalize_pins
import pytest


def test_initalize_pins_valid():

    config = {
        "pins": {
            "water_pump_pin": {
                "pin_type": "MOCK",
                "pin_num": 18
            }
        }
    }

    pins = initalize_pins(config=config)
    assert pins is not None
    assert isinstance(pins, dict)
    assert len(pins.items()) == 1
    assert pins.get("water_pump_pin") is not None
    assert isinstance(pins.get("water_pump_pin"), MockPin)


def test_initalize_pins_invalid():

    # Config with invalid Pin type
    config = {
        "pins": {
            "water_pump_pin": {
                "pin_type": "GPI",
                "pin_num": 18
            }
        }
    }

    with pytest.raises(ValueError):
        initalize_pins(config=config)
