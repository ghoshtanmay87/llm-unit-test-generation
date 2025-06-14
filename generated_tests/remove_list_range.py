def remove_list_range(list1, leftrange, rigthrange):
   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]
   return result

import pytest

def test_remove_sublists_within_range_2_to_5():
    list1 = [[1, 2], [3, 4], [5, 6], [2, 5]]
    leftrange = 2
    rigthrange = 5
    expected_output = [[3, 4], [2, 5]]
    assert remove_list_range(list1, leftrange, rigthrange) == expected_output

def test_remove_sublists_within_range_0_to_10():
    list1 = [[0, 10], [5, 5], [11, 12], [3, 7]]
    leftrange = 0
    rigthrange = 10
    expected_output = [[0, 10], [5, 5], [3, 7]]
    assert remove_list_range(list1, leftrange, rigthrange) == expected_output

def test_remove_sublists_within_single_value_range_5_to_5():
    list1 = [[5, 5], [5, 6], [4, 5], [5]]
    leftrange = 5
    rigthrange = 5
    expected_output = [[5, 5], [5]]
    assert remove_list_range(list1, leftrange, rigthrange) == expected_output

def test_empty_input_list_returns_empty_output():
    list1 = []
    leftrange = 0
    rigthrange = 10
    expected_output = []
    assert remove_list_range(list1, leftrange, rigthrange) == expected_output

def test_all_sublists_outside_range_10_to_20_removed():
    list1 = [[9, 10], [15, 18], [20, 21], [10, 20]]
    leftrange = 10
    rigthrange = 20
    expected_output = [[15, 18], [10, 20]]
    assert remove_list_range(list1, leftrange, rigthrange) == expected_output