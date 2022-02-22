
class MockTemperatureSensor:

    def __init__(self, temperature_array):
        self.temperature_array = temperature_array

    def get_current_temp(self):
        if len(self.temperature_array) > 1:
            return self.temperature_array.pop(0)
        return self.temperature_array[0]
