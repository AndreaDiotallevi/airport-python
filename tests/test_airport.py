import pytest
from unittest.mock import MagicMock
from src.airport import Airport, AirportIsFull, PlaneAlreadyLanded
from src.plane import Plane

# @pytest.fixture
# def mock_plane():
#     return MagicMock(spec=Plane)

# def test_no_planes_by_default():
#     airport = Airport()

#     assert airport.get_planes() == []

# def test_land_plane(mock_plane):
#     airport = Airport()
    
#     assert airport.land(mock_plane) == [mock_plane]

# def test_prevent_land_if_plane_already_landed(mock_plane):
#     airport = Airport()
#     plane = mock_plane
#     airport.land(plane)

#     with pytest.raises(PlaneAlreadyLanded):
#         airport.land(plane)

# def test_prevent_land_when_airport_is_full(mock_plane):
#     airport = Airport()
#     for i in range(airport.capacity):
#         plane = mock_plane
#         airport.land(plane)
        
#     with pytest.raises(AirportIsFull):
#         airport.land(mock_plane)

# def test_prevent_land_when_airport_is_full_with_overidden_capacity(mock_plane):
#     capacity = 5
#     airport = Airport(5)
#     for i in range(capacity):
#         airport.land(mock_plane)
        
#     with pytest.raises(AirportIsFull):
#         airport.land(mock_plane)

# def test_takeoff_plane(mock_plane):
#     airport = Airport()
#     airport.land(mock_plane)
    
#     assert airport.takeoff(mock_plane) == []
