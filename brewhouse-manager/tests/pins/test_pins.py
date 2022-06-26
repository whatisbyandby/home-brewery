from app.pins.pin import GPIOPin, initalize_pins
import RPi.GPIO as GPIO
import time


def test_gpio_pin():
    initalize_pins()

    pin = GPIOPin(18)

    pin.pin_on()
    assert GPIO.input(18)
    time.sleep(0.1)

    pin.pin_off()
    assert not GPIO.input(18)
    time.sleep(0.1)

    GPIO.cleanup()
