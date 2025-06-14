import math 
def sum_series(number):
 total = 0
 total = math.pow((number * (number + 1)) /2, 2)
 return total

import pytest

def test_sum_series_number_1():
    # Calculate sum_series for number = 1
    result = sum_series(1)
    assert result == 1.0

def test_sum_series_number_2():
    # Calculate sum_series for number = 2
    result = sum_series(2)
    assert result == 9.0

def test_sum_series_number_3():
    # Calculate sum_series for number = 3
    result = sum_series(3)
    assert result == 36.0

def test_sum_series_number_4():
    # Calculate sum_series for number = 4
    result = sum_series(4)
    assert result == 100.0

def test_sum_series_number_5():
    # Calculate sum_series for number = 5
    result = sum_series(5)
    assert result == 225.0

def test_sum_series_number_10():
    # Calculate sum_series for number = 10
    result = sum_series(10)
    assert result == 3025.0