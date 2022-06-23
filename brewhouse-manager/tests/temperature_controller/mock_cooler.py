from app.temperature_controller.cooler import Cooler 

class MockCooler(Cooler):

    def __init(self):
        self.is_on = False

    def cooler_on(self):
        self.is_on = True

    def cooler_off(self):
        self.is_on = False
    
    def get_state(self):
        return self.is_on