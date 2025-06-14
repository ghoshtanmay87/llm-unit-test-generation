from typing import List

def sort_numbers(numbers: str) -> str:
    value_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))

import pytest

def test_sort_simple_list_of_number_words():
    # Scenario: Sort a simple list of number words in ascending order
    input_numbers = 'three one four'
    expected = 'one three four'
    assert sort_numbers(input_numbers) == expected

def test_sort_input_with_repeated_number_words():
    # Scenario: Handle input with repeated number words
    input_numbers = 'five two five one'
    expected = 'one two five five'
    assert sort_numbers(input_numbers) == expected

def test_sort_input_with_extra_spaces_between_words():
    # Scenario: Handle input with extra spaces between words
    input_numbers = '  seven  three  nine '
    expected = 'three seven nine'
    assert sort_numbers(input_numbers) == expected

def test_sort_input_with_single_number_word():
    # Scenario: Handle input with a single number word
    input_numbers = 'zero'
    expected = 'zero'
    assert sort_numbers(input_numbers) == expected

def test_sort_empty_input_string():
    # Scenario: Handle empty input string
    input_numbers = ''
    expected = ''
    assert sort_numbers(input_numbers) == expected

def test_sort_all_number_words_in_descending_order():
    # Scenario: Handle input with all number words in descending order
    input_numbers = 'nine eight seven six five four three two one zero'
    expected = 'zero one two three four five six seven eight nine'
    assert sort_numbers(input_numbers) == expected