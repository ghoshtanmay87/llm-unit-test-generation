def extract_missing(test_list, strt_val, stop_val):
  res = []
  for sub in test_list:
    if sub[0] > strt_val:
      res.append((strt_val, sub[0]))
      strt_val = sub[1]
    if strt_val < stop_val:
      res.append((strt_val, stop_val))
  return (res)

import pytest

def test_empty_test_list_start_less_than_stop():
    # Scenario: Empty test_list with start less than stop
    test_list = []
    strt_val = 1
    stop_val = 5
    expected_output = [(1, 5)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output

def test_one_sub_interval_start_less_than_sub0():
    # Scenario: One sub-interval with start less than sub[0]
    test_list = [(3, 4)]
    strt_val = 1
    stop_val = 5
    expected_output = [(1, 3), (4, 5)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output

def test_one_sub_interval_start_equal_sub0():
    # Scenario: One sub-interval with start equal to sub[0]
    test_list = [(1, 3)]
    strt_val = 1
    stop_val = 5
    expected_output = [(1, 5)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output

def test_multiple_sub_intervals_with_gaps_corrected_reasoning():
    # Scenario: Multiple sub-intervals with gaps (corrected reasoning)
    test_list = [(2, 3), (5, 6)]
    strt_val = 1
    stop_val = 7
    expected_output = [(1, 2), (3, 7), (3, 5), (6, 7)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output

def test_sub_intervals_no_gaps_start_equals_strt_val():
    # Scenario: Sub-intervals with no gaps and start equals strt_val
    test_list = [(1, 2), (2, 3)]
    strt_val = 1
    stop_val = 3
    expected_output = [(1, 3), (1, 2)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output

def test_sub_intervals_start_greater_than_stop_val():
    # Scenario: Sub-intervals with start greater than stop_val
    test_list = [(10, 12)]
    strt_val = 1
    stop_val = 5
    expected_output = [(1, 10)]
    assert extract_missing(test_list, strt_val, stop_val) == expected_output