def find_Min_Sum(a,b,n): 
    a.sort() 
    b.sort() 
    sum = 0  
    for i in range(n): 
        sum = sum + abs(a[i] - b[i]) 
    return sum

import pytest

def test_both_lists_identical_and_sorted():
    a = [1, 2, 3]
    b = [1, 2, 3]
    n = 3
    expected = 0
    assert find_Min_Sum(a, b, n) == expected

def test_lists_reversed_versions_of_each_other():
    a = [1, 2, 3]
    b = [3, 2, 1]
    n = 3
    expected = 0
    assert find_Min_Sum(a, b, n) == expected

def test_lists_with_different_elements():
    a = [1, 4, 5]
    b = [2, 3, 6]
    n = 3
    expected = 3
    assert find_Min_Sum(a, b, n) == expected

def test_lists_with_negative_and_positive_numbers():
    a = [-1, 0, 1]
    b = [1, 0, -1]
    n = 3
    expected = 0
    assert find_Min_Sum(a, b, n) == expected

def test_lists_with_duplicates():
    a = [1, 2, 2, 3]
    b = [2, 2, 3, 4]
    n = 4
    expected = 3
    assert find_Min_Sum(a, b, n) == expected

def test_empty_lists():
    a = []
    b = []
    n = 0
    expected = 0
    assert find_Min_Sum(a, b, n) == expected

def test_single_element_lists_with_different_values():
    a = [10]
    b = [5]
    n = 1
    expected = 5
    assert find_Min_Sum(a, b, n) == expected