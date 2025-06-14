import sys 
def find_max_val(n, x, y): 
	ans = -sys.maxsize 
	for k in range(n + 1): 
		if (k % x == y): 
			ans = max(ans, k) 
	return (ans if (ans >= 0 and
					ans <= n) else -1)

import pytest

def test_find_max_val_multiple_valid_k_values():
    # Find max k in range 0 to n where k mod x equals y, with multiple valid k values
    n = 10
    x = 3
    y = 1
    expected = 10
    assert find_max_val(n, x, y) == expected

def test_find_max_val_no_valid_k_due_to_remainder_out_of_range():
    # No k in range 0 to n satisfies k mod x equals y
    n = 5
    x = 2
    y = 2
    expected = -1
    assert find_max_val(n, x, y) == expected

def test_find_max_val_only_zero_satisfies_when_y_zero():
    # Only k=0 satisfies k mod x equals y when y=0
    n = 0
    x = 1
    y = 0
    expected = 0
    assert find_max_val(n, x, y) == expected

def test_find_max_val_multiple_k_max_less_than_n():
    # Multiple k satisfy condition, max k is less than n
    n = 15
    x = 4
    y = 3
    expected = 11
    assert find_max_val(n, x, y) == expected

def test_find_max_val_y_zero_large_n():
    # Check when y is zero and n is large
    n = 20
    x = 5
    y = 0
    expected = 20
    assert find_max_val(n, x, y) == expected

def test_find_max_val_y_greater_than_x_no_valid_k():
    # y greater than x, no valid k
    n = 10
    x = 4
    y = 5
    expected = -1
    assert find_max_val(n, x, y) == expected

def test_find_max_val_single_valid_k_at_start():
    # Single valid k at the start of range
    n = 3
    x = 5
    y = 3
    expected = 3
    assert find_max_val(n, x, y) == expected

def test_find_max_val_negative_y_no_valid_k():
    # No valid k because y negative
    n = 10
    x = 3
    y = -1
    expected = -1
    assert find_max_val(n, x, y) == expected