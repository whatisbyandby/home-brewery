
class Heater:

    def heater_on():
        pass

    def heater_off():
        pass
    
    def get_state():
        pass


class StandardHeater(Heater):

    def __init__(self, control_pin):
        self.control_pin = control_pin

    def heater_on(self):
        self.control_pin.HIGH

    def heater_off():
        pass
    
    def get_state():
        pass

        
