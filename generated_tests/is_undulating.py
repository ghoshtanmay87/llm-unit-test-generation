def is_undulating(n): 
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True

import pytest

def test_input_list_length_less_than_or_equal_to_2_returns_false_single_element():
    # Input list with length less than or equal to 2 returns False
    n = [1]
    expected = False
    assert is_undulating(n) == expected

def test_input_list_length_less_than_or_equal_to_2_returns_false_two_elements():
    # Input list with length exactly 2 returns False
    n = [1, 2]
    expected = False
    assert is_undulating(n) == expected

def test_list_length_greater_than_2_alternating_pattern_returns_true():
    # List with length greater than 2 and alternating pattern returns True
    n = [1, 2, 1, 2, 1, 2]
    expected = True
    assert is_undulating(n) == expected

def test_list_length_greater_than_2_no_alternating_pattern_returns_false():
    # List with length greater than 2 but no alternating pattern returns False
    n = [1, 2, 3, 2, 1]
    expected = False
    assert is_undulating(n) == expected

def test_list_length_greater_than_2_all_elements_equal_returns_true():
    # List with length greater than 2 and all elements equal returns True
    n = [5, 5, 5, 5, 5]
    expected = True
    assert is_undulating(n) == expected

def test_list_length_greater_than_2_pattern_breaks_at_last_element_returns_false():
    # List with length greater than 2 and pattern breaks at last element returns False
    n = [1, 2, 1, 2, 3]
    expected = False
    assert is_undulating(n) == expected

def test_list_length_3_valid_undulating_pattern_returns_true():
    # List with length 3 and valid undulating pattern returns True
    n = [7, 8, 7]
    expected = True
    assert is_undulating(n) == expected

def test_list_length_3_invalid_undulating_pattern_returns_false():
    # List with length 3 and invalid undulating pattern returns False
    n = [7, 8, 9]
    expected = False
    assert is_undulating(n) == expected