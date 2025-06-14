import re
def fill_spaces(text):
  return (re.sub("[ ,.]", ":", text))

import pytest

def test_replace_spaces_with_colons_in_simple_sentence():
    input_text = 'hello world'
    expected = 'hello:world'
    assert fill_spaces(input_text) == expected

def test_replace_spaces_commas_periods_with_colons():
    input_text = 'hello, world. How are you?'
    expected = 'hello::world::How:are:you?'
    assert fill_spaces(input_text) == expected

def test_multiple_consecutive_spaces_and_punctuation():
    input_text = 'a  b, c. d'
    expected = 'a::b::c::d'
    assert fill_spaces(input_text) == expected

def test_string_with_no_spaces_commas_or_periods():
    input_text = 'hello_world!'
    expected = 'hello_world!'
    assert fill_spaces(input_text) == expected

def test_empty_string_input():
    input_text = ''
    expected = ''
    assert fill_spaces(input_text) == expected

def test_string_with_only_spaces_commas_and_periods():
    input_text = ' , . ,'
    expected = ':::::'
    assert fill_spaces(input_text) == expected