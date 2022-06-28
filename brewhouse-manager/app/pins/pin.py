import RPi.GPIO as GPIO
from typing import Protocol, Callable, runtime_checkable


@runtime_checkable
class Pin(Protocol):

    def set_pin_state(self, new_state: bool) -> bool:
        """Set the state of the pin"""

    def pin_on(self) -> bool:
        """pin_on will turn a pin on"""

    def pin_off(self) -> bool:
        """pin_off will turn a pin off"""

    def get_state(self):
        """Returns the current state of the pin"""


pin_creation_func: dict[str, Callable[..., Pin]] = {}


def register(pin_type: str, creation_func: Callable[..., Pin]):
    pin_creation_func[pin_type] = creation_func


def unregister(pin_type: str):
    pin_creation_func.pop(pin_type, None)


def create(arguments: dict) -> Pin:

    args_copy = arguments.copy()
    pin_type = args_copy.pop("pin_type")
    try:
        creation_func = pin_creation_func[pin_type]
        print(args_copy)
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown Pin Type {pin_type!r}")


def initalize_pins(config: dict) -> dict[str, Pin]:
    register("MOCK", MockPin)
    register("GPIO", GPIOPin)

    pin_ctx: dict[str, Pin] = {}

    pins = config["pins"]
    for key, pin_config in pins.items():
        pin_ctx[key] = create(pin_config)
    return pin_ctx


def start_pins(warnings_enabled: bool = False):
    GPIO.setwarnings(warnings_enabled)
    GPIO.setmode(GPIO.BCM)


class MockPin():

    def __init__(self, pin_num: int = 1) -> None:
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
