def get_noOfways(n):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1; 
    return get_noOfways(n - 1) + get_noOfways(n - 2);

import pytest

def test_get_noOfways_n_0_base_case():
    # When n=0, the function directly returns 0 as per the first if condition.
    assert get_noOfways(0) == 0

def test_get_noOfways_n_1_base_case():
    # When n=1, the function directly returns 1 as per the second if condition.
    assert get_noOfways(1) == 1

def test_get_noOfways_n_2():
    # For n=2, the function returns get_noOfways(1) + get_noOfways(0) = 1 + 0 = 1.
    assert get_noOfways(2) == 1

def test_get_noOfways_n_3():
    # For n=3, the function returns get_noOfways(2) + get_noOfways(1) = 1 + 1 = 2.
    assert get_noOfways(3) == 2

def test_get_noOfways_n_4():
    # For n=4, the function returns get_noOfways(3) + get_noOfways(2) = 2 + 1 = 3.
    assert get_noOfways(4) == 3

def test_get_noOfways_n_5():
    # For n=5, the function returns get_noOfways(4) + get_noOfways(3) = 3 + 2 = 5.
    assert get_noOfways(5) == 5

def test_get_noOfways_n_6():
    # For n=6, the function returns get_noOfways(5) + get_noOfways(4) = 5 + 3 = 8.
    assert get_noOfways(6) == 8