import re
def multiple_split(text):
  return (re.split('; |, |\*|\n',text))

import pytest

def test_split_string_with_semicolon_and_space_delimiter():
    text = 'apple; banana; cherry'
    expected = ['apple', 'banana', 'cherry']
    assert multiple_split(text) == expected

def test_split_string_with_comma_and_space_delimiter():
    text = 'dog, cat, mouse'
    expected = ['dog', 'cat', 'mouse']
    assert multiple_split(text) == expected

def test_split_string_with_asterisk_delimiter():
    text = 'red*green*blue'
    expected = ['red', 'green', 'blue']
    assert multiple_split(text) == expected

def test_split_string_with_newline_delimiter():
    text = 'line1\nline2\nline3'
    expected = ['line1', 'line2', 'line3']
    assert multiple_split(text) == expected

def test_split_string_with_mixed_delimiters():
    text = 'one; two,three*four\nfive'
    expected = ['one', 'two', 'three', 'four', 'five']
    assert multiple_split(text) == expected

def test_split_string_with_delimiters_but_no_spaces_after_semicolon_or_comma():
    text = 'a;b,c*d\ne'
    expected = ['a;b,c*d\ne']
    assert multiple_split(text) == expected

def test_split_string_with_multiple_consecutive_delimiters():
    text = 'x; y, z*\n'
    expected = ['x', 'y', 'z', '']
    assert multiple_split(text) == expected

def test_split_string_with_only_delimiters():
    text = '; , * \n'
    expected = ['; , * ']
    assert multiple_split(text) == expected