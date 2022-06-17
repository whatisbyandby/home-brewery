from .timer import Timer
import time

num_calls = 0

def test_timer():
    global num_calls
    def test_on_complete():
        global num_calls
        num_calls += 1
    timer = Timer(duration=2, on_complete=test_on_complete)
    timer.start()
    time.sleep(1)
    timer.tick()
    assert num_calls == 0
    time.sleep(1)
    timer.tick()
    assert num_calls == 1
    time.sleep(1)
    timer.tick()
    assert num_calls == 1