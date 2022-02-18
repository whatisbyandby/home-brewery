import asyncio
from enum import Enum
from random import Random
from server import broadcast


class TemperatureMode(Enum):
    HEATER = 0
    COOLER = 1


class ControllerState(Enum):
    IDLE = 0
    HEATING = 1
    COOLING = 2


class BrewhouseController:
    def __init__(self):
        self.ambient_temperature = 0
        self.current_temperature = 0
        self.set_temperature = 0
        self.temp_range = 1
        self.mode = TemperatureMode.HEATER
        self.state = ControllerState.IDLE
        self.pump_one_active = False
        self.pump_two_active = False

    def update_set_temperature(self, new_set_temperature):
        self.set_temperature = new_set_temperature

    def update_mode(self, new_mode: TemperatureMode):
        self.mode = new_mode

    def update_pump_state(self, pump_number, new_state):
        if pump_number == 1:
            self.pump_one_active = new_state
        if pump_number == 2:
            self.pump_two_active = new_state

    def compare_temperatures(self):
        temp_low_range = self.set_temperature - self.temp_range
        temp_high_range = self.set_temperature + self.temp_range
        if self.mode == TemperatureMode.HEATER:
            if self.current_temperature < temp_low_range and self.state == ControllerState.IDLE:
                self.handle_state_change(ControllerState.HEATING)
                return
            elif self.current_temperature >= self.set_temperature and self.state == ControllerState.HEATING:
                self.handle_state_change(ControllerState.IDLE)
                return
        if self.mode == TemperatureMode.COOLER:
            if self.current_temperature > temp_high_range and self.state == ControllerState.IDLE:
                self.handle_state_change(ControllerState.COOLING)
                return
            else:
                self.handle_state_change(ControllerState.IDLE)
                return
        else:
            self.handle_state_change(ControllerState.IDLE)

    def handle_state_change(self, new_state: ControllerState):
        if self.state == new_state:
            return
        self.state = new_state

    async def run(self):
        while True:
            self.read_temperature()
            await self.publish_temperature()
            await asyncio.sleep(5)

    def read_temperature(self):
        self.current_temperature = round(Random().random() * 100, 2)

    async def publish_temperature(self):
        await broadcast({
            'amb_temp': self.ambient_temperature,
            'cur_temp': self.current_temperature,
            'set_temp': self.set_temperature,
            'mode': self.mode.name,
            'state': self.state.name
        })
