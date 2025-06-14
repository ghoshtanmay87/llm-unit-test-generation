import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))

import pytest

def test_extract_single_quoted_phrase_from_text():
    text1 = 'He said "hello" to everyone.'
    expected = ['hello']
    assert extract_quotation(text1) == expected

def test_extract_multiple_quoted_phrases_from_text():
    text1 = 'She said "yes" and then "no".'
    expected = ['yes', 'no']
    assert extract_quotation(text1) == expected

def test_no_quoted_phrases_in_text():
    text1 = 'No quotes here.'
    expected = []
    assert extract_quotation(text1) == expected

def test_quoted_phrases_with_empty_quotes():
    text1 = 'Empty quotes "" and "non-empty".'
    expected = ['', 'non-empty']
    assert extract_quotation(text1) == expected

def test_quoted_phrases_with_nested_quotes_inside():
    text1 = 'He said "She said \\"hello\\"" loudly.'
    expected = ['She said \\"hello\\"']
    assert extract_quotation(text1) == expected