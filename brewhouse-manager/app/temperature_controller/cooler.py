from typing import Protocol


class Cooler(Protocol):

    def cooler_on():
        ...

    def cooler_off():
        ...

    def get_state():
        ...


class MockCooler:

    def __init__(self):
        self.is_on = False

    def cooler_on(self):
        self.is_on = True

    def cooler_off(self):
        self.is_on = False

    def get_state(self):
        return self.is_on
