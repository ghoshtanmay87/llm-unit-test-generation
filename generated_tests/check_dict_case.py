def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False
    else:
        state = 'start'
        for key in dict.keys():
            if isinstance(key, str) == False:
                state = 'mixed'
                break
            if state == 'start':
                if key.isupper():
                    state = 'upper'
                elif key.islower():
                    state = 'lower'
                else:
                    break
            elif state == 'upper' and (not key.isupper()) or (state == 'lower' and (not key.islower())):
                state = 'mixed'
                break
            else:
                break
        return state == 'upper' or state == 'lower'

import pytest

def test_empty_dictionary_returns_false():
    # The dictionary has no keys, so the function immediately returns False.
    input_dict = {}
    expected = False
    assert check_dict_case(input_dict) == expected

def test_all_keys_uppercase_strings_returns_true():
    # All keys are strings and uppercase, so state changes from 'start' to 'upper' and remains 'upper', returning True.
    input_dict = {'A': 1, 'B': 2, 'C': 3}
    expected = True
    assert check_dict_case(input_dict) == expected

def test_all_keys_lowercase_strings_returns_true():
    # All keys are strings and lowercase, so state changes from 'start' to 'lower' and remains 'lower', returning True.
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = True
    assert check_dict_case(input_dict) == expected

def test_mixed_case_keys_returns_false():
    # First key 'A' sets state to 'upper', second key 'b' is lowercase, which breaks the uniform case condition, setting state to 'mixed' and returning False.
    input_dict = {'A': 1, 'b': 2, 'C': 3}
    expected = False
    assert check_dict_case(input_dict) == expected

def test_non_string_key_causes_immediate_mixed_state_and_returns_false():
    # First key is integer (not string), so state is set to 'mixed' immediately and function returns False.
    input_dict = {1: 'one', 'B': 'two'}
    expected = False
    assert check_dict_case(input_dict) == expected

def test_key_with_mixed_case_letters_causes_break_and_returns_false():
    # First key 'Abc' is string but neither all uppercase nor all lowercase, so loop breaks and returns False.
    input_dict = {'Abc': 1, 'DEF': 2}
    expected = False
    assert check_dict_case(input_dict) == expected

def test_single_uppercase_key_returns_true():
    # Single key 'X' is uppercase string, so state becomes 'upper' and returns True.
    input_dict = {'X': 100}
    expected = True
    assert check_dict_case(input_dict) == expected

def test_single_lowercase_key_returns_true():
    # Single key 'x' is lowercase string, so state becomes 'lower' and returns True.
    input_dict = {'x': 100}
    expected = True
    assert check_dict_case(input_dict) == expected

def test_key_with_non_alphabetic_characters_breaks_and_returns_false():
    # '123' is string but neither isupper() nor islower() returns True, so loop breaks and returns False.
    input_dict = {'123': 'numbers', 'ABC': 'letters'}
    expected = False
    assert check_dict_case(input_dict) == expected

def test_all_keys_uppercase_but_one_key_is_mixed_case_returns_false():
    # First two keys are uppercase, state is 'upper', third key 'cD' is mixed case, so state changes to 'mixed' and returns False.
    input_dict = {'A': 1, 'B': 2, 'cD': 3}
    expected = False
    assert check_dict_case(input_dict) == expected