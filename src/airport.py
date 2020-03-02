from src.weather import Weather

class Airport:
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity = DEFAULT_CAPACITY, weather = Weather()):
        self.planes = []
        self.capacity = capacity
        self.weather = weather

    def get_planes(self):
        return self.planes
        
    def land(self, plane):
        if len(self.planes) == self.capacity:
            raise AirportIsFull("The airport is full!")
        elif plane.is_landed():
            raise PlaneAlreadyLanded("This plane has already landed!")
        elif self.weather.is_stormy():
            raise StormyWeather("The weather is stormy!")
        self.planes.append(plane)
        return self.planes

    def takeoff(self, plane):
        if plane not in self.planes:
            raise PlaneNotLandedHere("This plane has not landed here!")
        elif self.weather.is_stormy():
            raise StormyWeather("The weather is stormy!")
        self.planes.remove(plane)
        return self.planes

class AirportIsFull(Exception):
    pass

class PlaneAlreadyLanded(Exception):
    pass

class PlaneNotLandedHere(Exception):
    pass

class StormyWeather(Exception):
    pass
