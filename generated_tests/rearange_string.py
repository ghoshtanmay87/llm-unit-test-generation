import heapq
from collections import Counter
def rearange_string(S):
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1: 
        return ""
    ans = []
    while len(heap) >= 2:
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        ans.extend([char1, char2])
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
    return "".join(ans) + (heap[0][1] if heap else "")

import pytest

def test_rearranging_all_unique_characters():
    # Scenario: Rearranging a string with all unique characters
    input_str = 'abc'
    expected = 'abc'
    assert rearange_string(input_str) == expected

def test_rearranging_one_char_repeated_twice_and_one_unique():
    # Scenario: Rearranging a string with one character repeated twice and one unique character
    input_str = 'aab'
    expected = 'aba'
    assert rearange_string(input_str) == expected

def test_rearranging_one_char_too_frequent_to_rearrange():
    # Scenario: Rearranging a string where one character is too frequent to rearrange
    input_str = 'aaab'
    expected = ''
    assert rearange_string(input_str) == expected

def test_rearranging_multiple_chars_balanced_frequencies():
    # Scenario: Rearranging a string with multiple characters and balanced frequencies
    input_str = 'aabbcc'
    expected = 'abcabc'
    assert rearange_string(input_str) == expected

def test_rearranging_one_char_repeated_more_than_half_length():
    # Scenario: Rearranging a string with one character repeated more than half the length
    input_str = 'aaabb'
    expected = 'ababa'
    assert rearange_string(input_str) == expected

def test_rearranging_single_character():
    # Scenario: Rearranging a string with a single character
    input_str = 'z'
    expected = 'z'
    assert rearange_string(input_str) == expected

def test_rearranging_two_identical_characters():
    # Scenario: Rearranging a string with two identical characters
    input_str = 'cc'
    expected = ''
    assert rearange_string(input_str) == expected

def test_rearranging_characters_with_uneven_frequencies():
    # Scenario: Rearranging a string with characters having uneven frequencies
    input_str = 'aaabbc'
    expected = 'ababac'
    assert rearange_string(input_str) == expected