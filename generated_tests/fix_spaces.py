def fix_spaces(text):
    new_text = ''
    i = 0
    start, end = (0, 0)
    while i < len(text):
        if text[i] == ' ':
            end += 1
        else:
            if end - start > 2:
                new_text += '-' + text[i]
            elif end - start > 0:
                new_text += '_' * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = (i + 1, i + 1)
        i += 1
    if end - start > 2:
        new_text += '-'
    elif end - start > 0:
        new_text += '_'
    return new_text

import pytest

def test_fix_spaces_no_spaces():
    # Input with no spaces
    result = fix_spaces(text='hello')
    assert result == 'hello'

def test_fix_spaces_single_spaces_between_characters():
    # Input with single spaces between characters
    result = fix_spaces(text='a b c')
    assert result == 'a_b_c'

def test_fix_spaces_two_spaces_between_characters():
    # Input with two spaces between characters
    result = fix_spaces(text='a  b  c')
    assert result == 'a__b__c'

def test_fix_spaces_three_spaces_between_characters():
    # Input with three spaces between characters
    result = fix_spaces(text='a   b   c')
    assert result == 'a-b-c'

def test_fix_spaces_mixed_space_counts():
    # Input with mixed space counts
    result = fix_spaces(text='x  y   z w')
    assert result == 'x__y-z_w'

def test_fix_spaces_trailing_three_spaces():
    # Input with trailing spaces
    result = fix_spaces(text='end   ')
    assert result == 'end-'

def test_fix_spaces_trailing_single_space():
    # Input with trailing single space
    result = fix_spaces(text='end ')
    assert result == 'end_'

def test_fix_spaces_leading_spaces():
    # Input with leading spaces
    result = fix_spaces(text='   start')
    assert result == '-start'

def test_fix_spaces_only_spaces():
    # Input with only spaces
    result = fix_spaces(text='    ')
    assert result == '-'

def test_fix_spaces_empty_string():
    # Empty string input
    result = fix_spaces(text='')
    assert result == ''