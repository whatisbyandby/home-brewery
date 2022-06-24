from typing import Protocol

class Heater(Protocol):

    def heater_on(self):
        ...

    def heater_off(self):
        ...
    
    def get_state(self):
        ...

def create_heater(heater_config: dict) -> Heater:

    if heater_config.get("type") == "PUMP_HEATER":
        return PumpHeater(control_pin=heater_config.get("pin_num"), pump=None)

    if heater_config.get("type") == "STANDARD":
        return StandardHeater(1)
    
    if heater_config.get("type") == "MOCK":
        return MockHeater()

    

    raise Exception("Unable to create heater")
    

class MockHeater:
    def __init__(self):
        self.is_on = False

    def heater_on(self):
        self.is_on = True

    def heater_off(self):
        self.is_on = False

    def get_state(self):
        return self.is_on

class StandardHeater:

    def __init__(self, control_pin):
        self.control_pin = control_pin
        self.state = False

    def heater_on(self):
        self.control_pin.HIGH

    def heater_off():
        raise Exception("Not Implemented")
    
    def get_state():
        raise Exception("Not Implemented")


class PumpHeater:

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
