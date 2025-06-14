def sum_Natural(n): 
    sum = (n * (n + 1)) 
    return int(sum) 
def sum_Even(l,r): 
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2)))

import pytest

def test_sum_even_1_to_10():
    # Sum of even numbers between 1 and 10
    result = sum_Even(1, 10)
    assert result == 30

def test_sum_even_2_to_2_single_even():
    # Sum of even numbers between 2 and 2 (single even number)
    result = sum_Even(2, 2)
    assert result == 2

def test_sum_even_3_to_7_corrected():
    # Sum of even numbers between 3 and 7 (corrected)
    result = sum_Even(3, 7)
    assert result == 10

def test_sum_even_0_to_0_no_numbers():
    # Sum of even numbers between 0 and 0 (no numbers)
    result = sum_Even(0, 0)
    assert result == 0

def test_sum_even_5_to_5_single_odd():
    # Sum of even numbers between 5 and 5 (single odd number)
    result = sum_Even(5, 5)
    assert result == 0

def test_sum_even_0_to_8():
    # Sum of even numbers between 0 and 8
    result = sum_Even(0, 8)
    assert result == 20