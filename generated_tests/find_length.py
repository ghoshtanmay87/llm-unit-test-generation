def find_length(string, n): 
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0

import pytest

def test_all_zeros_in_string():
    # Each '0' adds +1 to current_sum, so current_sum increments to 4 without resetting. max_sum becomes 4.
    assert find_length('0000', 4) == 4

def test_all_ones_in_string():
    # Each '1' subtracts 1, causing current_sum to drop below 0 and reset to 0 each time. max_sum remains 0.
    assert find_length('1111', 4) == 0

def test_alternating_zeros_ones_starting_with_zero():
    # At each '0', current_sum increases by 1; at each '1', it decreases by 1 and resets if negative. max_sum reaches 1 but never more.
    assert find_length('0101', 4) == 1

def test_alternating_zeros_ones_starting_with_one():
    # First character '1' causes current_sum to reset to 0. Subsequent '0's increase current_sum to 1, max_sum is 1.
    assert find_length('1010', 4) == 1

def test_mixed_string_more_zeros_than_ones():
    # The longest positive sum segment is two consecutive zeros before current_sum resets due to ones.
    assert find_length('001100', 6) == 2

def test_mixed_string_equal_zeros_ones():
    # current_sum fluctuates but never exceeds 1 before resetting; max_sum is 1.
    assert find_length('010110', 6) == 1

def test_empty_string_input():
    # No characters to process, so max_sum remains 0.
    assert find_length('', 0) == 0

def test_single_zero_character():
    # Single '0' adds 1 to current_sum, max_sum becomes 1.
    assert find_length('0', 1) == 1

def test_single_one_character():
    # '1' subtracts 1 causing current_sum to reset to 0, max_sum remains 0.
    assert find_length('1', 1) == 0

def test_long_string_zeros_followed_by_ones():
    # First four zeros increase current_sum to 4, then ones cause resets but max_sum remains 4.
    assert find_length('00001111', 8) == 4