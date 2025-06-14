def common_prefix_util(str1, str2): 
	result = ""; 
	n1 = len(str1) 
	n2 = len(str2) 
	i = 0
	j = 0
	while i <= n1 - 1 and j <= n2 - 1: 
		if (str1[i] != str2[j]): 
			break
		result += str1[i] 
		i += 1
		j += 1
	return (result) 
def common_prefix (arr, n): 
	prefix = arr[0] 
	for i in range (1, n): 
		prefix = common_prefix_util(prefix, arr[i]) 
	return (prefix)

import pytest

def test_common_prefix_all_strings_have_common_prefix_fl():
    arr = ['flower', 'flow', 'flight']
    n = 3
    expected_output = 'fl'
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_all_strings_are_identical():
    arr = ['test', 'test', 'test']
    n = 3
    expected_output = 'test'
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_no_common_prefix_among_strings():
    arr = ['dog', 'racecar', 'car']
    n = 3
    expected_output = ''
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_single_string_in_array():
    arr = ['single']
    n = 1
    expected_output = 'single'
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_common_prefix_is_single_character():
    arr = ['cir', 'car', 'cat']
    n = 3
    expected_output = 'c'
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_empty_string_in_array():
    arr = ['', 'abc', 'ab']
    n = 3
    expected_output = ''
    assert common_prefix(arr, n) == expected_output

def test_common_prefix_common_prefix_is_entire_shortest_string():
    arr = ['interview', 'inter', 'internet']
    n = 3
    expected_output = 'inter'
    assert common_prefix(arr, n) == expected_output