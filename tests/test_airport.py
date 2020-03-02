import pytest
from unittest.mock import MagicMock
from src.airport import Airport, AirportIsFull, PlaneAlreadyLanded, PlaneNotLandedHere
from src.plane import Plane

@pytest.fixture
def mock_plane():
    return MagicMock(spec=Plane)

def test_no_planes_by_default():
    airport = Airport()

    assert airport.get_planes() == []

def test_land_plane(mock_plane):
    airport = Airport()
    plane = mock_plane
    plane.is_landed.return_value = False
    
    assert airport.land(mock_plane) == [plane]

def test_prevent_land_if_plane_already_landed(mock_plane):
    airport = Airport()
    plane = mock_plane
    plane.is_landed.return_value = True

    with pytest.raises(PlaneAlreadyLanded):
        airport.land(plane)

def test_prevent_land_when_airport_is_full(mock_plane):
    airport = Airport()
    plane = mock_plane
    plane.is_landed.return_value = False

    for i in range(airport.capacity):
        airport.land(plane)
        
    with pytest.raises(AirportIsFull):
        airport.land(plane)

def test_takeoff_plane_that_has_landed_there(mock_plane):
    airport = Airport()
    plane = mock_plane
    plane.is_landed.return_value = False

    airport.land(plane)

    plane.is_landed.return_value = True
    
    assert airport.takeoff(plane) == []

def test_prevent_takeoff_if_plane_not_landed_there(mock_plane):
    airport = Airport()
    plane = mock_plane

    with pytest.raises(PlaneNotLandedHere):
        airport.takeoff(plane)
