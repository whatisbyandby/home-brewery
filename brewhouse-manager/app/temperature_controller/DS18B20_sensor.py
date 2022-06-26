from w1thermsensor import W1ThermSensor

def create_DS18B20():
    return DS18B20Sensor()

class DS18B20Sensor:

    def __init__(self):
        self.sensor = W1ThermSensor()


    def get_temperature(self) -> float:
        return self.sensor.get_temperature()