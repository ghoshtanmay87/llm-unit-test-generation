def count_Odd_Squares(n,m): 
    return int(m**0.5) - int((n-1)**0.5)

import pytest

def test_count_odd_squares_1_to_10():
    # Count odd squares between 1 and 10
    result = count_Odd_Squares(1, 10)
    assert result == 3

def test_count_odd_squares_3_to_15():
    # Count odd squares between 3 and 15
    result = count_Odd_Squares(3, 15)
    assert result == 2

def test_count_odd_squares_10_to_25():
    # Count odd squares between 10 and 25
    result = count_Odd_Squares(10, 25)
    assert result == 2

def test_count_odd_squares_16_to_16():
    # Count odd squares between 16 and 16 (single number range)
    result = count_Odd_Squares(16, 16)
    assert result == 1

def test_count_odd_squares_17_to_24():
    # Count odd squares between 17 and 24 (no perfect squares in range)
    result = count_Odd_Squares(17, 24)
    assert result == 0

def test_count_odd_squares_1_to_1():
    # Count odd squares between 1 and 1 (single number range at start)
    result = count_Odd_Squares(1, 1)
    assert result == 1

def test_count_odd_squares_0_to_0():
    # Count odd squares between 0 and 0 (zero range)
    result = count_Odd_Squares(0, 0)
    assert result == 0

def test_count_odd_squares_5_to_5():
    # Count odd squares between 5 and 5 (single number range, not a perfect square)
    result = count_Odd_Squares(5, 5)
    assert result == 0