def find_Rotations(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n

import pytest

def test_no_rotation_original_string():
    # Check rotation index for a string with no rotation (original string)
    input_str = 'abcde'
    expected = 5
    assert find_Rotations(input_str) == expected

def test_rotation_by_1_position():
    # Check rotation index for a string rotated by 1 position
    input_str = 'bcdea'
    expected = 1
    assert find_Rotations(input_str) == expected

def test_rotation_by_2_positions():
    # Check rotation index for a string rotated by 2 positions
    input_str = 'cdeab'
    expected = 2
    assert find_Rotations(input_str) == expected

def test_rotation_by_3_positions():
    # Check rotation index for a string rotated by 3 positions
    input_str = 'deabc'
    expected = 3
    assert find_Rotations(input_str) == expected

def test_rotation_by_4_positions():
    # Check rotation index for a string rotated by 4 positions
    input_str = 'eabcd'
    expected = 4
    assert find_Rotations(input_str) == expected

def test_all_identical_characters():
    # Check rotation index for a string with all identical characters
    input_str = 'aaaaa'
    expected = 1
    assert find_Rotations(input_str) == expected

def test_single_character_string():
    # Check rotation index for a single character string
    input_str = 'z'
    expected = 1
    assert find_Rotations(input_str) == expected

def test_repeated_pattern_string():
    # Check rotation index for a string with repeated pattern
    input_str = 'abab'
    expected = 2
    assert find_Rotations(input_str) == expected

def test_no_internal_rotation_match():
    # Check rotation index for a string with no internal rotation match
    input_str = 'abcdefg'
    expected = 7
    assert find_Rotations(input_str) == expected