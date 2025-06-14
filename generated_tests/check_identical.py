def check_identical(test_list1, test_list2):
  res = test_list1 == test_list2
  return (res)

import pytest

def test_both_lists_exactly_same_integers():
    test_list1 = [1, 2, 3]
    test_list2 = [1, 2, 3]
    expected_output = True
    assert check_identical(test_list1, test_list2) == expected_output

def test_lists_same_elements_different_order():
    test_list1 = [1, 2, 3]
    test_list2 = [3, 2, 1]
    expected_output = False
    assert check_identical(test_list1, test_list2) == expected_output

def test_lists_differ_by_one_element():
    test_list1 = [1, 2, 3]
    test_list2 = [1, 2, 4]
    expected_output = False
    assert check_identical(test_list1, test_list2) == expected_output

def test_both_lists_empty():
    test_list1 = []
    test_list2 = []
    expected_output = True
    assert check_identical(test_list1, test_list2) == expected_output

def test_lists_same_elements_order_different_types():
    test_list1 = [1, 2, 3]
    test_list2 = [1, 2, 3.0]
    expected_output = True
    assert check_identical(test_list1, test_list2) == expected_output

def test_lists_with_nested_lists_identical():
    test_list1 = [[1, 2], [3, 4]]
    test_list2 = [[1, 2], [3, 4]]
    expected_output = True
    assert check_identical(test_list1, test_list2) == expected_output

def test_lists_with_nested_lists_differ_in_inner_list():
    test_list1 = [[1, 2], [3, 4]]
    test_list2 = [[1, 2], [4, 3]]
    expected_output = False
    assert check_identical(test_list1, test_list2) == expected_output