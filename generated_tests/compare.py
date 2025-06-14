def compare(game, guess):
    return [abs(x - y) for x, y in zip(game, guess)]

import pytest

def test_compare_equal_length_positive_integers():
    game = [1, 2, 3]
    guess = [3, 2, 1]
    expected = [2, 0, 2]
    assert compare(game, guess) == expected

def test_compare_lists_with_zeros_and_positive_integers():
    game = [0, 0, 0]
    guess = [0, 1, 2]
    expected = [0, 1, 2]
    assert compare(game, guess) == expected

def test_compare_lists_with_negative_and_positive_integers():
    game = [-1, -2, -3]
    guess = [1, 2, 3]
    expected = [2, 4, 6]
    assert compare(game, guess) == expected

def test_compare_lists_with_floating_point_numbers():
    game = [1.5, 2.5, 3.5]
    guess = [1.0, 3.0, 2.0]
    expected = [0.5, 0.5, 1.5]
    assert compare(game, guess) == expected

def test_compare_lists_different_lengths_extra_elements_ignored():
    game = [1, 2, 3, 4]
    guess = [4, 3, 2]
    expected = [3, 1, 1]
    assert compare(game, guess) == expected