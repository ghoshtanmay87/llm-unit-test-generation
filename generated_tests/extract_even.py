def even_ele(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def extract_even(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 == 0)
  return (res)

import pytest

def test_extract_even_flat_tuple():
    # Extract even numbers from a flat tuple of integers
    test_tuple = (1, 2, 3, 4, 5, 6)
    expected_output = (2, 4, 6)
    assert extract_even(test_tuple) == expected_output

def test_extract_even_one_level_nested_tuple():
    # Extract even numbers from a nested tuple with one level of nesting
    test_tuple = (1, (2, 3), 4)
    expected_output = ((2,), 4)
    assert extract_even(test_tuple) == expected_output

def test_extract_even_deeply_nested_tuple():
    # Extract even numbers from a deeply nested tuple
    test_tuple = (1, (2, (3, 4), 5), 6)
    expected_output = ((2, ((4,),)), 6)
    assert extract_even(test_tuple) == expected_output

def test_extract_even_no_even_numbers():
    # Extract even numbers from a tuple with no even numbers
    test_tuple = (1, 3, 5, (7, 9))
    expected_output = ()
    assert extract_even(test_tuple) == expected_output

def test_extract_even_empty_tuple():
    # Extract even numbers from an empty tuple
    test_tuple = ()
    expected_output = ()
    assert extract_even(test_tuple) == expected_output