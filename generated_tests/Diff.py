def Diff(li1,li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

import pytest

def test_diff_some_unique_and_common_elements():
    li1 = [1, 2, 3]
    li2 = [2, 3, 4]
    expected_output = [1, 4]
    assert Diff(li1, li2) == expected_output

def test_diff_one_list_empty_other_has_elements():
    li1 = []
    li2 = [5, 6]
    expected_output = [5, 6]
    assert Diff(li1, li2) == expected_output

def test_diff_both_lists_identical():
    li1 = [7, 8, 9]
    li2 = [7, 8, 9]
    expected_output = []
    assert Diff(li1, li2) == expected_output

def test_diff_lists_no_common_elements():
    li1 = [10, 11]
    li2 = [12, 13]
    expected_output = [10, 11, 12, 13]
    assert Diff(li1, li2) == expected_output

def test_diff_lists_with_duplicate_elements():
    li1 = [1, 1, 2, 2]
    li2 = [2, 3, 3]
    expected_output = [1, 3]
    assert Diff(li1, li2) == expected_output