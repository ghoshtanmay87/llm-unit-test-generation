from collections import defaultdict 
def freq_element(test_tup):
  res = defaultdict(int)
  for ele in test_tup:
    res[ele] += 1
  return (str(dict(res)))

import pytest

def test_freq_element_distinct_integers():
    test_tup = (1, 2, 3, 4)
    expected_output = '{1: 1, 2: 1, 3: 1, 4: 1}'
    assert freq_element(test_tup) == expected_output

def test_freq_element_repeated_integers():
    test_tup = (1, 2, 2, 3, 3, 3)
    expected_output = '{1: 1, 2: 2, 3: 3}'
    assert freq_element(test_tup) == expected_output

def test_freq_element_strings():
    test_tup = ('a', 'b', 'a', 'c', 'b', 'a')
    expected_output = "{'a': 3, 'b': 2, 'c': 1}"
    assert freq_element(test_tup) == expected_output

def test_freq_element_empty_tuple():
    test_tup = ()
    expected_output = '{}'
    assert freq_element(test_tup) == expected_output

def test_freq_element_mixed_types():
    test_tup = (1, '1', 1, '1', 2)
    expected_output = "{1: 2, '1': 2, 2: 1}"
    assert freq_element(test_tup) == expected_output