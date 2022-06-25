import random
from typing import Protocol, List
from .DS18B20_sensor import DS18B20Sensor

class TemperatureSensor(Protocol):

    def get_temperature(self) -> float:
        ...

class TemperatureFactoryError(Exception):
    """Should be raised when unable to construct sensor"""


class MockSensor:

    def __init__(self, readings: List[float] = [], temp_range=(60, 70)):
        self.readings = readings
        self.temp_range = temp_range

    def get_temperature(self):
        if len(self.readings) > 0:
            return self.readings.pop(0)
        return random.randrange(self.temp_range[0], self.temp_range[1])




def create_sensor(sensor_config: dict):

    if sensor_config.get("type") == "MOCK":
        return MockSensor()

    if sensor_config.get("type") == "DS18B20":
        return DS18B20Sensor()
    
    
