def remove_replica(test_tup):
  temp = set()
  res = tuple(ele if ele not in temp and not temp.add(ele) 
				else 'MSP' for ele in test_tup)
  return (res)

import pytest

def test_remove_duplicates_from_tuple_of_integers():
    test_tup = (1, 2, 2, 3, 1)
    expected_output = (1, 2, 'MSP', 3, 'MSP')
    assert remove_replica(test_tup) == expected_output

def test_tuple_with_all_unique_elements():
    test_tup = (4, 5, 6)
    expected_output = (4, 5, 6)
    assert remove_replica(test_tup) == expected_output

def test_tuple_with_all_identical_elements():
    test_tup = (7, 7, 7, 7)
    expected_output = (7, 'MSP', 'MSP', 'MSP')
    assert remove_replica(test_tup) == expected_output

def test_empty_tuple_input():
    test_tup = ()
    expected_output = ()
    assert remove_replica(test_tup) == expected_output

def test_tuple_with_mixed_data_types_and_duplicates():
    test_tup = (1, 'a', 1, 'b', 'a')
    expected_output = (1, 'a', 'MSP', 'b', 'MSP')
    assert remove_replica(test_tup) == expected_output