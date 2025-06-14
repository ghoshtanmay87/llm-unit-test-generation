from collections import Counter 
def anagram_lambda(texts,str):
  result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
  return result

import pytest

def test_anagrams_of_listen_with_mixed_texts():
    texts = ['enlist', 'google', 'inlets', 'banana', 'silent']
    str_input = 'listen'
    expected = ['enlist', 'inlets', 'silent']
    assert anagram_lambda(texts, str_input) == expected

def test_anagrams_of_abc_with_no_anagrams():
    texts = ['def', 'ghi', 'jkl']
    str_input = 'abc'
    expected = []
    assert anagram_lambda(texts, str_input) == expected

def test_anagrams_of_empty_string_with_empty_and_nonempty_texts():
    texts = ['', 'a', ' ']
    str_input = ''
    expected = ['']
    assert anagram_lambda(texts, str_input) == expected

def test_anagrams_of_aabbcc_with_repeated_characters():
    texts = ['abcabc', 'aabbcc', 'abccba', 'aabbc', 'aabbccc']
    str_input = 'aabbcc'
    expected = ['abcabc', 'aabbcc', 'abccba']
    assert anagram_lambda(texts, str_input) == expected

def test_anagrams_of_Dormitory_with_case_differences():
    texts = ['dirtyroom', 'Dormitory', 'dirtyRoom', 'dormitory']
    str_input = 'Dormitory'
    expected = ['Dormitory']
    assert anagram_lambda(texts, str_input) == expected