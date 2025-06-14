def chunk_tuples(test_tup, N):
  res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]
  return (res)

import pytest

def test_chunk_tuple_of_integers_size_2():
    test_tup = (1, 2, 3, 4, 5, 6)
    N = 2
    expected_output = [(1, 2), (3, 4), (5, 6)]
    assert chunk_tuples(test_tup, N) == expected_output

def test_chunk_tuple_of_integers_size_3_with_leftover():
    test_tup = (10, 20, 30, 40, 50)
    N = 3
    expected_output = [(10, 20, 30), (40, 50)]
    assert chunk_tuples(test_tup, N) == expected_output

def test_chunk_tuple_of_strings_size_1():
    test_tup = ('a', 'b', 'c')
    N = 1
    expected_output = [('a',), ('b',), ('c',)]
    assert chunk_tuples(test_tup, N) == expected_output

def test_chunk_empty_tuple_any_size():
    test_tup = ()
    N = 4
    expected_output = []
    assert chunk_tuples(test_tup, N) == expected_output

def test_chunk_tuple_with_chunk_size_larger_than_length():
    test_tup = (7, 8, 9)
    N = 10
    expected_output = [(7, 8, 9)]
    assert chunk_tuples(test_tup, N) == expected_output