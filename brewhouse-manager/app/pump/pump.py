from typing import Protocol
from pydantic.dataclasses import dataclass
from app.pins.pin import Pin, create_pin


class CreatePumpError(Exception):
    """Should be raised when there is a problem creating a pump"""


@dataclass
class PumpStateRequest:
    new_state: bool


class Pump(Protocol):

    def set_pump_state(self, new_state: bool) -> bool:
        """Should set the state of the pump"""

    def pump_on(self):
        """Should turn the pump on"""

    def pump_off(self):
        """Should turn the pump off"""

    def get_state(self) -> bool:
        """Returns the current state of the pump"""


def create_pump(pump_config: dict):

    pump_type = pump_config.get("pump_type")

    if pump_type == "STANDARD":
        name = pump_config.get("name")
        pin_config = pump_config.get("pin")
        pin = create_pin(pin_config)
        return StandardPump(name=name, pin=pin)

    if pump_type == "MOCK":
        return MockPump()

    raise CreatePumpError(f"Unable to create pump with type: {pump_type}")


class MockPump:
    def __init__(self) -> None:
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
