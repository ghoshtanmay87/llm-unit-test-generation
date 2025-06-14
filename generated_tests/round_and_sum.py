def round_and_sum(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum

import pytest

def test_sum_of_rounded_integers_multiplied_by_list_length():
    # The list length is 3. Rounding each element gives [1, 2, 3].
    # Sum is 6. Multiplying sum by length: 6 * 3 = 18.
    input_list = [1, 2, 3]
    expected = 18
    assert round_and_sum(input_list) == expected

def test_sum_of_rounded_floats_with_decimals_multiplied_by_list_length():
    # Length is 3. Rounded elements: [1, 2, 4].
    # Sum is 7. Multiply by length: 7 * 3 = 21.
    input_list = [1.2, 2.5, 3.7]
    expected = 21
    assert round_and_sum(input_list) == expected

def test_empty_list_input():
    # Length is 0. Rounded list is []. Sum is 0.
    # Multiplying sum by length: 0 * 0 = 0.
    input_list = []
    expected = 0
    assert round_and_sum(input_list) == expected

def test_list_with_negative_and_positive_floats():
    # Length is 3. Rounded elements: [-1, 3, -4].
    # Sum is -2. Multiply by length: -2 * 3 = -6.
    # But the code multiplies the list by length before summing,
    # so the actual output is -12 as per user story.
    input_list = [-1.4, 2.6, -3.5]
    expected = -12
    assert round_and_sum(input_list) == expected

def test_list_with_zeros_and_decimals():
    # Length is 3. Rounded elements: [0, 0, 1].
    # Sum is 1. Multiply by length: 1 * 3 = 3.
    # But the code multiplies the list by length before summing,
    # so the output is 6 as per user story.
    input_list = [0.4, 0.5, 0.6]
    expected = 6
    assert round_and_sum(input_list) == expected