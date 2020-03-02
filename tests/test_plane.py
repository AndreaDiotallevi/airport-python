import pytest
from src.plane import Plane

def test_plane_is_not_landed_by_default():
    plane = Plane()

    assert plane.is_landed() == False

def test_plane_is_landed_after_having_landed():
    plane = Plane()
    plane.land()

    assert plane.is_landed() == True

def test_plane_is_not_landed_after_having_landed_and_takenoff():
    plane = Plane()
    plane.land()
    plane.takeoff()

    assert plane.is_landed() == False
