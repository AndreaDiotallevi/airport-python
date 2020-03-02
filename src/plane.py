class Plane:
    def __init__(self):
        self.landed = False

    def is_landed(self):
        return self.landed

    def land(self):
        self.landed = True

    def takeoff(self):
        self.landed = False
