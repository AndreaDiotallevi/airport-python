class Airport:
    CAPACITY = 10

    def __init__(self):
        self.planes = []

    def get_planes(self):
        return self.planes
        
    def land(self, plane):
        if len(self.planes) < self.CAPACITY:
            self.planes.append(plane)
            return self.planes
        else:
            raise AirportIsFull("The airport is full!")

    def takeoff(self, plane):
        self.planes.remove(plane)
        return self.planes

class AirportIsFull(Exception):
    pass
