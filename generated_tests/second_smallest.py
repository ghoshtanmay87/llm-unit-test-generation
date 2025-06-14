def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]

import pytest

def test_second_smallest_distinct_elements_ascending():
    # List with distinct elements in ascending order
    numbers = [1, 2, 3, 4, 5]
    expected = 2
    assert second_smallest(numbers) == expected

def test_second_smallest_two_identical_elements():
    # List with two identical elements
    numbers = [7, 7]
    expected = None
    assert second_smallest(numbers) is expected

def test_second_smallest_two_distinct_elements():
    # List with two distinct elements
    numbers = [10, 5]
    expected = 10
    assert second_smallest(numbers) == expected

def test_second_smallest_duplicates_multiple_elements():
    # List with duplicates and multiple elements
    numbers = [4, 2, 2, 3, 1, 4]
    expected = 2
    assert second_smallest(numbers) == expected

def test_second_smallest_all_identical_elements():
    # List with all identical elements
    numbers = [9, 9, 9, 9]
    expected = None
    assert second_smallest(numbers) is expected

def test_second_smallest_one_element():
    # List with one element
    numbers = [42]
    expected = None
    assert second_smallest(numbers) is expected

def test_second_smallest_negative_and_positive_numbers():
    # List with negative and positive numbers
    numbers = [-1, -3, 0, 2, -3]
    expected = -1
    assert second_smallest(numbers) == expected