def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'

import pytest

def test_first_repeated_word_simple_sentence():
    # Find the first repeated word in a simple sentence with one repeated word
    input_str = 'hello world hello'
    expected = 'hello'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_no_repeats():
    # No repeated words in the input string
    input_str = 'this is a test'
    expected = 'None'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_first_repeated_later():
    # First repeated word is the second occurrence of a word appearing later in the string
    input_str = 'one two three two one'
    expected = 'two'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_immediate_repeat():
    # Repeated word appears immediately after its first occurrence
    input_str = 'repeat repeat word'
    expected = 'repeat'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_empty_string():
    # Empty string input returns 'None'
    input_str = ''
    expected = 'None'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_case_sensitive():
    # Case sensitive check for repeated words
    input_str = 'Word word Word'
    expected = 'Word'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_punctuation():
    # Repeated punctuation treated as part of the word
    input_str = 'hello, world hello,'
    expected = 'hello,'
    assert first_repeated_word(input_str) == expected

def test_first_repeated_word_multiple_repeats():
    # Multiple repeated words, return the first repeated one
    input_str = 'a b c a b c'
    expected = 'a'
    assert first_repeated_word(input_str) == expected