def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])

import pytest

def test_generate_sequence_string_from_0_to_5():
    n = 5
    expected_output = '0 1 2 3 4 5'
    assert string_sequence(n) == expected_output

def test_generate_sequence_string_from_0_to_0_single_element():
    n = 0
    expected_output = '0'
    assert string_sequence(n) == expected_output

def test_generate_sequence_string_from_0_to_3():
    n = 3
    expected_output = '0 1 2 3'
    assert string_sequence(n) == expected_output

def test_generate_sequence_string_from_0_to_1():
    n = 1
    expected_output = '0 1'
    assert string_sequence(n) == expected_output

def test_generate_sequence_string_from_0_to_10():
    n = 10
    expected_output = '0 1 2 3 4 5 6 7 8 9 10'
    assert string_sequence(n) == expected_output