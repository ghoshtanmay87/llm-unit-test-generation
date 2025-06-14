def sample_nam(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))

import pytest

def test_all_names_correct_capitalization():
    sample_names = ['Alice', 'Bob', 'Carol']
    expected_output = 14
    assert sample_nam(sample_names) == expected_output

def test_some_names_incorrect_capitalization():
    sample_names = ['Alice', 'bOb', 'Carol']
    expected_output = 10
    assert sample_nam(sample_names) == expected_output

def test_no_names_match_capitalization_pattern():
    sample_names = ['alice', 'BOB', 'carol']
    expected_output = 0
    assert sample_nam(sample_names) == expected_output

def test_empty_input_list():
    sample_names = []
    expected_output = 0
    assert sample_nam(sample_names) == expected_output

def test_single_name_correct_capitalization():
    sample_names = ['John']
    expected_output = 4
    assert sample_nam(sample_names) == expected_output

def test_single_name_incorrect_capitalization():
    sample_names = ['jOhn']
    expected_output = 0
    assert sample_nam(sample_names) == expected_output

def test_names_mixed_correct_and_incorrect_capitalization():
    sample_names = ['Anna', 'mike', 'George', 'susan']
    expected_output = 10
    assert sample_nam(sample_names) == expected_output

def test_names_with_single_character_strings():
    sample_names = ['A', 'b', 'C']
    expected_output = 2
    assert sample_nam(sample_names) == expected_output