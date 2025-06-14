def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)

import pytest

def test_remove_xyz_from_hello_not_palindrome():
    # Remove characters 'xyz' from 'hello' and check palindrome
    result = reverse_delete('hello', 'xyz')
    assert result == ('hello', False)

def test_remove_vowels_from_racecar_palindrome():
    # Remove vowels from 'racecar' and check palindrome
    result = reverse_delete('racecar', 'aeiou')
    assert result == ('rccr', True)

def test_remove_all_chars_from_abc_empty_palindrome():
    # Remove all characters from 'abc' and check palindrome
    result = reverse_delete('abc', 'abc')
    assert result == ('', True)

def test_remove_l_from_level_palindrome():
    # Remove characters 'l' from 'level' and check palindrome
    result = reverse_delete('level', 'l')
    assert result == ('eve', True)

def test_remove_z_from_empty_string_palindrome():
    # Remove characters 'z' from empty string and check palindrome
    result = reverse_delete('', 'z')
    assert result == ('', True)

def test_remove_vowels_from_python_not_palindrome():
    # Remove characters 'aeiou' from 'python' and check palindrome
    result = reverse_delete('python', 'aeiou')
    assert result == ('pythn', False)

def test_remove_abc_from_abracadabra_palindrome():
    # Remove characters 'abc' from 'abracadabra' and check palindrome
    result = reverse_delete('abracadabra', 'abc')
    assert result == ('rdr', True)