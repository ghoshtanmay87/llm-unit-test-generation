def remove_length(test_str, K):
  temp = test_str.split()
  res = [ele for ele in temp if len(ele) != K]
  res = ' '.join(res)
  return (res)

import pytest

def test_remove_words_length_3_simple_sentence():
    # Remove words of length 3 from a simple sentence
    test_str = 'the cat sat on the mat'
    K = 3
    expected_output = 'on'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_4_mixed_lengths():
    # Remove words of length 4 from a sentence with mixed word lengths
    test_str = 'this test is only a test'
    K = 4
    expected_output = 'is a'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_2_multiple_2_letter_words():
    # Remove words of length 2 from a sentence with multiple 2-letter words
    test_str = 'to be or not to be'
    K = 2
    expected_output = 'or not'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_5_all_words_length_5():
    # Remove words of length 5 from a sentence where no word has length 5 (all words length 5)
    test_str = 'hello world'
    K = 5
    expected_output = ''
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_1_all_single_letter_words():
    # Remove words of length 1 from a sentence with single-letter words
    test_str = 'a b c d e f g'
    K = 1
    expected_output = ''
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_0_no_words_length_0():
    # Remove words of length 0 (no words have length 0)
    test_str = 'empty test case'
    K = 0
    expected_output = 'empty test case'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_6_mixed_word_lengths():
    # Remove words of length 6 from a sentence with mixed word lengths
    test_str = 'python coding is fun and easy'
    K = 6
    expected_output = 'is fun and easy'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_3_empty_input_string():
    # Empty input string
    test_str = ''
    K = 3
    expected_output = ''
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_7_one_7_letter_word():
    # Remove words of length 7 from a sentence with one 7-letter word
    test_str = 'welcome to the jungle'
    K = 7
    expected_output = 'to the jungle'
    assert remove_length(test_str, K) == expected_output

def test_remove_words_length_2_punctuation_treated_as_part_of_words():
    # Remove words of length 2 from a sentence with punctuation treated as part of words
    test_str = 'hi, my name is AI.'
    K = 2
    expected_output = 'hi, name AI.'
    assert remove_length(test_str, K) == expected_output