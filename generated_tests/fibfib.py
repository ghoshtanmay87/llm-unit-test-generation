def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

import pytest

def test_fibfib_base_case_n_0():
    # Base case when n is 0
    result = fibfib(0)
    assert result == 0

def test_fibfib_base_case_n_1():
    # Base case when n is 1
    result = fibfib(1)
    assert result == 0

def test_fibfib_base_case_n_2():
    # Base case when n is 2
    result = fibfib(2)
    assert result == 1

def test_fibfib_calculate_n_3():
    # Calculate fibfib(3) using recursion
    result = fibfib(3)
    assert result == 1

def test_fibfib_calculate_n_4():
    # Calculate fibfib(4) using recursion
    result = fibfib(4)
    assert result == 2

def test_fibfib_calculate_n_5():
    # Calculate fibfib(5) using recursion
    result = fibfib(5)
    assert result == 4

def test_fibfib_calculate_n_6():
    # Calculate fibfib(6) using recursion
    result = fibfib(6)
    assert result == 7

def test_fibfib_calculate_n_7():
    # Calculate fibfib(7) using recursion
    result = fibfib(7)
    assert result == 13