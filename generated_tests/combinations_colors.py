from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))

import pytest

def test_combinations_two_colors_three_list():
    # Generate all combinations with replacement of 2 colors from a list of 3 colors
    input_list = ['red', 'green', 'blue']
    n = 2
    expected = [
        ('red', 'red'), ('red', 'green'), ('red', 'blue'),
        ('green', 'green'), ('green', 'blue'), ('blue', 'blue')
    ]
    assert combinations_colors(input_list, n) == expected

def test_combinations_one_color_two_list():
    # Generate all combinations with replacement of 1 color from a list of 2 colors
    input_list = ['yellow', 'purple']
    n = 1
    expected = [('yellow',), ('purple',)]
    assert combinations_colors(input_list, n) == expected

def test_combinations_three_colors_two_list():
    # Generate all combinations with replacement of 3 colors from a list of 2 colors
    input_list = ['black', 'white']
    n = 3
    expected = [
        ('black', 'black', 'black'),
        ('black', 'black', 'white'),
        ('black', 'white', 'white'),
        ('white', 'white', 'white')
    ]
    assert combinations_colors(input_list, n) == expected

def test_combinations_zero_colors_three_list():
    # Generate all combinations with replacement of 0 colors from a list of 3 colors
    input_list = ['red', 'green', 'blue']
    n = 0
    expected = [()]
    assert combinations_colors(input_list, n) == expected

def test_combinations_two_colors_one_list():
    # Generate all combinations with replacement of 2 colors from a list with one color
    input_list = ['orange']
    n = 2
    expected = [('orange', 'orange')]
    assert combinations_colors(input_list, n) == expected