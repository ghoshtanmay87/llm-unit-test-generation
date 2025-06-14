def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans

import pytest

def test_multiple_numbers_some_frequencies_meet_or_exceed_values():
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    expected_output = 4
    assert search(lst) == expected_output

def test_all_elements_same_frequency_less_than_element_value():
    lst = [5, 5, 5]
    expected_output = -1
    assert search(lst) == expected_output

def test_frequency_equals_element_value_for_smaller_number():
    lst = [1, 1, 2, 2, 2]
    expected_output = 2
    assert search(lst) == expected_output

def test_single_element_repeated_once():
    lst = [1]
    expected_output = 1
    assert search(lst) == expected_output

def test_list_with_zero_included_should_be_ignored():
    lst = [0, 0, 1, 1, 1]
    expected_output = 1
    assert search(lst) == expected_output

def test_large_numbers_low_frequencies():
    lst = [10, 10, 10, 1]
    expected_output = 1
    assert search(lst) == expected_output

def test_no_frequency_meets_or_exceeds_element_value():
    lst = [2, 3, 3]
    expected_output = -1
    assert search(lst) == expected_output