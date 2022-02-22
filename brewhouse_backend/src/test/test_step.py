from brewhouse_controller import Step
import time


def test_step():
    duration = 0.15
    new_step = Step("Mash", duration, 'minutes')

    assert new_step.name == "Mash"
    assert new_step.duration == 0.15
    assert new_step.units == 'minutes'

    new_step.start()
    assert new_step.start_time is not None

    assert new_step.is_completed() is False

    time.sleep(duration * 60)

    assert new_step.is_completed() is True
