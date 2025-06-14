def find_fixed_point(arr, n): 
	for i in range(n): 
		if arr[i] is i: 
			return i 
	return -1

import pytest

def test_fixed_point_with_element_equal_to_index_but_not_same_object():
    # The function uses 'is' which checks object identity, not equality.
    # Although arr[0] == 0, arr[0] is 0 is False because the int objects differ.
    arr = [0, 2, 3, 4, 5]
    n = 5
    expected = -1
    assert find_fixed_point(arr, n) == expected

def test_fixed_point_with_element_equal_to_index_but_different_object_identity():
    # Even though arr[2] == 2, 'is' checks identity, which fails here.
    arr = [1, 1, 2, 3, 4]
    n = 5
    expected = -1
    assert find_fixed_point(arr, n) == expected

def test_fixed_point_in_small_array_with_identical_integer_objects():
    # Small integers are cached by Python, so arr[0] is 0 is True.
    arr = [0, 1, 2]
    n = 3
    expected = 0
    assert find_fixed_point(arr, n) == expected

def test_fixed_point_in_array_with_repeated_small_integers():
    # At i=2, arr[2] is 2 is True due to small integer caching.
    arr = [1, 1, 2, 3]
    n = 4
    expected = 2
    assert find_fixed_point(arr, n) == expected

def test_no_fixed_point_when_elements_do_not_match_indices_by_identity():
    # No arr[i] is i condition is True, so returns -1.
    arr = [10, 20, 30, 40]
    n = 4
    expected = -1
    assert find_fixed_point(arr, n) == expected