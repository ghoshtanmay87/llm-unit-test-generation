def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm

import pytest

def test_lcm_two_equal_positive_integers():
    # LCM of two equal positive integers
    x = 5
    y = 5
    expected = 5
    assert lcm(x, y) == expected

def test_lcm_x_less_than_y():
    # LCM where x is less than y
    x = 4
    y = 6
    expected = 12
    assert lcm(x, y) == expected

def test_lcm_x_greater_than_y():
    # LCM where x is greater than y
    x = 15
    y = 10
    expected = 30
    assert lcm(x, y) == expected

def test_lcm_two_prime_numbers():
    # LCM of two prime numbers
    x = 7
    y = 11
    expected = 77
    assert lcm(x, y) == expected

def test_lcm_one_number_is_one():
    # LCM where one number is 1
    x = 1
    y = 9
    expected = 9
    assert lcm(x, y) == expected