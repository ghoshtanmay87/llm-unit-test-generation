import re
def replace_max_specialchar(text,n):
 return (re.sub("[ ,.]", ":", text, n))

import pytest

def test_replace_up_to_n_occurrences_in_simple_sentence():
    text = 'Hello, world. This is a test.'
    n = 2
    expected = 'Hello: world: This is a test.'
    assert replace_max_specialchar(text, n) == expected

def test_replace_all_occurrences_when_n_larger_than_total_special_chars():
    text = 'A, B. C D,E.'
    n = 10
    expected = 'A: B: C D:E:'
    assert replace_max_specialchar(text, n) == expected

def test_replace_zero_occurrences_when_n_zero():
    text = 'No changes here.'
    n = 0
    expected = 'No changes here.'
    assert replace_max_specialchar(text, n) == expected

def test_replace_only_first_three_special_chars_when_n_limits_replacements():
    text = 'One, two. Three four,five.'
    n = 3
    expected = 'One:two: Three four,five.'
    assert replace_max_specialchar(text, n) == expected

def test_replace_only_spaces_when_no_commas_or_periods_present():
    text = 'Space separated words only'
    n = 2
    expected = 'Space:separated:words only'
    assert replace_max_specialchar(text, n) == expected