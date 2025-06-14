def armstrong_number(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False

import pytest

def test_armstrong_number_153():
    # Check if 153 is an Armstrong number
    result = armstrong_number(153)
    assert result is True

def test_armstrong_number_9474():
    # Check if 9474 is an Armstrong number
    result = armstrong_number(9474)
    assert result is True

def test_armstrong_number_9475():
    # Check if 9475 is an Armstrong number
    result = armstrong_number(9475)
    assert result is False

def test_armstrong_number_0():
    # Check if 0 is an Armstrong number
    result = armstrong_number(0)
    assert result is True

def test_armstrong_number_1():
    # Check if 1 is an Armstrong number
    result = armstrong_number(1)
    assert result is True

def test_armstrong_number_10():
    # Check if 10 is an Armstrong number
    result = armstrong_number(10)
    assert result is False

def test_armstrong_number_370():
    # Check if 370 is an Armstrong number
    result = armstrong_number(370)
    assert result is True

def test_armstrong_number_407():
    # Check if 407 is an Armstrong number
    result = armstrong_number(407)
    assert result is True

def test_armstrong_number_123():
    # Check if 123 is an Armstrong number
    result = armstrong_number(123)
    assert result is False