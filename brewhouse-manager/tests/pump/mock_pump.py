from dataclasses import dataclass

@dataclass
class MockPump:

    state: bool = False

    def pump_on(self):
        self.state = True

    def pump_off(self):
        self.state = False

    def get_state(self):
        return self.state