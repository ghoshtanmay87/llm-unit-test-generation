def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen]

import pytest

def test_multiple_words_one_even_length_longest():
    # Words: 'I'(1), 'am'(2), 'testing'(7), 'this'(4), 'function'(8)
    # Longest even length word is 'function' (8)
    result = find_Max_Len_Even('I am testing this function')
    assert result == 'function'

def test_multiple_words_longest_even_length_at_end():
    # Same input as above, longest even length word at the end is 'function'
    result = find_Max_Len_Even('I am testing this function')
    assert result == 'function'

def test_no_even_length_words():
    # Words: 'one'(3), 'two'(3), 'three'(5) all odd length
    result = find_Max_Len_Even('one two three')
    assert result == '-1'

def test_all_even_length_multiple_same_max_length():
    # Words: 'to'(2), 'be'(2), 'or'(2), 'not'(3), 'to'(2), 'be'(2)
    # Max even length is 2, first such word is 'to'
    result = find_Max_Len_Even('to be or not to be')
    assert result == 'to'

def test_single_even_length_word():
    # Correction in reasoning: both words 'hello'(5) and 'world'(5) are odd length
    # So output should be '-1'
    result = find_Max_Len_Even('hello world')
    assert result == '-1'

def test_single_even_length_word_at_start():
    # Words: 'even'(4) even, 'odd'(3) odd, 'odd'(3) odd
    # Longest even length word is 'even'
    result = find_Max_Len_Even('even odd odd')
    assert result == 'even'

def test_trailing_spaces():
    # Word 'test' length 4 even, trailing spaces ignored
    result = find_Max_Len_Even('test  ')
    assert result == 'test'

def test_leading_spaces():
    # Leading spaces ignored, word 'test' length 4 even
    result = find_Max_Len_Even('  test')
    assert result == 'test'

def test_multiple_spaces_between_words():
    # Words: 'a'(1), 'bb'(2), 'ccc'(3), 'dddd'(4)
    # Longest even length word is 'dddd'
    result = find_Max_Len_Even('a  bb   ccc dddd')
    assert result == 'dddd'

def test_empty_string_input():
    # No words, so no even length word
    result = find_Max_Len_Even('')
    assert result == '-1'