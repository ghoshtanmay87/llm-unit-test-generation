def min_of_three(a,b,c): 
      if (a <= b) and (a <= c): 
        smallest = a 
      elif (b <= a) and (b <= c): 
        smallest = b 
      else: 
        smallest = c 
      return smallest

import pytest

def test_min_of_three_all_distinct_a_smallest():
    # All inputs are distinct and a is the smallest
    result = min_of_three(a=1, b=2, c=3)
    assert result == 1

def test_min_of_three_all_distinct_b_smallest():
    # All inputs are distinct and b is the smallest
    result = min_of_three(a=5, b=3, c=4)
    assert result == 3

def test_min_of_three_all_distinct_c_smallest():
    # All inputs are distinct and c is the smallest
    result = min_of_three(a=7, b=8, c=6)
    assert result == 6

def test_min_of_three_two_equal_smallest_a_and_b():
    # Two inputs are equal and smallest (a and b equal and smallest)
    result = min_of_three(a=2, b=2, c=5)
    assert result == 2

def test_min_of_three_two_equal_smallest_b_and_c():
    # Two inputs are equal and smallest (b and c equal and smallest)
    result = min_of_three(a=10, b=4, c=4)
    assert result == 4

def test_min_of_three_all_equal():
    # All inputs are equal
    result = min_of_three(a=9, b=9, c=9)
    assert result == 9

def test_min_of_three_negative_numbers_c_smallest():
    # Negative numbers with c smallest
    result = min_of_three(a=-1, b=0, c=-5)
    assert result == -5

def test_min_of_three_negative_numbers_a_smallest():
    # Negative numbers with a smallest
    result = min_of_three(a=-10, b=-3, c=-7)
    assert result == -10

def test_min_of_three_floating_point_b_smallest():
    # Floating point numbers with b smallest
    result = min_of_three(a=2.5, b=1.1, c=3.3)
    assert result == 1.1

def test_min_of_three_mixed_int_float_c_smallest():
    # Mixed integer and float with c smallest
    result = min_of_three(a=4, b=4.5, c=3.9)
    assert result == 3.9