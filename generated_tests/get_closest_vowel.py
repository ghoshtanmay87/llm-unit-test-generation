def get_closest_vowel(word):
    if len(word) < 3:
        return ''
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I'}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i + 1] not in vowels and word[i - 1] not in vowels:
                return word[i]
    return ''

import pytest

def test_word_shorter_than_three_characters_returns_empty_string():
    assert get_closest_vowel('at') == ''

def test_find_vowel_with_non_vowel_neighbors_near_end_of_word():
    assert get_closest_vowel('bake') == 'a'

def test_no_vowel_with_non_vowel_neighbors_returns_empty_string():
    assert get_closest_vowel('aeiou') == ''

def test_vowel_at_index_2_with_non_vowel_neighbors_returns_that_vowel():
    assert get_closest_vowel('catnip') == 'i'

def test_vowel_at_index_1_with_non_vowel_neighbors_returns_that_vowel():
    assert get_closest_vowel('bake') == 'a'

def test_uppercase_vowel_with_non_vowel_neighbors_is_recognized_and_returned():
    assert get_closest_vowel('bAkE') == 'A'

def test_vowel_at_index_3_with_non_vowel_neighbors_returns_that_vowel():
    assert get_closest_vowel('strong') == 'o'

def test_no_vowel_with_non_vowel_neighbors_in_word_with_vowels_at_edges():
    assert get_closest_vowel('apple') == ''

def test_vowel_surrounded_by_vowels_does_not_qualify():
    assert get_closest_vowel('aei') == ''