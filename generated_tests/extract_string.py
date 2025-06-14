def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result

import pytest

def test_extract_strings_length_3():
    input_data = ['cat', 'dog', 'bird', 'fish']
    length = 3
    expected = ['cat', 'dog']
    assert extract_string(input_data, length) == expected

def test_extract_strings_length_4():
    input_data = ['tree', 'bush', 'flower', 'grass']
    length = 4
    expected = ['tree', 'bush', 'grass']
    assert extract_string(input_data, length) == expected

def test_extract_strings_length_5():
    input_data = ['hi', 'hello', 'hey', 'yo']
    length = 5
    expected = ['hello']
    assert extract_string(input_data, length) == expected

def test_extract_strings_length_0_with_empty_strings():
    input_data = ['', 'a', 'ab', '']
    length = 0
    expected = ['', '']
    assert extract_string(input_data, length) == expected

def test_extract_strings_length_2_empty_list():
    input_data = []
    length = 2
    expected = []
    assert extract_string(input_data, length) == expected