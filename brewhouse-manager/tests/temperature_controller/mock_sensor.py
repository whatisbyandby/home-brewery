import random
from app.temperature_controller.sensor import Sensor
from typing import List


class MockSensor(Sensor):

    def __init__(self, readings: List[float] = [], temp_range=(60, 70)):
        self.readings = readings
        self.temp_range = temp_range

    def get_temperature(self):
        if len(self.readings) > 0:
            return self.readings.pop(0)
        return random.randrange(self.temp_range[0], self.temp_range[1])
