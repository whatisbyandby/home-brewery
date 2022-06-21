import pytest
from app.step_controller.step_controller import StepController, Step, StepType, StepControllerError

invalid_timed_step = Step(name="Mash", type=StepType.TIMED, mash_set_temperature=152, hlt_set_temperature=160,
                          boil_set_temperature=None, duration=10)

invalid_fixed_step = Step(name="Mash", type=StepType.FIXED, mash_set_temperature=152, hlt_set_temperature=160,
                          boil_set_temperature=None, duration=None)

valid_timed_step = Step(name="Mash", type=StepType.TIMED, mash_set_temperature=152, hlt_set_temperature=160,
                        boil_set_temperature=None, duration=None)

valid_fixed_step = Step(name="Mash", type=StepType.FIXED, mash_set_temperature=152, hlt_set_temperature=160,
                        boil_set_temperature=None, duration=10)


def test_set_step():

    step_controller = StepController()

    # Assert the vaidation for invalid steps fail
    with pytest.raises(StepControllerError):
        step_controller.set_steps([invalid_timed_step])

        step_controller.set_steps([invalid_fixed_step])

    # Assert the validation for valid steps pass
    step_controller.set_steps([valid_timed_step])

    step_controller.set_steps([valid_fixed_step])

    # Assert validation runs when steps are passed into the constructor
    with pytest.raises(StepControllerError):
        step_controller.set_steps([invalid_timed_step])

    step_controller = StepController([valid_timed_step])


def test_move_next_step():

    step_controller = StepController([valid_timed_step, valid_fixed_step])

    step_controller.next_step()
    assert step_controller.get_current_step().get("step") == valid_timed_step

    step_controller.next_step()
    assert step_controller.get_current_step().get("step") == valid_fixed_step


def test_peek_next_step():

    step_controller = StepController([valid_timed_step, valid_fixed_step])

    assert step_controller.peek_next_step() == valid_timed_step

    step_controller.next_step()

    assert step_controller.peek_next_step() == valid_fixed_step


def test_start():

    step_controller = StepController([valid_timed_step, valid_fixed_step])

    step_controller.next_step()
    step_controller.start()

    assert step_controller.get_current_step().get("is_running") == True
    assert step_controller.get_current_step().get("step_start_time") is not None
    assert step_controller.get_current_step().get("step").type == StepType.TIMED
    assert step_controller.get_current_step().get("step_end_time") is None

    step_controller.stop()
    assert step_controller.get_current_step().get("is_running") == False
