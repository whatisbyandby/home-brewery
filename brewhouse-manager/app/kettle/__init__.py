from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode


class Kettle:

    def __init__(self, name: str, temp_controller: TemperatureController):
        self.name = name
        self.temperature_controller = temp_controller

    def get_set_temp(self):
        return self.temperature_controller.get_set_temp()

    def get_current_temp(self):
        return self.temperature_controller.get_current_temperature()

    def update_set_temp(self, new_set_temp: float):
        self.temperature_controller.update_set_temp(new_set_temp=new_set_temp)


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
