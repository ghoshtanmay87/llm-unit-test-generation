def zip_tuples(test_tup1, test_tup2):
  res = []
  for i, j in enumerate(test_tup1):
    res.append((j, test_tup2[i % len(test_tup2)])) 
  return (res)

import pytest

def test_zip_tuples_equal_length():
    # Zipping two tuples of equal length
    test_tup1 = (1, 2, 3)
    test_tup2 = ('a', 'b', 'c')
    expected_output = [(1, 'a'), (2, 'b'), (3, 'c')]
    assert zip_tuples(test_tup1, test_tup2) == expected_output

def test_zip_tuples_longer_first_shorter_second():
    # Zipping a longer first tuple with a shorter second tuple
    test_tup1 = (10, 20, 30, 40)
    test_tup2 = ('x', 'y')
    expected_output = [(10, 'x'), (20, 'y'), (30, 'x'), (40, 'y')]
    assert zip_tuples(test_tup1, test_tup2) == expected_output

def test_zip_tuples_shorter_first_longer_second():
    # Zipping a shorter first tuple with a longer second tuple
    test_tup1 = (5, 6)
    test_tup2 = ('p', 'q', 'r', 's')
    expected_output = [(5, 'p'), (6, 'q')]
    assert zip_tuples(test_tup1, test_tup2) == expected_output

def test_zip_tuples_empty_second_tuple_raises_error():
    # Zipping with an empty second tuple should raise an error due to modulo by zero
    test_tup1 = (1, 2, 3)
    test_tup2 = ()
    with pytest.raises(ZeroDivisionError):
        zip_tuples(test_tup1, test_tup2)

def test_zip_tuples_empty_first_tuple_returns_empty_list():
    # Zipping with an empty first tuple returns an empty list
    test_tup1 = ()
    test_tup2 = ('a', 'b')
    expected_output = []
    assert zip_tuples(test_tup1, test_tup2) == expected_output

def test_zip_tuples_mixed_data_types():
    # Zipping tuples with mixed data types
    test_tup1 = (True, None, 3.14)
    test_tup2 = ('yes', 0, [1, 2])
    expected_output = [(True, 'yes'), (None, 0), (3.14, [1, 2])]
    assert zip_tuples(test_tup1, test_tup2) == expected_output