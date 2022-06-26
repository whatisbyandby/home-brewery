from typing import Protocol

class CreateHeaterError(Exception):
    """Error raised when something went wrong creating heater"""

class Heater(Protocol):

    def heater_on(self):
        ...

    def heater_off(self):
        ...
    
    def get_state(self):
        ...

def create_heater(heater_config: dict, context: dict) -> Heater:

    if heater_config.get("type") == "PUMP_HEATER":
        return create_pump_heater(heater_config, context)

    if heater_config.get("type") == "STANDARD":
        return create_standard_heater(heater_config)
    
    if heater_config.get("type") == "MOCK":
        return create_mock_heater(heater_config)

    raise Exception("Unable to create heater")

def create_mock_heater(heater_config: dict):
    return MockHeater() 

class MockHeater:
    def __init__(self):
        self.is_on = False

    def heater_on(self):
        self.is_on = True

    def heater_off(self):
        self.is_on = False

    def get_state(self):
        return self.is_on

def create_standard_heater(heater_config: dict):
    return StandardHeater(heater_config.get("pin_num"))

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

def create_pump_heater(heater_config: dict, context: dict):

    pump = context["pumps"][heater_config.get("pump")]

    if pump is None:
        raise CreateHeaterError("Pump is required when creating a pump heater")
    return PumpHeater(control_pin=heater_config.get("pin_num"), pump=pump)

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
