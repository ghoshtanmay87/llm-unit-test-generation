from collections import defaultdict 
def get_unique(test_list):
  res = defaultdict(list)
  for sub in test_list:
    res[sub[1]].append(sub[0])
  res = dict(res)
  res_dict = dict()
  for key in res:
    res_dict[key] = len(list(set(res[key])))
  return (str(res_dict))

import pytest

def test_unique_counts_multiple_pairs_repeated_first_elements():
    test_list = [[1, 'a'], [2, 'a'], [1, 'a'], [3, 'b'], [3, 'b'], [4, 'b']]
    expected_output = "{'a': 2, 'b': 2}"
    assert get_unique(test_list) == expected_output

def test_empty_input_list_returns_empty_dict_string():
    test_list = []
    expected_output = '{}'
    assert get_unique(test_list) == expected_output

def test_single_pair_input_returns_count_1_for_that_key():
    test_list = [[10, 'x']]
    expected_output = "{'x': 1}"
    assert get_unique(test_list) == expected_output

def test_multiple_keys_single_unique_first_elements():
    test_list = [[5, 'a'], [6, 'b'], [7, 'c']]
    expected_output = "{'a': 1, 'b': 1, 'c': 1}"
    assert get_unique(test_list) == expected_output

def test_multiple_keys_multiple_repeated_first_elements():
    test_list = [[1, 'a'], [1, 'a'], [2, 'a'], [2, 'b'], [2, 'b'], [3, 'b'], [3, 'b'], [3, 'b']]
    expected_output = "{'a': 2, 'b': 2}"
    assert get_unique(test_list) == expected_output