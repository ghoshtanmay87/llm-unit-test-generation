def is_Sum_Of_Powers_Of_Two(n): 
    if (n % 2 == 1): 
        return False
    else: 
        return True

import pytest

def test_is_Sum_Of_Powers_Of_Two_with_odd_number():
    # Input is an odd number
    n = 3
    expected = False
    assert is_Sum_Of_Powers_Of_Two(n) == expected

def test_is_Sum_Of_Powers_Of_Two_with_even_number():
    # Input is an even number
    n = 4
    expected = True
    assert is_Sum_Of_Powers_Of_Two(n) == expected

def test_is_Sum_Of_Powers_Of_Two_with_zero():
    # Input is zero
    n = 0
    expected = True
    assert is_Sum_Of_Powers_Of_Two(n) == expected

def test_is_Sum_Of_Powers_Of_Two_with_large_odd_number():
    # Input is a large odd number
    n = 999999
    expected = False
    assert is_Sum_Of_Powers_Of_Two(n) == expected

def test_is_Sum_Of_Powers_Of_Two_with_large_even_number():
    # Input is a large even number
    n = 1000000
    expected = True
    assert is_Sum_Of_Powers_Of_Two(n) == expected