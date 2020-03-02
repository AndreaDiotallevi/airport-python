import pytest
from src.weather import Weather
import random

def test_weather_is_stormy():
    random.seed(1)
    weather = Weather()

    assert weather.is_stormy() == False

def test_weather_is_not_stormy():
    random.seed(2)
    weather = Weather()

    assert weather.is_stormy() == True
