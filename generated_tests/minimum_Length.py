def minimum_Length(s) : 
    maxOcc = 0
    n = len(s) 
    arr = [0]*26
    for i in range(n) : 
        arr[ord(s[i]) -ord('a')] += 1
    for i in range(26) : 
        if arr[i] > maxOcc : 
            maxOcc = arr[i] 
    return n - maxOcc

import pytest

def test_all_characters_are_the_same():
    # The string length is 5, and the maximum occurrence of any character is 5 (all 'a's).
    # The function returns 5 - 5 = 0.
    assert minimum_Length('aaaaa') == 0

def test_all_characters_are_unique():
    # The string length is 5, each character appears once, so max occurrence is 1.
    # The function returns 5 - 1 = 4.
    assert minimum_Length('abcde') == 4

def test_one_character_appears_most_frequently():
    # The string length is 8. 'c' appears 5 times, which is the max occurrence.
    # The function returns 8 - 5 = 3.
    assert minimum_Length('aabbccccc') == 3

def test_empty_string_input():
    # The string length is 0, so max occurrence is 0.
    # The function returns 0 - 0 = 0.
    assert minimum_Length('') == 0

def test_multiple_characters_with_same_max_frequency():
    # The string length is 6. 'a', 'b', and 'c' each appear 2 times, max occurrence is 2.
    # The function returns 6 - 2 = 4.
    assert minimum_Length('aabbcc') == 4

def test_single_character_string():
    # The string length is 1, max occurrence is 1.
    # The function returns 1 - 1 = 0.
    assert minimum_Length('z') == 0

def test_string_with_mixed_frequency_characters():
    # The string length is 12. Each of 'a', 'b', and 'c' appears 4 times, max occurrence is 4.
    # The function returns 12 - 4 = 8.
    assert minimum_Length('abcabcabcabc') == 8