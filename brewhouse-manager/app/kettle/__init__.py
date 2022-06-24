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
        self.temp_controller = temp_controller


    def get_set_temp(self):
        return 

    def update_set_temp(self):
        pass

def create_kettle(kettle_config: KettleConfig) -> Kettle:

    name = kettle_config.name
    sensor = create_sensor(kettle_config.sensor_config)
    heater = create_heater(kettle_config.heater_config)
    mode = ControllerMode.HEATER
    temp_range = 1


    temp_controller = TemperatureController(sensor=sensor, mode=mode, temp_range=temp_range, heater=heater)

    kettle = Kettle(name, temp_controller)