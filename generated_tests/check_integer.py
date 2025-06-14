def check_integer(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False

import pytest

def test_empty_string_input():
    # After stripping, the string is empty (length < 1), so the function returns None.
    assert check_integer(text='') is None

def test_string_with_only_digits():
    # All characters are digits, so the function returns True.
    assert check_integer(text='12345') is True

def test_string_with_leading_and_trailing_spaces_but_digits_only():
    # After stripping, the string is '6789' which contains only digits, so returns True.
    assert check_integer(text='  6789  ') is True

def test_string_with_leading_plus_sign_and_digits():
    # First character is '+', rest are digits, so returns True.
    assert check_integer(text='+123') is True

def test_string_with_leading_minus_sign_and_digits():
    # First character is '-', rest are digits, so returns True.
    assert check_integer(text='-456') is True

def test_string_with_plus_sign_but_no_digits():
    # First character is '+', but there are no digits after it, so returns False.
    assert check_integer(text='+') is False

def test_string_with_minus_sign_but_no_digits():
    # First character is '-', but there are no digits after it, so returns False.
    assert check_integer(text='-') is False

def test_string_with_digits_and_trailing_plus_sign():
    # The last character '+' is not a digit, and '+' is only allowed at the start, so returns False.
    assert check_integer(text='123+') is False

def test_string_with_digits_and_trailing_minus_sign():
    # The last character '-' is not a digit, and '-' is only allowed at the start, so returns False.
    assert check_integer(text='456-') is False

def test_string_with_letters_mixed_with_digits():
    # Contains a non-digit character 'a', so returns False.
    assert check_integer(text='12a34') is False

def test_string_with_spaces_inside_digits():
    # Space is not a digit, so returns False.
    assert check_integer(text='12 34') is False

def test_string_with_only_spaces():
    # After stripping, string is empty, so returns None.
    assert check_integer(text='    ') is None

def test_string_with_plus_sign_and_spaces_after_it():
    # After stripping, first character is '+', but the next character is space which is not a digit, so returns False.
    assert check_integer(text='+ 123') is False

def test_string_with_minus_sign_and_spaces_after_it():
    # After stripping, first character is '-', but the next character is space which is not a digit, so returns False.
    assert check_integer(text='- 456') is False

def test_string_with_multiple_plus_signs():
    # First character is '+', but second character is also '+', which is not a digit, so returns False.
    assert check_integer(text='++123') is False

def test_string_with_multiple_minus_signs():
    # First character is '-', but second character is also '-', which is not a digit, so returns False.
    assert check_integer(text='--456') is False