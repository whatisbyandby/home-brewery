from typing import Protocol
from tests.temperature_controller.mock_sensor import MockSensor

class TemperatureSensor(Protocol):

    def get_temperature(self) -> float:
        ...

class TemperatureFactoryError(Exception):
    """Should be raised when unable to construct sensor"""



def create_sensor(sensor_type):

    if sensor_type == "MOCK":
        return MockSensor()

    if sensor_type == "DS18B20":
        return DS18B20Sensor()
    
    
