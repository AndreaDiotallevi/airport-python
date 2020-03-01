class Airport:
    def __init__(self):
        self.planes = []

    def get_planes(self):
        return self.planes
        
    def land(self, plane):
        self.planes.append(plane)
        return plane
