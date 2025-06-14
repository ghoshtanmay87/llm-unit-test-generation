def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return ' '.join(new_lst)

import pytest

def test_sentence_with_only_prime_length_words_greater_than_2():
    sentence = 'cat dog pig'
    expected_output = 'cat dog pig'
    assert words_in_sentence(sentence) == expected_output

def test_sentence_with_words_of_length_2_and_composite_length_greater_than_2():
    sentence = 'be tree on'
    expected_output = 'be on'
    assert words_in_sentence(sentence) == expected_output

def test_sentence_with_words_of_length_1_and_composite_length_greater_than_2():
    sentence = 'a four six'
    expected_output = 'six'
    assert words_in_sentence(sentence) == expected_output

def test_sentence_with_words_of_length_1_2_and_prime_length_greater_than_2():
    sentence = 'a be cat dog'
    expected_output = 'be cat dog'
    assert words_in_sentence(sentence) == expected_output

def test_sentence_with_words_of_length_1_2_and_composite_length_greater_than_2():
    sentence = 'a be tree four'
    expected_output = 'be'
    assert words_in_sentence(sentence) == expected_output