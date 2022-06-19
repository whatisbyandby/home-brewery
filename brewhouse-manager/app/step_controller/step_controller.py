from pydantic.dataclasses import dataclass
from typing import Optional, List
from datetime import timedelta, datetime
from enum import Enum


class StepType(str, Enum):
    TIMED = "TIMED"
    FIXED = "FIXED"


@dataclass
class Step:
    name: str
    type: StepType
    mash_set_temperature: Optional[float]
    hlt_set_temperature: Optional[float]
    boil_set_temperature: Optional[float]
    duration: Optional[float]


class StepValidationError(Exception):
    pass


class StepController:
    def __init__(self, steps: List[Step] = []):
        self._step_index: int = 0
        self._steps: List[Step] = self.set_steps(steps)
        self._current_step: Step = None
        self._step_start_time: datetime = None
        self._step_end_time: datetime = None
        self._step_delta: timedelta = None

    def _validate_step(self, step):
        if step.type == StepType.FIXED and step.duration is None:
            raise StepValidationError(
                "Steps with a type of FIXED must have a duration")
        if step.type == StepType.TIMED and step.duration is not None:
            raise StepValidationError(
                "Steps with a type of TIMED must not have a duration")

    def set_steps(self, steps: List[Step]):
        for step in steps:
            self._validate_step(step)
        self._steps = steps
        return self._steps

    def move_next_step(self):
        self._step_index += 1
        self._current_step = self._steps[self._step_index]

    def set_current_step(self, index: int):
        self._step_index = index
        self._current_step = self._steps[self._step_index]

    def get_current_step(self):
        return self._current_step

    def get_steps(self):
        return self._steps

    def peek_next_step(self):
        return self._steps[self._step_index + 1]

    def start_current_step(self):
        self._step_start_time = datetime.now()
        self._step_end_time = self._step_start_time + self._current_step.duration
