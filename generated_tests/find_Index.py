import math 
def find_Index(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1))); 
    return round(x);

import pytest

def test_find_index_smallest_input_n_1():
    # For n=1, expected output is 1
    assert find_Index(1) == 1

def test_find_index_small_input_n_2():
    # For n=2, expected output is 4
    assert find_Index(2) == 4

def test_find_index_moderate_input_n_3():
    # For n=3, expected output is 13
    assert find_Index(3) == 13

def test_find_index_larger_input_n_4():
    # For n=4, expected output is 45
    assert find_Index(4) == 45

def test_find_index_larger_input_n_5():
    # For n=5, expected output is 142
    assert find_Index(5) == 142