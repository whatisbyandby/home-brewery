from typing import Protocol
from dataclasses import dataclass

class Pump(Protocol):

    def pump_on(self):
        ...

    def pump_off(self):
        ...

    def get_state(self) -> bool:
        ...

def create_pump(pump_config: dict):

    name = pump_config.get("name")
    pin_number = pump_config.get("pin_number")

    return StandardPump(name=name, pin_number=pin_number)

from dataclasses import dataclass

@dataclass
class MockPump:

    state: bool = False

    def pump_on(self):
        self.state = True

    def pump_off(self):
        self.state = False

    def get_state(self):
        return self.state

class StandardPump:

    def __init__(self, name: str, pin_number: int):
        self.name = name
        self.pin_number = pin_number
        self.state: bool = False

    def pump_on(self):
        self.state = True

    def pump_off(self):
        self.state = False

    def get_state(self) -> bool:
        return self.state