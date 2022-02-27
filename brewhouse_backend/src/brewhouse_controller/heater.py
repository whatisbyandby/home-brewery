
class Heater:
    def __init__(self, pin):
        self.pin = pin
        self.is_heater_on = False

    def heater_on(self):
        self.is_heater_on = True

    def heater_off(self):
        self.is_heater_on = False

    def get_heater_status(self):
        return self.is_heater_on
