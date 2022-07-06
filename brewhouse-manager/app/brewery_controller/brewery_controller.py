import logging
from pydantic.dataclasses import dataclass
import asyncio


@dataclass
class KettleUpdate:
    set_temperature: float


class ComponentNotFound(Exception):
    """Raised when the component requested is not found"""


class BreweryController:

    def __init__(self, components: dict):
        self.components = components
        self.logging = logging.getLogger()

    def run_step(self):
        pass

    def update_kettle(self, kettle_id: str, kettle_update: KettleUpdate):
        kettles = self.components.get("kettles")
        kettle_to_update = kettles.get(kettle_id)
        if kettle_to_update is None:
            raise ComponentNotFound(f"No Kettle Found with id: {kettle_id}")
        kettle_to_update.update_set_temp(kettle_update.set_temperature)
        return kettle_to_update

    def get_state(self):
        state = {}
        state["pins"] = {}
        pins = self.components.get("pins")
        for key, pin in pins.items():
            state["pins"][key] = {
                "pin_num": pin.pin_num, "state": pin.get_state()}

        return state

    async def run_main(self):
        while True:
            await asyncio.sleep(1)
