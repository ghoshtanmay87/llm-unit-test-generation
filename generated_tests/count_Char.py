def count_Char(str,x): 
    count = 0
    for i in range(len(str)):  
        if (str[i] == x) : 
            count += 1
    n = 10
    repititions = n // len(str)  
    count = count * repititions  
    l = n % len(str)  
    for i in range(l): 
        if (str[i] == x):  
            count += 1
    return count

import pytest

def test_count_char_a_in_short_string():
    # Count occurrences of character 'a' in a string shorter than 10 characters
    result = count_Char('abc', 'a')
    assert result == 4

def test_count_char_b_in_short_string():
    # Count occurrences of character 'b' in a string shorter than 10 characters
    result = count_Char('abc', 'b')
    assert result == 3

def test_count_char_c_in_short_string():
    # Count occurrences of character 'c' in a string shorter than 10 characters
    result = count_Char('abc', 'c')
    assert result == 3

def test_count_char_a_in_string_length_10():
    # Count occurrences of character 'a' in a string of length exactly 10
    result = count_Char('abcdefghij', 'a')
    assert result == 1

def test_count_char_z_in_string_length_10_no_z():
    # Count occurrences of character 'z' in a string of length exactly 10 with no 'z'
    result = count_Char('abcdefghij', 'z')
    assert result == 0

def test_count_char_a_in_string_longer_than_10():
    # Count occurrences of character 'a' in a string longer than 10 characters
    result = count_Char('abcdefghijklm', 'a')
    assert result == 1

def test_count_char_m_in_string_longer_than_10():
    # Count occurrences of character 'm' in a string longer than 10 characters
    result = count_Char('abcdefghijklm', 'm')
    assert result == 0

def test_count_char_a_in_string_length_1():
    # Count occurrences of character 'a' in a string of length 1
    result = count_Char('a', 'a')
    assert result == 10

def test_count_char_b_in_string_length_1_different_char():
    # Count occurrences of character 'b' in a string of length 1 with different character
    result = count_Char('a', 'b')
    assert result == 0

def test_count_char_x_in_string_with_multiple_occurrences():
    # Count occurrences of character 'x' in a string with multiple occurrences
    result = count_Char('xxabcxx', 'x')
    assert result == 6