def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

import pytest

def test_even_odd_count_mixed_positive():
    # Count even and odd digits in a positive number with mixed digits
    result = even_odd_count(123456)
    assert result == (3, 3)

def test_even_odd_count_mixed_negative():
    # Count even and odd digits in a negative number with mixed digits
    result = even_odd_count(-246801)
    assert result == (5, 1)

def test_even_odd_count_zero():
    # Count even and odd digits in zero
    result = even_odd_count(0)
    assert result == (1, 0)

def test_even_odd_count_all_odd():
    # Count even and odd digits in a number with all odd digits
    result = even_odd_count(13579)
    assert result == (0, 5)

def test_even_odd_count_all_even():
    # Count even and odd digits in a number with all even digits
    result = even_odd_count(24680)
    assert result == (5, 0)

def test_even_odd_count_single_odd_digit():
    # Count even and odd digits in a single digit odd number
    result = even_odd_count(7)
    assert result == (0, 1)

def test_even_odd_count_single_even_digit():
    # Count even and odd digits in a single digit even number
    result = even_odd_count(8)
    assert result == (1, 0)