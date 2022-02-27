
class Pump:
    def __init__(self, pin):
        self.pin = pin
        self.is_pump_on = False

    def pump_on(self):
        self.is_pump_on = True

    def pump_off(self):
        self.is_pump_on = False

    def get_pump_status(self):
        return self.is_pump_on
