def get_odd_collatz(n):
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    return sorted(odd_collatz)

import pytest

def test_get_odd_collatz_with_input_1():
    # Input is 1, the smallest odd number, so list starts with [1] and no further steps
    result = get_odd_collatz(1)
    expected = [1]
    assert result == expected

def test_get_odd_collatz_with_input_2():
    # Input is 2, the smallest even number, so list starts empty and only odd numbers from sequence appended
    result = get_odd_collatz(2)
    expected = [1]
    assert result == expected

def test_get_odd_collatz_with_input_3():
    # Input is 3, an odd number, so list starts with [3] and odd numbers from sequence appended
    result = get_odd_collatz(3)
    expected = [1, 3, 5]
    assert result == expected

def test_get_odd_collatz_with_input_6():
    # Input is an even number, so initial list is empty and only odd numbers from the sequence are appended
    result = get_odd_collatz(6)
    expected = [1, 3, 5]
    assert result == expected

def test_get_odd_collatz_with_input_7():
    # Input is an odd number, so initial list starts with n and odd numbers from the sequence are appended
    result = get_odd_collatz(7)
    expected = [1, 5, 7, 11, 13, 17]
    assert result == expected