def count_element_in_list(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr

import pytest

def test_count_occurrences_element_in_some_strings():
    list1 = ['apple', 'banana', 'apricot', 'grape']
    x = 'ap'
    expected = 3
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_single_character_in_list():
    list1 = ['cat', 'dog', 'bird', 'cow']
    x = 'o'
    expected = 2
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_element_not_present():
    list1 = ['red', 'blue', 'green']
    x = 'yellow'
    expected = 0
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_list_with_empty_strings():
    list1 = ['', 'empty', '']
    x = 'e'
    expected = 1
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_element_is_empty_string():
    list1 = ['a', 'b', 'c']
    x = ''
    expected = 3
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_element_substring_of_some_strings():
    list1 = ['hello', 'world', 'hold', 'cold']
    x = 'ol'
    expected = 3
    assert count_element_in_list(list1, x) == expected

def test_count_occurrences_empty_list():
    list1 = []
    x = 'any'
    expected = 0
    assert count_element_in_list(list1, x) == expected