import pytest
from app.step_controller.step_controller import StepController, Step, StepType, StepValidationError


def test_set_step():

    invalid_timed_step = Step(name="Mash", type=StepType.FIXED, mash_set_temperature=152, hlt_set_temperature=160,
                              boil_set_temperature=None, duration=None)

    invalid_fixed_step = Step(name="Mash", type=StepType.TIMED, mash_set_temperature=152, hlt_set_temperature=160,
                              boil_set_temperature=None, duration=30)

    valid_timed_step = Step(name="Mash", type=StepType.FIXED, mash_set_temperature=152, hlt_set_temperature=160,
                            boil_set_temperature=None, duration=10)

    valid_fixed_step = Step(name="Mash", type=StepType.TIMED, mash_set_temperature=152, hlt_set_temperature=160,
                            boil_set_temperature=None, duration=None)

    step_controller = StepController()

    # Assert the vaidation for invalid steps fail
    with pytest.raises(StepValidationError):
        step_controller.set_steps([invalid_timed_step])

        step_controller.set_steps([invalid_fixed_step])

    # Assert the validation for valid steps pass
    step_controller.set_steps([valid_timed_step])

    step_controller.set_steps([valid_fixed_step])

    # Assert validation runs when steps are passed into the constructor
    with pytest.raises(StepValidationError):
        step_controller.set_steps([invalid_timed_step])

    step_controller = StepController([valid_timed_step])
