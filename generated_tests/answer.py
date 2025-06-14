def answer(L,R): 
    if (2 * L <= R): 
        return (L ,2*L)
    else: 
        return (-1)

import pytest

def test_L_is_exactly_half_of_R():
    # Since 2 * L = 10 which is equal to R, the condition 2 * L <= R holds True,
    # so the function returns (L, 2*L) which is (5, 10).
    assert answer(5, 10) == (5, 10)

def test_L_is_less_than_half_of_R():
    # 2 * L = 6 which is less than R=10, so the condition 2 * L <= R is True,
    # and the function returns (3, 6).
    assert answer(3, 10) == (3, 6)

def test_L_is_more_than_half_of_R():
    # 2 * L = 12 which is greater than R=10, so the condition 2 * L <= R is False,
    # and the function returns -1.
    assert answer(6, 10) == -1

def test_L_equals_R():
    # 2 * L = 20 which is greater than R=10, so the condition 2 * L <= R is False,
    # and the function returns -1.
    assert answer(10, 10) == -1

def test_L_is_zero():
    # 2 * L = 0 which is less than R=10, so the condition 2 * L <= R is True,
    # and the function returns (0, 0).
    assert answer(0, 10) == (0, 0)