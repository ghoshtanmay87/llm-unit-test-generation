import math
def wind_chill(v,t):
 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
 return int(round(windchill, 0))

import pytest

def test_wind_chill_moderate_wind_and_temperature():
    # scenario: Calculate wind chill for moderate wind and temperature
    v = 10
    t = 5
    expected = -1
    result = wind_chill(v, t)
    assert result == expected

def test_wind_chill_zero_wind_speed():
    # scenario: Calculate wind chill for zero wind speed
    v = 0
    t = 0
    expected = 0
    result = wind_chill(v, t)
    assert result == expected

def test_wind_chill_high_wind_low_temperature():
    # scenario: Calculate wind chill for high wind speed and low temperature
    v = 50
    t = -10
    expected = -22
    result = wind_chill(v, t)
    assert result == expected

def test_wind_chill_no_wind_positive_temperature():
    # scenario: Calculate wind chill for no wind and positive temperature
    v = 0
    t = 20
    expected = 25
    result = wind_chill(v, t)
    assert result == expected

def test_wind_chill_low_wind_negative_temperature():
    # scenario: Calculate wind chill for low wind speed and negative temperature
    v = 2
    t = -5
    expected = -7
    result = wind_chill(v, t)
    assert result == expected