def by_length(arr):
    dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr

import pytest

def test_input_list_all_within_dictionary_keys():
    # Input list with numbers all within dictionary keys
    arr = [3, 1, 4]
    expected = ['Four', 'Three', 'One']
    assert by_length(arr) == expected

def test_input_list_with_numbers_outside_dictionary_keys():
    # Input list with numbers outside dictionary keys
    arr = [10, 2, 5]
    expected = ['Five', 'Two']
    assert by_length(arr) == expected

def test_input_list_with_duplicate_numbers():
    # Input list with duplicate numbers
    arr = [2, 2, 3]
    expected = ['Three', 'Two', 'Two']
    assert by_length(arr) == expected

def test_input_list_with_no_valid_dictionary_keys():
    # Input list with no valid dictionary keys
    arr = [0, 10, 11]
    expected = []
    assert by_length(arr) == expected

def test_empty_input_list():
    # Empty input list
    arr = []
    expected = []
    assert by_length(arr) == expected

def test_input_list_all_dictionary_keys_1_to_9():
    # Input list with all dictionary keys from 1 to 9
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    assert by_length(arr) == expected