def count_odd(array_nums):
   count_odd = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
   return count_odd

import pytest

def test_count_odd_mixed_even_and_odd():
    # The list contains three odd numbers: 1, 3, and 5.
    result = count_odd([1, 2, 3, 4, 5])
    assert result == 3

def test_count_odd_all_even():
    # All numbers are even, so the filter finds no odd numbers, resulting in a count of 0.
    result = count_odd([2, 4, 6, 8])
    assert result == 0

def test_count_odd_all_odd():
    # All numbers are odd, so the filter includes all elements, resulting in a count of 5.
    result = count_odd([1, 3, 5, 7, 9])
    assert result == 5

def test_count_odd_empty_list():
    # The list is empty, so there are no odd numbers to count, resulting in 0.
    result = count_odd([])
    assert result == 0

def test_count_odd_negative_and_positive():
    # Odd numbers are -3, -1, 1, and 3. The function counts these four odd numbers correctly.
    result = count_odd([-3, -2, -1, 0, 1, 2, 3])
    assert result == 4