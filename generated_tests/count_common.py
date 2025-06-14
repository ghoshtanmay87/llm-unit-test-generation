from collections import Counter
def count_common(words):
  word_counts = Counter(words)
  top_four = word_counts.most_common(4)
  return (top_four)

import pytest

def test_count_common_more_than_four_unique_words():
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'grape', 'apple', 'kiwi']
    expected = [('banana', 3), ('apple', 3), ('orange', 1), ('grape', 1)]
    assert count_common(words) == expected

def test_count_common_exactly_four_unique_words():
    words = ['cat', 'dog', 'cat', 'bird', 'dog', 'dog', 'fish']
    expected = [('dog', 3), ('cat', 2), ('bird', 1), ('fish', 1)]
    assert count_common(words) == expected

def test_count_common_fewer_than_four_unique_words():
    words = ['red', 'blue', 'red', 'red']
    expected = [('red', 3), ('blue', 1)]
    assert count_common(words) == expected

def test_count_common_empty_list():
    words = []
    expected = []
    assert count_common(words) == expected

def test_count_common_ties_in_frequency():
    words = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
    expected = [('a', 2), ('b', 2), ('c', 2), ('d', 2)]
    assert count_common(words) == expected