def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]

import pytest

def test_capitalize_first_last_letters_simple_lowercase_sentence():
    input_str = 'hello world'
    expected = 'HellO WorlD'
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_single_word_mixed_case():
    input_str = 'pYtHon'
    expected = 'PythoN'
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_multiple_words_with_punctuation():
    input_str = 'this is a test.'
    expected = 'ThiS Is A TesT.'
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_single_character_words():
    input_str = 'a i u e o'
    expected = 'A I U E O'
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_empty_string():
    input_str = ''
    expected = ''
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_already_capitalized_words():
    input_str = 'Already Capitalized Words'
    expected = 'AlreadY CapitalizeD WordS'
    assert capitalize_first_last_letters(input_str) == expected

def test_capitalize_first_last_letters_hyphenated_words_treated_as_separate_words():
    input_str = 'well-known fact'
    expected = 'WelL-KnowN FacT'
    assert capitalize_first_last_letters(input_str) == expected