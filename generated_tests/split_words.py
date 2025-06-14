def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

import pytest

def test_split_words_with_spaces():
    # Input string contains spaces, so split by spaces
    input_txt = 'hello world'
    expected = ['hello', 'world']
    assert split_words(input_txt) == expected

def test_split_words_with_commas_no_spaces():
    # Input string contains commas but no spaces, so replace commas with spaces and split
    input_txt = 'apple,banana,carrot'
    expected = ['apple', 'banana', 'carrot']
    assert split_words(input_txt) == expected

def test_split_words_no_spaces_no_commas_count_lowercase_even_ascii():
    # Input string contains neither spaces nor commas, so count lowercase letters with even ASCII codes
    input_txt = 'abcXYZ'
    expected = 1
    assert split_words(input_txt) == expected

def test_split_words_spaces_and_commas_spaces_take_precedence():
    # Input string with spaces and commas, spaces take precedence
    input_txt = 'one, two, three'
    expected = ['one,', 'two,', 'three']
    assert split_words(input_txt) == expected

def test_split_words_no_spaces_no_commas_all_lowercase_odd_ascii():
    # Input string with no spaces or commas, all lowercase letters have odd ASCII codes
    input_txt = 'aceg'
    expected = 0
    assert split_words(input_txt) == expected

def test_split_words_no_spaces_no_commas_multiple_lowercase_even_ascii():
    # Input string with no spaces or commas, multiple lowercase letters with even ASCII codes
    input_txt = 'bdfh'
    expected = 4
    assert split_words(input_txt) == expected

def test_split_words_empty_string():
    # Input string is empty
    input_txt = ''
    expected = 0
    assert split_words(input_txt) == expected

def test_split_words_uppercase_only_no_spaces_no_commas():
    # Input string with uppercase letters only and no spaces or commas
    input_txt = 'ABCDEF'
    expected = 0
    assert split_words(input_txt) == expected