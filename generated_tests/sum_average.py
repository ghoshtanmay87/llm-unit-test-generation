def sum_average(number):
 total = 0
 for value in range(1, number + 1):
    total = total + value
 average = total / number
 return (total,average)

import pytest

def test_sum_average_number_1():
    # Calculate sum and average for number = 1
    result = sum_average(1)
    expected = (1, 1.0)
    assert result == expected

def test_sum_average_number_3():
    # Calculate sum and average for number = 3
    result = sum_average(3)
    expected = (6, 2.0)
    assert result == expected

def test_sum_average_number_5():
    # Calculate sum and average for number = 5
    result = sum_average(5)
    expected = (15, 3.0)
    assert result == expected

def test_sum_average_number_10():
    # Calculate sum and average for number = 10
    result = sum_average(10)
    expected = (55, 5.5)
    assert result == expected

def test_sum_average_number_100():
    # Calculate sum and average for number = 100
    result = sum_average(100)
    expected = (5050, 50.5)
    assert result == expected