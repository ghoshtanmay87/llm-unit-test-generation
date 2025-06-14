def check_permutation(str1, str2):
  n1=len(str1)
  n2=len(str2)
  if(n1!=n2):
    return False
  a=sorted(str1)
  str1=" ".join(a)
  b=sorted(str2)
  str2=" ".join(b)
  for i in range(0, n1, 1):
    if(str1[i] != str2[i]):
      return False
  return True

import pytest

def test_check_two_identical_strings():
    # Both strings have the same length and characters. After sorting, both become 'a b c'.
    # Comparing character by character, all match, so return True.
    assert check_permutation('abc', 'abc') is True

def test_check_two_strings_same_characters_different_order():
    # Both strings have the same length and characters. After sorting, both become 'a b c'.
    # Comparing character by character, all match, so return True.
    assert check_permutation('bca', 'cab') is True

def test_check_two_strings_different_lengths():
    # Lengths differ (3 vs 2), so function returns False immediately.
    assert check_permutation('abc', 'ab') is False

def test_check_two_strings_same_length_different_characters():
    # Lengths are equal. After sorting, str1 becomes 'a b c' and str2 becomes 'a b d'.
    # At index 4 (0-based), characters differ ('c' vs 'd'), so return False.
    assert check_permutation('abc', 'abd') is False

def test_check_two_empty_strings():
    # Both strings are empty, lengths equal zero. Sorted empty strings remain empty.
    # No characters to compare, so return True.
    assert check_permutation('', '') is True

def test_check_strings_with_repeated_characters():
    # Both strings have length 6 and same characters with same counts.
    # After sorting, both become 'a a b b c c'. Comparing character by character, all match, so return True.
    assert check_permutation('aabbcc', 'abcabc') is True

def test_check_strings_same_characters_different_counts():
    # Both strings have length 6. After sorting, str1 becomes 'a a b b c c' and str2 becomes 'a a b b b c'.
    # At index 6 (0-based), characters differ ('c' vs 'b'), so return False.
    assert check_permutation('aabbcc', 'aabbbc') is False