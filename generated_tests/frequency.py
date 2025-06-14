def frequency(a,x): 
    count = 0  
    for i in a: 
        if i == x: count += 1
    return count

import pytest

def test_frequency_element_multiple_times():
    # Count frequency of an element present multiple times in the list
    a = [1, 2, 3, 2, 4, 2, 5]
    x = 2
    expected = 3
    assert frequency(a, x) == expected

def test_frequency_element_once():
    # Count frequency of an element present once in the list
    a = [10, 20, 30, 40]
    x = 30
    expected = 1
    assert frequency(a, x) == expected

def test_frequency_element_not_present():
    # Count frequency of an element not present in the list
    a = [5, 6, 7, 8]
    x = 9
    expected = 0
    assert frequency(a, x) == expected

def test_frequency_empty_list():
    # Count frequency in an empty list
    a = []
    x = 1
    expected = 0
    assert frequency(a, x) == expected

def test_frequency_string_element():
    # Count frequency of a string element in a list of strings
    a = ['apple', 'banana', 'apple', 'cherry']
    x = 'apple'
    expected = 2
    assert frequency(a, x) == expected

def test_frequency_none_element():
    # Count frequency of None in a list containing None values
    a = [None, 1, None, 2, None]
    x = None
    expected = 3
    assert frequency(a, x) == expected

def test_frequency_float_element():
    # Count frequency of a float element in a list of floats
    a = [1.1, 2.2, 3.3, 2.2, 4.4]
    x = 2.2
    expected = 2
    assert frequency(a, x) == expected