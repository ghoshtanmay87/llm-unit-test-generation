import re
text = 'Python Exercises'
def replace_spaces(text):
  text =text.replace (" ", "_")
  return (text)
  text =text.replace ("_", " ")
  return (text)

import pytest

def test_replace_single_space_with_underscore_in_simple_string():
    input_text = 'Python Exercises'
    expected = 'Python_Exercises'
    assert replace_spaces(input_text) == expected

def test_replace_multiple_spaces_with_underscores():
    input_text = 'Hello World Test'
    expected = 'Hello_World_Test'
    assert replace_spaces(input_text) == expected

def test_string_with_no_spaces_remains_unchanged():
    input_text = 'NoSpacesHere'
    expected = 'NoSpacesHere'
    assert replace_spaces(input_text) == expected

def test_string_with_leading_and_trailing_spaces():
    input_text = ' Leading and trailing '
    expected = '_Leading_and_trailing_'
    assert replace_spaces(input_text) == expected

def test_empty_string_input():
    input_text = ''
    expected = ''
    assert replace_spaces(input_text) == expected