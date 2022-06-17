from .temperature_controller import TemperatureController, Timer
from .pump import Pump
from dataclasses import dataclass

class MashStep:

    def __init__(self, name, temp, duration):
        self.name = name
        self.temp = temp
        self.duration = duration
        self.timer = Timer(duration, name, callback=self.step_finished)

    def start(self):
        self.timer.start()


    def step_finished(self):
        print("Step finished")


class MashController:

    def __init__(self, profile, temp_controller: TemperatureController, circulation_pump: Pump, transfer_pump: Pump):
        self.profile = profile
        self.temp_controller = temp_controller
        self.circulation_pump = circulation_pump
        self.transfer_pump = transfer_pump
        self.current_step = None

    
    def start_mash(self):
        self.current_step = self.profile[0]
        self.start_step(self.current_step)

    def start_step(self, step: MashStep):
        step.start()
        

        
