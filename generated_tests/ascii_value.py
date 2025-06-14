def ascii_value(k):
  ch=k
  return ord(ch)

import pytest

def test_ascii_value_lowercase_a():
    # Calculate ASCII value of lowercase letter 'a'
    result = ascii_value('a')
    assert result == 97

def test_ascii_value_uppercase_Z():
    # Calculate ASCII value of uppercase letter 'Z'
    result = ascii_value('Z')
    assert result == 90

def test_ascii_value_digit_5():
    # Calculate ASCII value of digit character '5'
    result = ascii_value('5')
    assert result == 53

def test_ascii_value_space_character():
    # Calculate ASCII value of space character ' '
    result = ascii_value(' ')
    assert result == 32

def test_ascii_value_special_character_at():
    # Calculate ASCII value of special character '@'
    result = ascii_value('@')
    assert result == 64