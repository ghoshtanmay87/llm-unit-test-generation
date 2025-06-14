def zip_list(list1,list2):  
 result = list(map(list.__add__, list1, list2)) 
 return result

import pytest

def test_zip_list_equal_length_integer_sublists():
    list1 = [[1, 2], [3, 4]]
    list2 = [[5, 6], [7, 8]]
    expected_output = [[1, 2, 5, 6], [3, 4, 7, 8]]
    assert zip_list(list1, list2) == expected_output

def test_zip_list_equal_length_empty_sublists():
    list1 = [[], [1]]
    list2 = [[2], []]
    expected_output = [[2], [1]]
    assert zip_list(list1, list2) == expected_output

def test_zip_list_one_empty_sublists_other_multiple_elements():
    list1 = [[1, 2, 3], []]
    list2 = [[], [4, 5]]
    expected_output = [[1, 2, 3], [4, 5]]
    assert zip_list(list1, list2) == expected_output

def test_zip_list_string_elements_in_sublists():
    list1 = [['a', 'b'], ['c']]
    list2 = [['d'], ['e', 'f']]
    expected_output = [['a', 'b', 'd'], ['c', 'e', 'f']]
    assert zip_list(list1, list2) == expected_output

def test_zip_list_two_empty_lists():
    list1 = []
    list2 = []
    expected_output = []
    assert zip_list(list1, list2) == expected_output