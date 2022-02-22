from datetime import datetime, timedelta


class Step:
    def __init__(self, name, duration, units='minutes'):
        self.name = name
        self.units = units
        self.duration = duration
        self.start_time = None
        self.completed_time = None
        self.completed = False

    def start(self):
        self.start_time = datetime.now()

    def is_completed(self):
        if datetime.now() - self.start_time > timedelta(**{self.units: self.duration}):
            self.completed = True
            self.completed_time = datetime.now()
            return True
        return False
