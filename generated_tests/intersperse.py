from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result

import pytest

def test_intersperse_empty_list_returns_empty_list():
    numbers = []
    delimeter = 0
    expected = []
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_single_element_list_returns_same_list():
    numbers = [5]
    delimeter = 99
    expected = [5]
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_multiple_elements_inserts_delimiter_between_each_pair():
    numbers = [1, 2, 3]
    delimeter = 0
    expected = [1, 0, 2, 0, 3]
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_negative_delimiter_with_multiple_elements():
    numbers = [10, 20, 30]
    delimeter = -1
    expected = [10, -1, 20, -1, 30]
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_repeated_numbers_and_delimiter():
    numbers = [7, 7, 7]
    delimeter = 1
    expected = [7, 1, 7, 1, 7]
    assert intersperse(numbers, delimeter) == expected