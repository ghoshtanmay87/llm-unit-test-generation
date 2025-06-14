def flatten(test_tuple): 
	for tup in test_tuple: 
		if isinstance(tup, tuple): 
			yield from flatten(tup) 
		else: 
			yield tup 
def count_element_freq(test_tuple):
  res = {}
  for ele in flatten(test_tuple):
    if ele not in res:
      res[ele] = 0
    res[ele] += 1
  return (res)

import pytest

def test_count_frequencies_flat_tuple_of_integers():
    test_tuple = (1, 2, 2, 3)
    expected_output = {1: 1, 2: 2, 3: 1}
    assert count_element_freq(test_tuple) == expected_output

def test_count_frequencies_nested_tuple_of_integers():
    test_tuple = (1, (2, 2), 3)
    expected_output = {1: 1, 2: 2, 3: 1}
    assert count_element_freq(test_tuple) == expected_output

def test_count_frequencies_deeply_nested_tuple_with_mixed_types():
    test_tuple = (1, (2, (3, 3), 2), 1)
    expected_output = {1: 2, 2: 2, 3: 2}
    assert count_element_freq(test_tuple) == expected_output

def test_count_frequencies_empty_tuple():
    test_tuple = ()
    expected_output = {}
    assert count_element_freq(test_tuple) == expected_output

def test_count_frequencies_tuple_with_different_data_types():
    test_tuple = (1, (2, 'a', (3, 'a')), 1)
    expected_output = {1: 2, 2: 1, 'a': 2, 3: 1}
    assert count_element_freq(test_tuple) == expected_output