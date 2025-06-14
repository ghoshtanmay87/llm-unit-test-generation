def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result

import pytest

def test_all_nested_lists_have_common_elements():
    nestedlist = [[1, 2, 3], [2, 3, 4], [2, 5, 6]]
    expected_output = [2]
    assert common_in_nested_lists(nestedlist) == expected_output

def test_no_common_elements_across_nested_lists():
    nestedlist = [[1, 2], [3, 4], [5, 6]]
    expected_output = []
    assert common_in_nested_lists(nestedlist) == expected_output

def test_single_nested_list_input():
    nestedlist = [[1, 2, 3]]
    expected_output = [1, 2, 3]
    assert common_in_nested_lists(nestedlist) == expected_output

def test_nested_lists_with_duplicate_elements_inside():
    nestedlist = [[1, 1, 2, 2], [2, 2, 3, 3], [2, 4, 4]]
    expected_output = [2]
    assert common_in_nested_lists(nestedlist) == expected_output

def test_empty_nested_list_input():
    nestedlist = []
    expected_output = []
    assert common_in_nested_lists(nestedlist) == expected_output

def test_nested_lists_where_one_list_is_empty():
    nestedlist = [[1, 2, 3], [], [2, 3, 4]]
    expected_output = []
    assert common_in_nested_lists(nestedlist) == expected_output

def test_nested_lists_with_all_identical_lists():
    nestedlist = [[1, 2], [1, 2], [1, 2]]
    expected_output = [1, 2]
    assert common_in_nested_lists(nestedlist) == expected_output