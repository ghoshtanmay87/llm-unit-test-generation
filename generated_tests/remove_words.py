def remove_words(list1, charlist):
    new_list = []
    for line in list1:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])
        new_list.append(new_words)
    return new_list

import pytest

def test_remove_words_with_substring_o_removes_correct_words():
    list1 = ['hello world', 'python programming is fun']
    charlist = ['o']
    expected = ['', 'is fun']
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_substrings_a_and_e_removes_correct_words():
    list1 = ['apple banana cherry', 'date elderberry fig grape']
    charlist = ['a', 'e']
    expected = ['', 'fig']
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_nonexistent_substring_removes_no_words():
    list1 = ['cat dog', 'bird fish']
    charlist = ['z']
    expected = ['cat dog', 'bird fish']
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_empty_input_list_returns_empty_list():
    list1 = []
    charlist = ['a']
    expected = []
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_empty_charlist_removes_no_words():
    list1 = ['one two three', 'four five six']
    charlist = []
    expected = ['one two three', 'four five six']
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_substring_the_removes_words_containing_the():
    list1 = ['the quick brown fox', 'jumps over the lazy dog']
    charlist = ['the']
    expected = ['quick brown fox', 'jumps over lazy dog']
    assert remove_words(list1, charlist) == expected

def test_remove_words_with_substring_cat_removes_all_words_containing_cat():
    list1 = ['catapult catalog scatter', 'concatenate category']
    charlist = ['cat']
    expected = ['', '']
    assert remove_words(list1, charlist) == expected