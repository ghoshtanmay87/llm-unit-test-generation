def words_string(s):
    if not s:
        return []
    s_list = []
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    s_list = ''.join(s_list)
    return s_list.split()

import pytest

def test_empty_string_input_returns_empty_list():
    assert words_string('') == []

def test_string_with_no_commas_splits_on_whitespace():
    assert words_string('hello world') == ['hello', 'world']

def test_string_with_commas_replaced_by_spaces_and_split():
    assert words_string('hello,world') == ['hello', 'world']

def test_string_with_multiple_commas_and_spaces():
    assert words_string('one,two, three,four') == ['one', 'two', 'three', 'four']

def test_string_with_consecutive_commas_treated_as_multiple_spaces():
    assert words_string('a,,b') == ['a', 'b']

def test_string_with_commas_at_start_and_end():
    assert words_string(',start,end,') == ['start', 'end']

def test_string_with_only_commas():
    assert words_string(',,,') == []

def test_string_with_letters_commas_and_spaces_mixed():
    assert words_string('a, b,c d,e') == ['a', 'b', 'c', 'd', 'e']