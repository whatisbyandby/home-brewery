from brewhouse_controller import Step
import time


def test_step():
    duration = 0.15
    new_step = Step("Mash", duration, 'minutes')

    # Assert the test is create with the correct values
    assert new_step.name == "Mash"
    assert new_step.duration == 0.15
    assert new_step.units == 'minutes'

    # Start the step, and assert that the start time is set
    new_step.start()
    assert new_step.start_time is not None

    # Assert that the step is not complete
    assert new_step.is_completed() is False

    # Wait for the step to complete
    time.sleep(duration * 60)

    # Assert that the step is complete
    assert new_step.is_completed() is True
