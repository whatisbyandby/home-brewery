from w1thermsensor import W1ThermSensor


class DS18B20Sensor:

    def __init__(self):
        self.sensor = W1ThermSensor()

    def get_temperature(self) -> float:
        return self.sensor.get_temperature()


def initalize():
    pass
