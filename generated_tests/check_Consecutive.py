def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1))

import pytest

def test_list_with_consecutive_integers_in_order():
    # The list sorted is [1, 2, 3, 4, 5], which matches the range from min=1 to max=5 inclusive
    assert check_Consecutive([1, 2, 3, 4, 5]) is True

def test_list_with_consecutive_integers_out_of_order():
    # Sorting the list gives [1, 2, 3, 4, 5], which matches the range from min=1 to max=5 inclusive
    assert check_Consecutive([3, 1, 2, 5, 4]) is True

def test_list_with_missing_integer_in_sequence():
    # Sorting the list gives [1, 2, 4, 5], but the range from min=1 to max=5 inclusive is [1, 2, 3, 4, 5]
    assert check_Consecutive([1, 2, 4, 5]) is False

def test_list_with_duplicate_integers():
    # Sorting the list gives [1, 2, 2, 3], but the range from min=1 to max=3 inclusive is [1, 2, 3]
    assert check_Consecutive([1, 2, 2, 3]) is False

def test_single_element_list():
    # Sorting the list is [7], and the range from min=7 to max=7 inclusive is [7]
    assert check_Consecutive([7]) is True

def test_list_with_negative_consecutive_integers():
    # Sorting the list is [-3, -2, -1, 0], which matches the range from min=-3 to max=0 inclusive
    assert check_Consecutive([-3, -2, -1, 0]) is True

def test_list_with_negative_integers_missing_a_number():
    # Sorting the list is [-3, -1, 0], but the range from min=-3 to max=0 inclusive is [-3, -2, -1, 0]
    assert check_Consecutive([-3, -1, 0]) is False