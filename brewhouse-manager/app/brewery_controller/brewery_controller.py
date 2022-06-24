from dataclasses import dataclass
from app.pump.pump import Pump
from app.step_controller.step_controller import Step

class BreweryController:

    def __init__(self, pump_one: Pump, pump_two: Pump):
        self.pump_one: Pump = pump_one
        self.pump_two: Pump = pump_two
        self.cur_step: Step = None

    
    

    
    def run_step(self):
        pass