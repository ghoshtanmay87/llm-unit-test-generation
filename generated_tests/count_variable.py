from collections import Counter
def count_variable(a,b,c,d):
  c = Counter(p=a, q=b, r=c, s=d)
  return list(c.elements())

import pytest

def test_all_inputs_distinct_strings():
    # All inputs are distinct strings
    result = count_variable(a='apple', b='banana', c='cherry', d='date')
    expected = ['apple', 'banana', 'cherry', 'date']
    assert sorted(result) == sorted(expected)

def test_some_inputs_repeated_strings():
    # Some inputs are repeated strings
    result = count_variable(a='apple', b='banana', c='apple', d='banana')
    expected = ['apple', 'apple', 'banana', 'banana']
    assert sorted(result) == sorted(expected)

def test_all_inputs_same_string():
    # All inputs are the same string
    result = count_variable(a='kiwi', b='kiwi', c='kiwi', d='kiwi')
    expected = ['kiwi', 'kiwi', 'kiwi', 'kiwi']
    assert sorted(result) == sorted(expected)

def test_inputs_are_integers_with_duplicates():
    # Inputs are integers with some duplicates
    result = count_variable(a=1, b=2, c=1, d=3)
    expected = [1, 1, 2, 3]
    assert sorted(result) == sorted(expected)

def test_inputs_mixed_types_string_and_integer():
    # Inputs are mixed types (string and integer)
    result = count_variable(a='1', b=1, c='1', d=2)
    expected = ['1', '1', 1, 2]
    assert sorted(result) == sorted(expected)