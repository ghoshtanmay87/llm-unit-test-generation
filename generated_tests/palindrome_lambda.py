def palindrome_lambda(texts):
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result

import pytest

def test_filter_palindromes_mixed_list():
    # Filter palindromes from a list of strings with mixed palindromes and non-palindromes
    texts = ['racecar', 'hello', 'level', 'world', 'madam']
    expected = ['racecar', 'level', 'madam']
    assert palindrome_lambda(texts) == expected

def test_filter_palindromes_all_palindromes():
    # Input list contains only palindromes
    texts = ['noon', 'civic', 'radar']
    expected = ['noon', 'civic', 'radar']
    assert palindrome_lambda(texts) == expected

def test_filter_palindromes_no_palindromes():
    # Input list contains no palindromes
    texts = ['python', 'java', 'code']
    expected = []
    assert palindrome_lambda(texts) == expected

def test_filter_palindromes_empty_and_single_chars():
    # Input list contains empty string and single character strings
    texts = ['', 'a', 'b', 'ab']
    expected = ['', 'a', 'b']
    assert palindrome_lambda(texts) == expected

def test_filter_palindromes_case_sensitive():
    # Input list contains palindromes with mixed case sensitivity
    texts = ['Deed', 'deed', 'DeeD']
    expected = ['deed']
    assert palindrome_lambda(texts) == expected