def find_Max_Num(arr,n) : 
    arr.sort(reverse = True) 
    num = arr[0] 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
    return num

import pytest

def test_find_max_num_single_digit_list():
    # Find max number from a list of single-digit integers
    arr = [3, 1, 4, 2]
    n = 4
    expected_output = 4321
    assert find_Max_Num(arr, n) == expected_output

def test_find_max_num_with_repeated_digits():
    # Find max number from a list with repeated digits
    arr = [9, 9, 1, 0]
    n = 4
    expected_output = 9910
    assert find_Max_Num(arr, n) == expected_output

def test_find_max_num_single_element_list():
    # Find max number from a single-element list
    arr = [7]
    n = 1
    expected_output = 7
    assert find_Max_Num(arr, n) == expected_output

def test_find_max_num_with_zeros_and_small_digits():
    # Find max number from a list with zeros and small digits
    arr = [0, 0, 1, 2]
    n = 4
    expected_output = 2100
    assert find_Max_Num(arr, n) == expected_output

def test_find_max_num_ascending_order_digits():
    # Find max number from a list with digits in ascending order
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected_output = 54321
    assert find_Max_Num(arr, n) == expected_output