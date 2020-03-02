import pytest
from unittest.mock import MagicMock
from src.airport import Airport, AirportIsFull, PlaneAlreadyLanded, PlaneNotLandedHere, StormyWeather
from src.plane import Plane
from src.weather import Weather

@pytest.fixture
def mock_plane():
    return MagicMock(spec=Plane)

@pytest.fixture
def mock_weather():
    return MagicMock(spec=Weather)

def test_no_planes_by_default():
    airport = Airport()

    assert airport.get_planes() == []

def test_land_plane(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_plane.is_landed.return_value = False
    mock_weather.is_stormy.return_value = False
    
    assert airport.land(mock_plane) == [mock_plane]

def test_prevent_land_if_plane_already_landed(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_plane.is_landed.return_value = True
    mock_weather.is_stormy.return_value = False

    with pytest.raises(PlaneAlreadyLanded):
        airport.land(mock_plane)

def test_prevent_land_when_airport_is_full(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_plane.is_landed.return_value = False
    mock_weather.is_stormy.return_value = False

    for i in range(airport.capacity):
        airport.land(mock_plane)
        
    with pytest.raises(AirportIsFull):
        airport.land(mock_plane)

def test_takeoff_plane_that_has_landed_there(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_plane.is_landed.return_value = False
    mock_weather.is_stormy.return_value = False

    airport.land(mock_plane)

    mock_plane.is_landed.return_value = True
    
    assert airport.takeoff(mock_plane) == []

def test_prevent_takeoff_if_plane_not_landed_there(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_weather.is_stormy.return_value = False

    with pytest.raises(PlaneNotLandedHere):
        airport.takeoff(mock_plane)

def test_prevent_land_when_whether_is_stormy(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_weather.is_stormy.return_value = True
    mock_plane.is_landed.return_value = False

    with pytest.raises(StormyWeather):
        airport.land(mock_plane)

def test_prevent_takeoff_when_whether_is_stormy(mock_plane, mock_weather):
    airport = Airport(weather = mock_weather)
    mock_plane.is_landed.return_value = False
    mock_weather.is_stormy.return_value = False

    airport.land(mock_plane)

    mock_plane.is_landed.return_value = True
    mock_weather.is_stormy.return_value = True

    with pytest.raises(StormyWeather):
        airport.takeoff(mock_plane)
