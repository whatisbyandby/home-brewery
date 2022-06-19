import asyncio
from datetime import datetime, timedelta


class Timer:
    def __init__(self, duration, timer_name, callback, tick_interval=1):
        self._name = timer_name
        self._callback = callback
        self._ok = True
        self._time_started = datetime.now()
        self._duration = timedelta(minutes=duration)
        self._time_remaining = self._duration
        self._time_remaining

    def start(self):
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        try:
            while self._ok:
                await asyncio.sleep(self._tick_interval)
                self._tick()
        except Exception as ex:
            print(ex)

    def _tick(self):
        # Update the time remaining
        self._time_remaining = self._duration - \
            (datetime.now() - self._time_started)
        print(self.format_time_remaining())
        if self._time_remaining.total_seconds() <= 0:
            self._ok = False
            self._callback(self._name)
            print("Timer " + self._name + " expired")

    def cancel(self):
        self._ok = False
        self._task.cancel()

    def format_time_remaining(self) -> str:
        hours = int(self._time_remaining.total_seconds() / 3600)
        minutes = int(self._time_remaining.total_seconds() / 60) % 60
        seconds = int(self._time_remaining.total_seconds()) % 60
        return f'{hours:02}:{minutes:02}:{seconds:02}'


def some_callback(timer_name):
    print("Some callback is finished")


if __name__ == "__main__":
    timer1 = Timer(tick_interval=1, duration=1, first_immediately=True,
                   timer_name="Timer 1", callback=some_callback)
    try:
        timer1.start()
        loop = asyncio.get_event_loop()
        loop.run_forever()
    except KeyboardInterrupt:
        timer1.cancel()
        print("clean up done")
