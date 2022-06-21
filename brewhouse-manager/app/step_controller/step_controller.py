from pydantic.dataclasses import dataclass
from typing import Optional, List
from datetime import date, timedelta, datetime
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


class StepControllerError(Exception):
    pass


class StepController:
    def __init__(self, steps: List[Step] = []):
        self._step_index: int = None
        self._steps: List[Step] = self.set_steps(steps)
        self._current_step: Step = None
        self._is_running: bool = False
        self._step_start_time: datetime = None
        self._step_end_time: datetime = None
        self._step_delta: timedelta = None

    def _validate_step(self, step):
        if step.type == StepType.FIXED and step.duration is None:
            raise StepControllerError(
                "Steps with a type of FIXED must have a duration")
        if step.type == StepType.TIMED and step.duration is not None:
            raise StepControllerError(
                "Steps with a type of TIMED must not have a duration")

    def set_steps(self, steps: List[Step]):
        for step in steps:
            self._validate_step(step)
        self._steps = steps
        return self._steps

    def next_step(self):
        if self._step_index is None:
            self._set_current_step(0)
            return self._current_step
        self._set_current_step(self._step_index + 1)
        return self._current_step

    def _set_current_step(self, index: int = 0):
        self._step_index = index
        self._current_step = self._steps[self._step_index]

    def get_current_step(self):
        return {
            "step": self._current_step,
            "is_running": self._is_running,
            "step_start_time": self._step_start_time,
            "step_end_time": self._step_end_time
        }

    def get_steps(self):
        return self._steps

    def peek_next_step(self):
        if self._step_index is None:
            return self._steps[0]
        return self._steps[self._step_index + 1]

    def stop(self):
        self._is_running = False

    def start_timed_step(self):
        self._is_running = True
        self._step_start_time = datetime.now()

    def start_fixed_step(self):
        self._is_running = True
        self._step_start_time = datetime.now()
        self._step_end_time = datetime.now() + timedelta(minutes=self._current_step.duration)

    def start(self):
        if self._current_step is None:
            raise StepControllerError("No step to start")
        if self._current_step.type == StepType.TIMED:
            self.start_timed_step()
        elif self._current_step.type == StepType.FIXED:
            self.start_fixed_step()
        return {"message": "Started step"}
