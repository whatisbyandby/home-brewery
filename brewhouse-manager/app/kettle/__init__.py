from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode
from app.temperature_controller.heaters import create_heater
from app.temperature_controller.temperature_sensor import create_sensor
from dataclasses import dataclass


@dataclass
class KettleConfig:
    name: str
    sensor_config: dict
    heater_config: dict


class Kettle:

    def __init__(self, name: str, temp_controller: TemperatureController):
        self.name = name
        self.temperature_controller = temp_controller

    def get_set_temp(self):
        return self.temperature_controller.get_set_temp()

    def update_set_temp(self):
        pass


def create_kettle(kettle_config: dict, context: dict) -> Kettle:

    name = kettle_config.get("name")
    mode = ControllerMode.HEATER
    temp_range = 1
    temp_controller_config = kettle_config.get("temperature_controller")
    heater = context["heaters"][temp_controller_config.get("heater")]

    temp_controller = TemperatureController(
        sensors=context.get(kettle_config.get("sensor")), mode=mode, temp_range=temp_range, heater=heater)

    kettle = Kettle(name, temp_controller)
    return kettle
