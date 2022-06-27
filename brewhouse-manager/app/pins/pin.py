import RPi.GPIO as GPIO
from typing import Protocol


class Pin(Protocol):

    def set_pin_state(self, new_state: bool) -> bool:
        """Set the state of the pin"""

    def pin_on(self) -> bool:
        """pin_on will turn a pin on"""

    def pin_off(self) -> bool:
        """pin_off will turn a pin off"""

    def get_state(self):
        """Returns the current state of the pin"""


def initalize_pins(warnings_enabled: bool = False):
    GPIO.setwarnings(warnings_enabled)
    GPIO.setmode(GPIO.BCM)


def create_pin(pin_config: dict):

    if pin_config.get("pin_type") == "GPIO":
        pin_num = pin_config.get("pin_num")
        return GPIOPin(pin_num=pin_num)

    if pin_config.get("pin_type") == "MOCK":
        pin_num = pin_config.get("pin_num")
        return MockPin(pin_num=pin_num)


class MockPin():

    def __init__(self, pin_num) -> None:
        self.pin_num = pin_num
        self.pin_state = False

    def set_pin_state(self, new_state: bool) -> bool:
        self.pin_state = new_state
        return self.pin_state

    def pin_on(self) -> bool:
        self.pin_state = True
        return self.pin_state

    def pin_off(self) -> bool:
        self.pin_state = False
        return self.pin_state

    def get_state(self) -> bool:
        return self.pin_state


class GPIOPin():

    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT)

    def set_pin_state(self, new_state: bool) -> bool:
        GPIO.output(self.pin_num, new_state)
        return GPIO.input(self.pin_num)

    def pin_on(self) -> bool:
        print(GPIO.output(self.pin_num, GPIO.HIGH))
        return GPIO.input(self.pin_num)

    def pin_off(self) -> bool:
        GPIO.output(self.pin_num, GPIO.LOW)
        return GPIO.input(self.pin_num)

    def get_state(self) -> bool:
        return GPIO.input(self.pin_num)
