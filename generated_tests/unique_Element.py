def unique_Element(arr,n):
    s = set(arr)
    if (len(s) == 1):
        return ('YES')
    else:
        return ('NO')

import pytest

def test_all_elements_identical():
    # All elements in the array are identical
    arr = [5, 5, 5, 5]
    n = 4
    expected = "YES"
    assert unique_Element(arr, n) == expected

def test_multiple_distinct_elements():
    # Array contains multiple distinct elements
    arr = [1, 2, 3, 4]
    n = 4
    expected = "NO"
    assert unique_Element(arr, n) == expected

def test_two_identical_elements():
    # Array with two identical elements
    arr = [7, 7]
    n = 2
    expected = "YES"
    assert unique_Element(arr, n) == expected

def test_single_element_array():
    # Array with one element
    arr = [42]
    n = 1
    expected = "YES"
    assert unique_Element(arr, n) == expected

def test_all_identical_strings():
    # Array with multiple elements but all identical strings
    arr = ['a', 'a', 'a']
    n = 3
    expected = "YES"
    assert unique_Element(arr, n) == expected

def test_duplicates_but_not_all_identical():
    # Array with multiple elements including duplicates but not all identical
    arr = [2, 2, 3, 2]
    n = 4
    expected = "NO"
    assert unique_Element(arr, n) == expected