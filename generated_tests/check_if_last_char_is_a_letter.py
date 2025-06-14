def check_if_last_char_is_a_letter(txt):
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and 97 <= ord(check.lower()) <= 122 else False

import pytest

def test_single_letter_word_at_the_end_lowercase():
    result = check_if_last_char_is_a_letter(txt='hello a')
    assert result is True

def test_single_letter_word_at_the_end_uppercase():
    result = check_if_last_char_is_a_letter(txt='hello Z')
    assert result is True

def test_last_word_longer_than_one_character():
    result = check_if_last_char_is_a_letter(txt='hello world')
    assert result is False

def test_last_word_is_single_non_letter_character():
    result = check_if_last_char_is_a_letter(txt='hello !')
    assert result is False

def test_single_letter_word_at_the_end_digit():
    result = check_if_last_char_is_a_letter(txt='number 5')
    assert result is False

def test_empty_string_input():
    result = check_if_last_char_is_a_letter(txt='')
    assert result is False

def test_single_letter_word_at_the_end_with_mixed_case():
    result = check_if_last_char_is_a_letter(txt='check Y')
    assert result is True

def test_last_word_is_two_letter_word():
    result = check_if_last_char_is_a_letter(txt='go to')
    assert result is False

def test_last_word_is_single_letter_but_non_alphabetic_symbol():
    result = check_if_last_char_is_a_letter(txt='end #')
    assert result is False

def test_string_with_trailing_spaces_and_single_letter_at_the_end():
    result = check_if_last_char_is_a_letter(txt='test x  ')
    assert result is False