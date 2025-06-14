def max_run_uppercase(test_str):
  cnt = 0
  res = 0
  for idx in range(0, len(test_str)):
    if test_str[idx].isupper():
      cnt += 1
    else:
      res = cnt
      cnt = 0
  if test_str[len(test_str) - 1].isupper():
    res = cnt
  return (res)

import pytest

def test_empty_string_input():
    # The input string is empty, so there are no uppercase letters and no runs.
    assert max_run_uppercase('') == 0

def test_string_with_no_uppercase_letters():
    # No characters are uppercase, so the count never increments.
    assert max_run_uppercase('abcdefg') == 0

def test_string_with_single_uppercase_letter():
    # One uppercase letter 'B' at index 1, counted as a run of length 1.
    assert max_run_uppercase('aBcdefg') == 1

def test_string_with_multiple_uppercase_runs_last_run_longest():
    # Runs: 'BB' (2), 'DDDD' (4). Returns length of last run 4.
    assert max_run_uppercase('aaBBccDDDD') == 4

def test_string_with_multiple_uppercase_runs_last_run_shorter():
    # Runs: 'AA' (2), 'BB' (2). Returns 2.
    assert max_run_uppercase('AAaaBB') == 2

def test_string_with_uppercase_run_in_middle():
    # Uppercase run 'DEF' length 3 in the middle. Returns 3.
    assert max_run_uppercase('abcDEFghi') == 3

def test_string_with_uppercase_run_at_start():
    # Uppercase run 'XYZ' length 3 at start. Returns 3.
    assert max_run_uppercase('XYZabc') == 3

def test_string_with_uppercase_run_at_end():
    # Uppercase run 'XYZ' length 3 at end. Returns 3.
    assert max_run_uppercase('abcXYZ') == 3

def test_string_with_alternating_uppercase_and_lowercase_letters():
    # Uppercase letters appear singly separated by lowercase letters. Each run length 1.
    assert max_run_uppercase('aAaAaA') == 1

def test_string_with_all_uppercase_letters():
    # All letters uppercase, run length is entire string length 7.
    assert max_run_uppercase('ABCDEFG') == 7