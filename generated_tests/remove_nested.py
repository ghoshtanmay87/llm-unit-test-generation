def remove_nested(test_tup):
  res = tuple()
  for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
      res = res + (ele, )
  return (res)

import pytest

def test_remove_nested_with_only_non_tuple_elements():
    # Input tuple with only non-tuple elements
    test_tup = (1, 2, 3)
    expected_output = (1, 2, 3)
    assert remove_nested(test_tup) == expected_output

def test_remove_nested_with_some_nested_tuples():
    # Input tuple with some nested tuples
    test_tup = (1, (2, 3), 4)
    expected_output = (1, 4)
    assert remove_nested(test_tup) == expected_output

def test_remove_nested_with_all_elements_as_tuples():
    # Input tuple with all elements as tuples
    test_tup = ((1,), (2, 3))
    expected_output = ()
    assert remove_nested(test_tup) == expected_output

def test_remove_nested_with_mixed_types_including_nested_tuples():
    # Input tuple with mixed types including nested tuples
    test_tup = (1, 'a', (2, 3), 4.5, ())
    expected_output = (1, 'a', 4.5)
    assert remove_nested(test_tup) == expected_output

def test_remove_nested_with_empty_input_tuple():
    # Empty input tuple
    test_tup = ()
    expected_output = ()
    assert remove_nested(test_tup) == expected_output