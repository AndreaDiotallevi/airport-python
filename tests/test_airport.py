from src.airport import Airport

def test_no_planes_by_default():
  airport = Airport()
  assert airport.planes == []
  