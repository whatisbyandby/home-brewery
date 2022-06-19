import logging


class Pump:

    def __init__(self, name: str):
        self.pump_name = name

    def pump_on(self):
        logging.info(f"Pump {self.pump_name} is on")

    def pump_off(self):
        pass
