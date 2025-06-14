def parallel_lines(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]

import pytest

def test_parallel_lines_same_positive_slope():
    # Both lines have the same slope, positive values
    line1 = [2, 4]
    line2 = [3, 6]
    expected = True
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_different_positive_slopes():
    # Lines have different slopes, positive values
    line1 = [1, 2]
    line2 = [3, 5]
    expected = False
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_same_negative_slope():
    # Both lines have the same slope, negative values
    line1 = [-4, 2]
    line2 = [-6, 3]
    expected = True
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_zero_and_nonzero_slope():
    # One line has zero slope, the other does not
    line1 = [0, 5]
    line2 = [1, 2]
    expected = False
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_both_zero_slope():
    # Both lines have zero slope
    line1 = [0, 3]
    line2 = [0, 7]
    expected = True
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_equal_fractional_slopes():
    # Lines with fractional slopes that are equal
    line1 = [5, 10]
    line2 = [15, 30]
    expected = True
    assert parallel_lines(line1, line2) == expected

def test_parallel_lines_unequal_fractional_slopes():
    # Lines with fractional slopes that are not equal
    line1 = [7, 14]
    line2 = [10, 21]
    expected = False
    assert parallel_lines(line1, line2) == expected