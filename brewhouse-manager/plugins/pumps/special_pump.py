from app.pump.pump import register


"""Pump extension that adds a special pump"""


class SpecialPump:

    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.state = False

    def set_pump_state(self, new_state: bool) -> bool:
        self.state = new_state
        return self.state

    def pump_on(self) -> bool:
        self.state = True
        return self.state

    def pump_off(self) -> bool:
        self.state = False
        return self.state

    def get_state(self) -> bool:
        return self.state


def initalize() -> None:
    register("SPECIAL", SpecialPump)
