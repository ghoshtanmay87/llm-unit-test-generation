def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return(len(final))

import pytest

def test_count_vowels_standard_vowels():
    # The string 'hello world' contains the vowels 'e', 'o', and 'o'.
    # Since vowels are 'aeiou', the function counts these 3 vowels.
    result = Check_Vow(string='hello world', vowels='aeiou')
    assert result == 3

def test_count_vowels_uppercase_vowels_included():
    # The string 'HELLO world' contains vowels 'E', 'O', and 'o'.
    # Since vowels include uppercase and lowercase, the function counts these 3 vowels.
    result = Check_Vow(string='HELLO world', vowels='aeiouAEIOU')
    assert result == 3

def test_count_vowels_no_vowels():
    # The string 'rhythm' contains no characters in 'aeiou', so the function returns 0.
    result = Check_Vow(string='rhythm', vowels='aeiou')
    assert result == 0

def test_count_vowels_empty_string():
    # An empty string has no characters, so no vowels are found, resulting in 0.
    result = Check_Vow(string='', vowels='aeiou')
    assert result == 0

def test_count_vowels_custom_vowel_set():
    # The string 'sky' contains 'y', and vowels is set to 'y', so the function counts 1 vowel.
    result = Check_Vow(string='sky', vowels='y')
    assert result == 1