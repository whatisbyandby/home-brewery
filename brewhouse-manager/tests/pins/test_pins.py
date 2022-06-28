from app.pins.pin import MockPin, GPIOPin, initalize_pins, start_pins
import RPi.GPIO as GPIO
import time
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
    print(pins.get("water_pump_pin"))
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


def test_gpio_pin():
    start_pins()

    pin = GPIOPin(18)

    pin.pin_on()
    assert GPIO.input(18)
    assert bool(pin.get_state()) is True
    time.sleep(0.1)

    pin.pin_off()
    assert not GPIO.input(18)
    assert bool(pin.get_state()) is False
    time.sleep(0.1)

    pin.set_pin_state(GPIO.HIGH)
    time.sleep(0.1)
    pin.set_pin_state(GPIO.LOW)
    time.sleep(0.1)

    GPIO.cleanup()
