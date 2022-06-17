
from .heater import Heater

class PumpHeater(Heater):
    def __init__(self, control_pin, pump):
        self.control_pin = control_pin
        self.is_on = False
        self.pump = pump

    def heater_on(self):
        self.pump.pump_on()
        self.is_on = True
        self.control_pin.HIGH

    def heater_off(self):
        self.is_on = False
        self.control_pin.LOW

    def get_state(self):
        return self.is_on