
class Repository():
    def __init__(self):
        self.db = None
        self.sensors = {}

    def set_db(self, db):
        self.db = db

    def get_db(self):
        return self.db

    def add_sensor(self, name, sensor):
        self.sensors[name] = sensor

    def get_sensor(self, name):
        return self.sensors[name]

    

    