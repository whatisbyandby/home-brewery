from typing import Protocol
from dataclasses import dataclass

class Pump(Protocol):

    def pump_on(self):
        ...

    def pump_off(self):
        ...

    def get_state(self) -> bool:
        ...