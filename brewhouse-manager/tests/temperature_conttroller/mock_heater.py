from app.temperature_controller import Heater

class MockHeater(Heater):
    def __init__(self):
        self.is_on = False
       
    def heater_on(self):
        self.is_on = True
        
    def heater_off(self):
        self.is_on = False
        
    def get_state(self):
        return self.is_on