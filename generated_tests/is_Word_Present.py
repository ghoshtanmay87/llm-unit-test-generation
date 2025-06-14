def is_Word_Present(sentence,word): 
    s = sentence.split(" ") 
    for i in s:  
        if (i == word): 
            return True
    return False

import pytest

def test_word_present_as_standalone_word():
    # The sentence splits into ['hello', 'world'].
    # The word 'world' matches exactly one of the split words, so the function returns True.
    assert is_Word_Present('hello world', 'world') is True

def test_word_not_present_in_sentence():
    # The sentence splits into ['hello', 'there'].
    # The word 'world' does not match any of these words, so the function returns False.
    assert is_Word_Present('hello there', 'world') is False

def test_word_is_substring_but_not_standalone():
    # The sentence splits into ['helloworld', 'is', 'a', 'test'].
    # None of these words exactly match 'world', so the function returns False.
    assert is_Word_Present('helloworld is a test', 'world') is False

def test_word_present_multiple_times():
    # The sentence splits into ['test', 'test', 'test'].
    # The word 'test' matches the first word, so the function returns True immediately.
    assert is_Word_Present('test test test', 'test') is True

def test_word_with_punctuation_attached():
    # The sentence splits into ['hello,', 'world!'].
    # Neither 'hello,' nor 'world!' exactly matches 'world' due to punctuation, so the function returns False.
    assert is_Word_Present('hello, world!', 'world') is False