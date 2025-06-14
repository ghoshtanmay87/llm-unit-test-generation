from math import radians, sin, cos, acos
def distance_lat_long(slat,slon,elat,elon):
 dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
 return dist

import pytest

def test_distance_identical_points_equator():
    # Calculate distance between two identical points at the equator
    slat = 0.0
    slon = 0.0
    elat = 0.0
    elon = 0.0
    expected = 0.0
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected

def test_distance_equator_1_radian_longitude():
    # Calculate distance between two points on the equator 1 radian apart in longitude
    slat = 0.0
    slon = 0.0
    elat = 0.0
    elon = 1.0
    expected = 6371.01
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected

def test_distance_north_pole_to_equator_longitude_0():
    # Calculate distance between North Pole and Equator at longitude 0
    slat = 1.57079632679
    slon = 0.0
    elat = 0.0
    elon = 0.0
    expected = 10007.543
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected

def test_distance_equator_90_degrees_longitude():
    # Calculate distance between two points on the equator 90 degrees (pi/2 radians) apart in longitude
    slat = 0.0
    slon = 0.0
    elat = 0.0
    elon = 1.57079632679
    expected = 10007.543
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected

def test_distance_same_latitude_45_degrees_longitude_0():
    # Calculate distance between two points at latitude 45 degrees (pi/4 radians) and longitude difference 0
    slat = 0.78539816339
    slon = 0.0
    elat = 0.78539816339
    elon = 0.0
    expected = 0.0
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected

def test_distance_latitude_45_degrees_longitude_1_radian():
    # Calculate distance between two points at latitude 45 degrees (pi/4 radians) and longitude difference 1 radian
    slat = 0.78539816339
    slon = 0.0
    elat = 0.78539816339
    elon = 1.0
    expected = 4504.977
    result = distance_lat_long(slat, slon, elat, elon)
    assert result == expected