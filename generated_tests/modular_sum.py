def modular_sum(arr, n, m): 
	if (n > m): 
		return True
	DP = [False for i in range(m)] 
	for i in range(n): 
		if (DP[0]): 
			return True
		temp = [False for i in range(m)] 
		for j in range(m): 
			if (DP[j] == True): 
				if (DP[(j + arr[i]) % m] == False): 
					temp[(j + arr[i]) % m] = True
		for j in range(m): 
			if (temp[j]): 
				DP[j] = True
		DP[arr[i] % m] = True
	return DP[0]

import pytest

def test_sum_of_elements_modulo_m_equals_zero_with_small_array():
    arr = [1, 2, 3]
    n = 3
    m = 3
    expected = True
    assert modular_sum(arr, n, m) == expected

def test_n_greater_than_m_returns_true_immediately():
    arr = [1, 2, 3, 4]
    n = 4
    m = 3
    expected = True
    assert modular_sum(arr, n, m) == expected

def test_no_subset_sums_to_multiple_of_m():
    arr = [1, 1, 1]
    n = 3
    m = 5
    expected = False
    assert modular_sum(arr, n, m) == expected

def test_single_element_equal_to_multiple_of_m():
    arr = [6]
    n = 1
    m = 3
    expected = True
    assert modular_sum(arr, n, m) == expected

def test_empty_array_with_n_zero_returns_false():
    arr = []
    n = 0
    m = 1
    expected = False
    assert modular_sum(arr, n, m) == expected

def test_array_with_elements_all_multiples_of_m():
    arr = [4, 8, 12]
    n = 3
    m = 4
    expected = True
    assert modular_sum(arr, n, m) == expected

def test_array_with_no_subset_sum_modulo_m_equals_zero_but_n_less_than_m():
    arr = [2, 4, 6]
    n = 3
    m = 7
    expected = False
    assert modular_sum(arr, n, m) == expected