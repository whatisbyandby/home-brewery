from app.pins.pin import register
import RPi.GPIO as GPIO


def start_pins(warnings_enabled: bool = False):
    GPIO.setwarnings(warnings_enabled)
    GPIO.setmode(GPIO.BCM)


class GPIOPin():

    def __init__(self, pin_num):
        self.pin_num = pin_num
        print(pin_num)
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


def initalize():
    mode = GPIO.getmode()
    if mode is None:
        start_pins()
    register("GPIO", GPIOPin)
