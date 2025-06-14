def below_threshold(l: list, t: int):
    for e in l:
        if e >= t:
            return False
    return True

import pytest

def test_all_elements_less_than_threshold():
    # All elements (1, 2, 3) are less than 5, so the function returns True.
    assert below_threshold([1, 2, 3], 5) is True

def test_one_element_equals_threshold():
    # The element 5 is equal to the threshold 5, so the function returns False.
    assert below_threshold([1, 5, 3], 5) is False

def test_one_element_greater_than_threshold():
    # The element 6 is greater than the threshold 5, so the function returns False.
    assert below_threshold([1, 6, 3], 5) is False

def test_empty_list_input():
    # No elements to compare, so none are >= threshold; function returns True.
    assert below_threshold([], 5) is True

def test_all_elements_zero_threshold_positive():
    # All elements (0) are less than threshold 1, so function returns True.
    assert below_threshold([0, 0, 0], 1) is True

def test_negative_elements_positive_threshold():
    # All elements are less than 0, so function returns True.
    assert below_threshold([-3, -2, -1], 0) is True

def test_negative_elements_negative_threshold():
    # Element -1 is greater than threshold -2, so function returns False.
    assert below_threshold([-3, -2, -1], -2) is False