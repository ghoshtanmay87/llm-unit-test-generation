def count_tuplex(tuplex,value):  
  count = tuplex.count(value)
  return count

import pytest

def test_count_occurrences_value_present_multiple_times():
    # The value 2 appears three times in the list [1, 2, 3, 2, 2, 4], so the count is 3.
    result = count_tuplex([1, 2, 3, 2, 2, 4], 2)
    assert result == 3

def test_count_occurrences_value_present_once():
    # The value 7 appears exactly once in the list [5, 6, 7, 8], so the count is 1.
    result = count_tuplex([5, 6, 7, 8], 7)
    assert result == 1

def test_count_occurrences_value_not_present():
    # The value 40 does not appear in the list [10, 20, 30], so the count is 0.
    result = count_tuplex([10, 20, 30], 40)
    assert result == 0

def test_count_occurrences_empty_list():
    # The list is empty, so no values are present, resulting in a count of 0.
    result = count_tuplex([], 1)
    assert result == 0

def test_count_occurrences_string_value_in_list_of_strings():
    # The string 'apple' appears twice in the list, so the count is 2.
    result = count_tuplex(['apple', 'banana', 'apple', 'cherry'], 'apple')
    assert result == 2