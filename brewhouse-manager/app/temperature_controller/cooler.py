from typing import Protocol

class Cooler(Protocol):

    def cooler_on():
        ...

    def cooler_off():
        ...
    
    def get_state():
        ...