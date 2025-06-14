def find_longest_conseq_subseq(arr, n): 
	ans = 0
	count = 0
	arr.sort() 
	v = [] 
	v.append(arr[0]) 
	for i in range(1, n): 
		if (arr[i] != arr[i - 1]): 
			v.append(arr[i]) 
	for i in range(len(v)): 
		if (i > 0 and v[i] == v[i - 1] + 1): 
			count += 1
		else: 
			count = 1
		ans = max(ans, count) 
	return ans

import pytest

def test_longest_conseq_subseq_with_duplicates_and_consecutive_numbers():
    arr = [1, 2, 2, 3, 4, 5]
    n = 6
    expected_output = 5
    assert find_longest_conseq_subseq(arr, n) == expected_output

def test_longest_conseq_subseq_with_no_consecutive_numbers():
    arr = [10, 20, 30, 40]
    n = 4
    expected_output = 1
    assert find_longest_conseq_subseq(arr, n) == expected_output

def test_longest_conseq_subseq_with_negative_and_positive_numbers():
    arr = [-2, -1, 0, 1, 2, 4, 5]
    n = 7
    expected_output = 5
    assert find_longest_conseq_subseq(arr, n) == expected_output

def test_longest_conseq_subseq_with_all_elements_same():
    arr = [7, 7, 7, 7]
    n = 4
    expected_output = 1
    assert find_longest_conseq_subseq(arr, n) == expected_output

def test_longest_conseq_subseq_with_empty_list():
    arr = []
    n = 0
    expected_output = 0
    assert find_longest_conseq_subseq(arr, n) == expected_output

def test_longest_conseq_subseq_with_multiple_consecutive_subsequences():
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = 7
    expected_output = 4
    assert find_longest_conseq_subseq(arr, n) == expected_output