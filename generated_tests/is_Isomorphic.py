def is_Isomorphic(str1,str2):          
    dict_str1 = {}
    dict_str2 = {}
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value,[]) + [i]        
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value,[]) + [j]
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False

import pytest

def test_isomorphic_strings_same_pattern():
    input_data = {'str1': 'egg', 'str2': 'add'}
    expected_output = True
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_strings_different_pattern():
    input_data = {'str1': 'foo', 'str2': 'bar'}
    expected_output = False
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_strings_same_length_different_characters():
    input_data = {'str1': 'paper', 'str2': 'title'}
    expected_output = True
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_strings_different_lengths():
    input_data = {'str1': 'abc', 'str2': 'ab'}
    expected_output = False
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_identical_strings():
    input_data = {'str1': 'hello', 'str2': 'hello'}
    expected_output = True
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_strings_repeated_characters():
    input_data = {'str1': 'aabb', 'str2': 'ccdd'}
    expected_output = True
    assert is_Isomorphic(**input_data) == expected_output

def test_isomorphic_strings_different_mappings():
    input_data = {'str1': 'abcd', 'str2': 'aabb'}
    expected_output = False
    assert is_Isomorphic(**input_data) == expected_output