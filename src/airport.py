class Airport:
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.planes = []
        self.capacity = capacity

    def get_planes(self):
        return self.planes
        
    def land(self, plane):
        if len(self.planes) < self.capacity:
            self.planes.append(plane)
            return self.planes
        else:
            raise AirportIsFull("The airport is full!")

    def takeoff(self, plane):
        self.planes.remove(plane)
        return self.planes

class AirportIsFull(Exception):
    pass
