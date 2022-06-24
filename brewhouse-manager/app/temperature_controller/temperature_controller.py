from .temperature_sensor import TemperatureSensor
from .cooler import Cooler
from .heaters import Heater
from enum import Enum


class ControllerMode(Enum):
    HEATER = "HEATER"
    COOLER = "COOLER"


class ControllerState(Enum):
    HEATER_ON = "HEATER_ON"
    COOLER_ON = "COOLER_ON"
    ALL_OFF = "ALL_OFF"
    ERROR = "ERROR"


class TemperatureState(Enum):
    OVER_TEMP = "OVER_TEMP"
    UNDER_TEMP = "UNDER_TEMP"
    IN_RANGE_UNDER = "IN_RANGE_UNDER"
    IN_RANGE_OVER = "IN_RANGE_OVER"


class TemperatureController:

    def __init__(
        self, 
        sensor: TemperatureSensor,  
        mode: ControllerMode = ControllerMode.HEATER, 
        temp_range: float = 1.0, 
        heater: Heater = None, 
        cooler: Cooler = None
    ):
        self._sensor = sensor
        self._set_temperature = None
        self._mode = mode
        self._temp_range = temp_range
        self._current_temp = None
        self._current_state = ControllerState.ALL_OFF
        self.heater = heater
        self.cooler = cooler

        if mode == ControllerMode.HEATER and heater is None:
            raise Exception(
                "Error creating the controller, mode is set to heater, but no heater is provided")
        if mode == ControllerMode.COOLER and cooler is None:
            raise Exception(
                "Error creating the controller, mode is set to cooler, but no cooler is provided")

    def get_current_temperature(self):
        return self._sensor.get_temperature()

    def compare_temperature(self) -> TemperatureState:
        self._current_temp = self.get_current_temperature()
        high_range = self._set_temperature + self._temp_range
        low_range = self._set_temperature - self._temp_range
        if (self._current_temp >= high_range):
            return TemperatureState.OVER_TEMP
        if (self._current_temp <= low_range):
            return TemperatureState.UNDER_TEMP
        if (self._current_temp >= self._set_temperature):
            return TemperatureState.IN_RANGE_OVER
        if (self._current_temp <= self._set_temperature):
            return TemperatureState.IN_RANGE_UNDER

    def tick(self):
        cur_temp_state = self.compare_temperature()
        next_state = self._get_next_state(cur_temp_state)
        self._set_state(next_state)
        return self.get_state()

    def update_set_temp(self, new_set_temp: float):
        self._set_temperature = new_set_temp

    def update_temp_range(self, temp_range: float):
        self._temp_range = temp_range

    def get_state(self):
        return {
            "current_temperature": self._current_temp,
            "set_temperature": self._set_temperature,
            "temperature_range": self._temp_range,
            "state": self._current_state,
            "mode": self._mode
        }

    def _set_state(self, new_state):
        if new_state == self._current_state:
            return
        self._current_state = new_state

    def _get_next_state(self, temp_state: TemperatureState):
        # Heater Paths
        if temp_state == TemperatureState.UNDER_TEMP and self._mode == ControllerMode.HEATER:
            return ControllerState.HEATER_ON
        if temp_state == TemperatureState.IN_RANGE_UNDER and self._mode == ControllerMode.HEATER and self._current_state == ControllerState.HEATER_ON:
            return ControllerState.HEATER_ON
        if temp_state == TemperatureState.IN_RANGE_OVER and self._mode == ControllerMode.HEATER:
            return ControllerState.ALL_OFF
        if temp_state == TemperatureState.OVER_TEMP and self._mode == ControllerMode.HEATER:
            return ControllerState.ALL_OFF
        # Cooler Paths
        if temp_state == TemperatureState.UNDER_TEMP and self._mode == ControllerMode.COOLER:
            return ControllerState.ALL_OFF
        if temp_state == TemperatureState.IN_RANGE_UNDER and self._mode == ControllerMode.COOLER:
            return ControllerState.ALL_OFF
        if temp_state == TemperatureState.IN_RANGE_OVER and self._mode == ControllerMode.COOLER and self._current_state == ControllerState.COOLER_ON:
            return ControllerState.COOLER_ON
        if temp_state == TemperatureState.OVER_TEMP and self._mode == ControllerMode.COOLER:
            return ControllerState.COOLER_ON
        return ControllerState.ERROR
