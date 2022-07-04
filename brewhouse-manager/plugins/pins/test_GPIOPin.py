import RPi.GPIO as GPIO
import time
from .GPIOPin import GPIOPin, start_pins


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
