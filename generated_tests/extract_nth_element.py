def extract_nth_element(list1, n):
    result = [x[n] for x in list1]
    return result

import pytest

def test_extract_0th_element_from_each_sublists():
    list1 = [[1, 2], [3, 4], [5, 6]]
    n = 0
    expected_output = [1, 3, 5]
    assert extract_nth_element(list1, n) == expected_output

def test_extract_1st_element_from_each_sublists():
    list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    n = 1
    expected_output = [20, 50, 80]
    assert extract_nth_element(list1, n) == expected_output

def test_extract_2nd_element_from_each_sublists_with_varying_lengths():
    list1 = [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
    n = 2
    expected_output = [9, 3, 6]
    assert extract_nth_element(list1, n) == expected_output

def test_extract_0th_element_from_sublists_containing_strings():
    list1 = [['apple', 'banana'], ['cherry', 'date'], ['fig', 'grape']]
    n = 0
    expected_output = ['apple', 'cherry', 'fig']
    assert extract_nth_element(list1, n) == expected_output

def test_extract_1st_element_from_sublists_containing_mixed_data_types():
    list1 = [[100, 'a'], [200, 'b'], [300, 'c']]
    n = 1
    expected_output = ['a', 'b', 'c']
    assert extract_nth_element(list1, n) == expected_output