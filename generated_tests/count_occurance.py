def count_occurance(s):
  count=0
  for i in range(len(s)):
    if (s[i]== 's' and s[i+1]=='t' and s[i+2]== 'd'):
      count = count + 1
  return count

import pytest

def test_count_occurance_one_occurrence():
    # Count occurrences of 'std' in a string with one occurrence
    s = 'this is a std test'
    expected = 1
    assert count_occurance(s) == expected

def test_count_occurance_multiple_occurrences():
    # Count occurrences of 'std' in a string with multiple occurrences
    s = 'stdstdstd'
    expected = 3
    assert count_occurance(s) == expected

def test_count_occurance_overlapping_substrings():
    # Count occurrences of 'std' in a string with overlapping substrings
    s = 'ststd'
    expected = 1
    assert count_occurance(s) == expected

def test_count_occurance_no_occurrences():
    # Count occurrences of 'std' in a string with no occurrences
    s = 'hello world'
    expected = 0
    assert count_occurance(s) == expected

def test_count_occurance_short_string():
    # Count occurrences of 'std' in a string shorter than 3 characters
    s = 'st'
    expected = 0
    assert count_occurance(s) == expected