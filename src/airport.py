class Airport:
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.planes = []
        self.capacity = capacity

    def get_planes(self):
        return self.planes
        
    def land(self, plane):
        if len(self.planes) == self.capacity:
            raise AirportIsFull("The airport is full!")
        elif plane.is_landed():
            raise PlaneAlreadyLanded("This plane has already landed!")
        self.planes.append(plane)
        return self.planes

    def takeoff(self, plane):
        if plane not in self.planes:
            raise PlaneNotLandedHere("This plane has not landed here!")
        self.planes.remove(plane)
        return self.planes

class AirportIsFull(Exception):
    pass

class PlaneAlreadyLanded(Exception):
    pass

class PlaneNotLandedHere(Exception):
    pass
