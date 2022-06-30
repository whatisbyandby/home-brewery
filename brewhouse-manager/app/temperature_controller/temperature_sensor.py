import random
from typing import Protocol, List, Callable, Any


class TemperatureSensor(Protocol):

    def get_temperature(self) -> float:
        """Read from the sensor the latest temperature"""


class TemperatureFactoryError(Exception):
    """Should be raised when unable to construct sensor"""


temperature_sensor_creation_funcs: dict[str,
                                        Callable[..., TemperatureSensor]] = {}


def register(sensor_type: str, creation_func: Callable[..., TemperatureSensor]):
    """Register a new sensor type"""
    temperature_sensor_creation_funcs[sensor_type] = creation_func


def unregistered(sensor_type: str):
    """Unregister a sensor type"""
    temperature_sensor_creation_funcs.pop(sensor_type, None)


def create(arguments: dict[str, Any]) -> TemperatureSensor:
    args_copy = arguments.copy()
    sensor_type = args_copy.pop("sensor_type")

    try:
        creation_func = temperature_sensor_creation_funcs[sensor_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown sensor type {sensor_type!r}")


def initalize_temp_sensors(config: dict[str, Any]):
    register("MOCK", MockSensor)

    sensors = {}
    for sensor_name, sensor_config in config["temp_sensors"].items():
        sensors[sensor_name] = create(**sensor_config)
    return sensors


class MockSensor:

    def __init__(self, readings: List[float] = [], temp_range=(60, 70)):
        self.readings = readings
        self.temp_range = temp_range

    def get_temperature(self):
        if len(self.readings) > 0:
            return self.readings.pop(0)
        return random.randrange(self.temp_range[0], self.temp_range[1])
