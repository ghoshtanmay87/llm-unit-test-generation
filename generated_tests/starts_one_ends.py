def starts_one_ends(n):
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)

import pytest

def test_starts_one_ends_with_input_1():
    # Input is 1, the smallest valid input
    # The function explicitly returns 1 when n equals 1.
    assert starts_one_ends(1) == 1

def test_starts_one_ends_with_input_2():
    # Input is 2, the smallest n greater than 1
    # For n=2, the function returns 18 * 10^(2-2) = 18 * 10^0 = 18 * 1 = 18.
    assert starts_one_ends(2) == 18

def test_starts_one_ends_with_input_3():
    # Input is 3, a small number greater than 2
    # For n=3, the function returns 18 * 10^(3-2) = 18 * 10^1 = 18 * 10 = 180.
    assert starts_one_ends(3) == 180

def test_starts_one_ends_with_input_4():
    # Input is 4, a moderate number
    # For n=4, the function returns 18 * 10^(4-2) = 18 * 10^2 = 18 * 100 = 1800.
    assert starts_one_ends(4) == 1800

def test_starts_one_ends_with_input_5():
    # Input is 5, a larger number
    # For n=5, the function returns 18 * 10^(5-2) = 18 * 10^3 = 18 * 1000 = 18000.
    assert starts_one_ends(5) == 18000