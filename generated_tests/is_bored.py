def is_bored(S):
    import re
    sentences = re.split('[.?!]\s*', S)
    return sum((sentence[0:2] == 'I ' for sentence in sentences))

import pytest

def test_multiple_sentences_starting_with_I_space():
    S = 'I am bored. I want to play! Are you coming? I hope so.'
    expected = 3
    assert is_bored(S) == expected

def test_no_sentences_starting_with_I_space():
    S = "You are here. We are ready! Let's go?"
    expected = 0
    assert is_bored(S) == expected

def test_sentences_starting_with_I_but_not_followed_by_space():
    S = "I'm happy. Iam bored. I am ready."
    expected = 1
    assert is_bored(S) == expected

def test_empty_sentences_due_to_trailing_punctuation():
    S = 'I am here! I am there! '
    expected = 2
    assert is_bored(S) == expected

def test_single_sentence_starting_with_I_space():
    S = 'I like Python.'
    expected = 1
    assert is_bored(S) == expected