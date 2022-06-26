import RPi.GPIO as GPIO
from typing import Protocol


class Pin(Protocol):

    def pin_on(self):
        """pin_on will turn a pin on"""

    def pin_off(self):
        """pin_off will turn a pin off"""


def initalize_pins(warnings_enabled: bool = False):
    GPIO.setwarnings(warnings_enabled)
    GPIO.setmode(GPIO.BCM)


class GPIOPin():

    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT)

    def pin_on(self):
        GPIO.output(self.pin_num, GPIO.HIGH)

    def pin_off(self):
        GPIO.output(self.pin_num, GPIO.LOW)
