def count_Num(n): 
    if (n == 1): 
        return 1
    count = pow(2,n - 2) 
    return count

import pytest

def test_count_Num_base_case_n_1():
    # Input is 1, the base case
    result = count_Num(1)
    assert result == 1

def test_count_Num_smallest_n_greater_than_1_n_2():
    # Input is 2, smallest n greater than 1
    result = count_Num(2)
    assert result == 1

def test_count_Num_small_integer_n_3():
    # Input is 3, a small integer greater than 2
    result = count_Num(3)
    assert result == 2

def test_count_Num_small_integer_n_4():
    # Input is 4, a small integer greater than 3
    result = count_Num(4)
    assert result == 4

def test_count_Num_larger_integer_n_10():
    # Input is 10, a larger integer
    result = count_Num(10)
    assert result == 256