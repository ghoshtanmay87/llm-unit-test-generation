def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

import pytest

def test_count_all_elements_within_range():
    # All elements 1, 2, 3, 4, 5 are between 1 and 5 inclusive, so count is 5.
    result = count_range_in_list([1, 2, 3, 4, 5], 1, 5)
    assert result == 5

def test_count_some_elements_within_range():
    # Only elements 4 and 6 are between 3 and 7 inclusive, so count is 2.
    result = count_range_in_list([0, 2, 4, 6, 8], 3, 7)
    assert result == 2

def test_count_no_elements_within_range():
    # No elements are between 1 and 5 inclusive, so count is 0.
    result = count_range_in_list([10, 20, 30], 1, 5)
    assert result == 0

def test_count_empty_list():
    # Empty list means no elements to count, so result is 0.
    result = count_range_in_list([], 0, 10)
    assert result == 0

def test_count_min_equals_max():
    # Only element equal to 3 is counted, so count is 1.
    result = count_range_in_list([1, 2, 3, 4, 5], 3, 3)
    assert result == 1

def test_count_all_elements_less_than_min():
    # All elements are less than min=0, so none are counted.
    result = count_range_in_list([-5, -4, -3], 0, 10)
    assert result == 0

def test_count_all_elements_greater_than_max():
    # All elements are greater than max=10, so none are counted.
    result = count_range_in_list([11, 12, 13], 0, 10)
    assert result == 0

def test_count_with_negative_range_values():
    # Elements -5, 0, and 5 are within the range -5 to 5 inclusive.
    result = count_range_in_list([-10, -5, 0, 5, 10], -5, 5)
    assert result == 3