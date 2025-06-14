def count_samepair(list1,list2,list3):
    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))
    return result

import pytest

def test_all_identical_elements_all_positions():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 3]
    expected_output = 3
    assert count_samepair(list1, list2, list3) == expected_output

def test_no_identical_elements_any_position():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    expected_output = 0
    assert count_samepair(list1, list2, list3) == expected_output

def test_some_positions_identical_others_not():
    list1 = [1, 2, 3, 4]
    list2 = [1, 0, 3, 5]
    list3 = [1, 2, 3, 4]
    expected_output = 2
    assert count_samepair(list1, list2, list3) == expected_output

def test_different_data_types_matching_values_some_positions():
    list1 = ['a', 'b', 'c']
    list2 = ['a', 'x', 'c']
    list3 = ['a', 'b', 'c']
    expected_output = 2
    assert count_samepair(list1, list2, list3) == expected_output

def test_empty_lists():
    list1 = []
    list2 = []
    list3 = []
    expected_output = 0
    assert count_samepair(list1, list2, list3) == expected_output

def test_lists_different_lengths_count_up_to_shortest():
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 0]
    list3 = [1, 2, 3]
    expected_output = 2
    assert count_samepair(list1, list2, list3) == expected_output