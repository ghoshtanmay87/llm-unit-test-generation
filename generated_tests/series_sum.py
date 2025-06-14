def series_sum(number):
 total = 0
 total = (number * (number + 1) * (2 * number + 1)) / 6
 return total

import pytest

def test_series_sum_number_0():
    # Calculate series sum for number = 0
    result = series_sum(0)
    assert result == 0.0

def test_series_sum_number_1():
    # Calculate series sum for number = 1
    result = series_sum(1)
    assert result == 1.0

def test_series_sum_number_2():
    # Calculate series sum for number = 2
    result = series_sum(2)
    assert result == 5.0

def test_series_sum_number_3():
    # Calculate series sum for number = 3
    result = series_sum(3)
    assert result == 14.0

def test_series_sum_number_5():
    # Calculate series sum for number = 5
    result = series_sum(5)
    assert result == 55.0

def test_series_sum_number_10():
    # Calculate series sum for number = 10
    result = series_sum(10)
    assert result == 385.0