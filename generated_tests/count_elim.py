def count_elim(num):
  count_elim = 0
  for n in num:
    if isinstance(n, tuple):
        break
    count_elim += 1
  return count_elim

import pytest

def test_count_elim_no_tuples_all_integers():
    # List with no tuples, all elements are integers
    input_data = [1, 2, 3, 4, 5]
    expected = 5
    assert count_elim(input_data) == expected

def test_count_elim_tuple_at_start():
    # List with a tuple at the start
    input_data = [(1, 2), 3, 4]
    expected = 0
    assert count_elim(input_data) == expected

def test_count_elim_tuple_in_middle():
    # List with a tuple in the middle
    input_data = [1, 2, (3, 4), 5]
    expected = 2
    assert count_elim(input_data) == expected

def test_count_elim_tuple_at_end():
    # List with a tuple at the end
    input_data = [1, 2, 3, (4, 5)]
    expected = 3
    assert count_elim(input_data) == expected

def test_count_elim_empty_list():
    # Empty list input
    input_data = []
    expected = 0
    assert count_elim(input_data) == expected

def test_count_elim_multiple_tuples_first_in_middle():
    # List with multiple tuples, first tuple in the middle
    input_data = [1, (2, 3), (4, 5), 6]
    expected = 1
    assert count_elim(input_data) == expected

def test_count_elim_non_tuple_iterables():
    # List with non-tuple iterable elements
    input_data = [1, [2, 3], 4, (5, 6)]
    expected = 3
    assert count_elim(input_data) == expected