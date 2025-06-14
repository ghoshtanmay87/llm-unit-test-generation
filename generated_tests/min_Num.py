def min_Num(arr,n):  
    odd = 0
    for i in range(n): 
        if (arr[i] % 2): 
            odd += 1 
    if (odd % 2): 
        return 1
    return 2

import pytest

def test_all_elements_even_numbers():
    # All elements are even numbers
    arr = [2, 4, 6, 8]
    n = 4
    expected = 2
    assert min_Num(arr, n) == expected

def test_array_contains_one_odd_number():
    # Array contains one odd number
    arr = [1, 2, 4, 6]
    n = 4
    expected = 1
    assert min_Num(arr, n) == expected

def test_array_contains_multiple_odd_numbers_with_odd_count():
    # Array contains multiple odd numbers with odd count
    arr = [1, 3, 5, 2]
    n = 4
    expected = 1
    assert min_Num(arr, n) == expected

def test_array_contains_multiple_odd_numbers_with_even_count():
    # Array contains multiple odd numbers with even count
    arr = [1, 3, 2, 4]
    n = 4
    expected = 2
    assert min_Num(arr, n) == expected

def test_empty_array():
    # Empty array
    arr = []
    n = 0
    expected = 2
    assert min_Num(arr, n) == expected

def test_array_with_all_odd_numbers_and_odd_count():
    # Array with all odd numbers and odd count
    arr = [7, 9, 11]
    n = 3
    expected = 1
    assert min_Num(arr, n) == expected

def test_array_with_all_odd_numbers_and_even_count():
    # Array with all odd numbers and even count
    arr = [7, 9, 11, 13]
    n = 4
    expected = 2
    assert min_Num(arr, n) == expected