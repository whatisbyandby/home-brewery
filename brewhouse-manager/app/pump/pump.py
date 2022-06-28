from typing import Protocol, Callable, Any
from pydantic.dataclasses import dataclass
from app.pins.pin import Pin


class Pump(Protocol):

    def __init__(self, name: str, pin: Pin):
        """Should Initalize the new Pump"""

    def set_pump_state(self, new_state: bool) -> bool:
        """Should set the state of the pump"""

    def pump_on(self):
        """Should turn the pump on"""

    def pump_off(self):
        """Should turn the pump off"""

    def get_state(self) -> bool:
        """Returns the current state of the pump"""


pump_creation_funcs: dict[str, Callable[..., Pump]] = {}


def register(pump_type: str, creation_func: Callable[..., Pump]):
    """Register a new pump type"""
    pump_creation_funcs[pump_type] = creation_func


def unregister(pump_type: str):
    """Unregister a pump type"""
    pump_creation_funcs.pop(pump_type, None)


def create(arguments: dict[str, Any]) -> Pump:
    """Create a pump of a specific type, given a dictionary of arguments"""
    args_copy = arguments.copy()
    pump_type = args_copy.pop("pump_type")
    try:
        creation_func = pump_creation_funcs[pump_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown Pump Type {pump_type!r}")


class CreatePumpError(Exception):
    """Should be raised when there is a problem creating a pump"""


@dataclass
class PumpStateRequest:
    new_state: bool


def initalize_pumps(config, context: dict[str, Any]):
    register("MOCK", MockPump)
    register("STANDARD", StandardPump)
    pumps = {}
    for pump_name, pump_config in config["pumps"].items():
        pin = context["pins"]
        print(pin)
        pumps[pump_name] = create({**pump_config, "pin": pin})
    return pumps


class MockPump:
    def __init__(self, name: str = "Mock Pump", pin: Pin = None) -> None:
        self.state = False

    def set_pump_state(self, new_state: bool) -> bool:
        self.state = new_state
        return self.state

    def pump_on(self):
        self.state = True

    def pump_off(self):
        self.state = False

    def get_state(self):
        return self.state


class StandardPump:

    def __init__(self, name: str, pin: Pin):
        self.name = name
        self.pin = pin
        self.state: bool = False

    def set_pump_state(self, new_state) -> bool:
        self.state = self.pin.set_pin_state(new_state)

    def pump_on(self):
        self.state = self.pin.pin_on()

    def pump_off(self):
        self.state = self.pin.pin_off()

    def get_state(self) -> bool:
        return self.state
