def Seq_Linear(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: 
    return "Linear Sequence"
  else:
    return "Non Linear Sequence"

import pytest

def test_detects_strictly_increasing_linear_sequence():
    input_seq = [2, 4, 6, 8, 10]
    expected = "Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_strictly_decreasing_linear_sequence():
    input_seq = [10, 7, 4, 1, -2]
    expected = "Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_non_linear_sequence_with_varying_differences():
    input_seq = [1, 3, 6, 10, 15]
    expected = "Non Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_constant_sequence_as_linear():
    input_seq = [5, 5, 5, 5]
    expected = "Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_sequence_with_one_element_as_linear():
    input_seq = [42]
    expected = "Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_sequence_with_two_elements_as_linear():
    input_seq = [3, 8]
    expected = "Linear Sequence"
    assert Seq_Linear(input_seq) == expected

def test_detects_sequence_with_zero_difference_followed_by_non_zero_difference_as_non_linear():
    input_seq = [7, 7, 10]
    expected = "Non Linear Sequence"
    assert Seq_Linear(input_seq) == expected