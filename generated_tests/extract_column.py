def extract_column(list1, n):
   result = [i.pop(n) for i in list1]
   return result

import pytest

def test_extract_first_column_multiple_elements():
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = 0
    expected_output = [1, 4, 7]
    assert extract_column(list1, n) == expected_output

def test_extract_second_column_multiple_elements():
    list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    n = 1
    expected_output = [20, 50, 80]
    assert extract_column(list1, n) == expected_output

def test_extract_last_column_three_elements_each():
    list1 = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
    n = 2
    expected_output = [300, 600, 900]
    assert extract_column(list1, n) == expected_output

def test_extract_only_element_single_element_lists():
    list1 = [[42], [43], [44]]
    n = 0
    expected_output = [42, 43, 44]
    assert extract_column(list1, n) == expected_output

def test_extract_middle_element_three_elements_with_strings():
    list1 = [[1, 'a', 3], [4, 'b', 6], [7, 'c', 9]]
    n = 1
    expected_output = ['a', 'b', 'c']
    assert extract_column(list1, n) == expected_output