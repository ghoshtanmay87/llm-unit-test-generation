from copy import deepcopy
def colon_tuplex(tuplex,m,n):
  tuplex_colon = deepcopy(tuplex)
  tuplex_colon[m].append(n)
  return tuplex_colon

import pytest

def test_append_integer_to_inner_list():
    tuplex = [[1, 2], [3, 4]]
    m = 0
    n = 5
    expected_output = [[1, 2, 5], [3, 4]]
    assert colon_tuplex(tuplex, m, n) == expected_output

def test_append_string_to_inner_list():
    tuplex = [['a', 'b'], ['c']]
    m = 1
    n = 'd'
    expected_output = [['a', 'b'], ['c', 'd']]
    assert colon_tuplex(tuplex, m, n) == expected_output

def test_append_float_to_inner_list():
    tuplex = [[1.1, 2.2], [3.3]]
    m = 1
    n = 4.4
    expected_output = [[1.1, 2.2], [3.3, 4.4]]
    assert colon_tuplex(tuplex, m, n) == expected_output

def test_append_list_to_inner_list():
    tuplex = [[1, 2], [3, 4]]
    m = 1
    n = [5, 6]
    expected_output = [[1, 2], [3, 4, [5, 6]]]
    assert colon_tuplex(tuplex, m, n) == expected_output

def test_append_to_empty_inner_list():
    tuplex = [[], [1, 2]]
    m = 0
    n = 10
    expected_output = [[10], [1, 2]]
    assert colon_tuplex(tuplex, m, n) == expected_output