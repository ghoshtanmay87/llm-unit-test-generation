import math 
def is_polite(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2)))

import pytest

def test_politeness_n_1():
    # n=1, expected output is 5 according to user story
    result = is_polite(1)
    assert result == 5

def test_politeness_n_2():
    # n=2, expected output is 7 according to user story
    result = is_polite(2)
    assert result == 7

def test_politeness_n_3():
    # n=3, expected output is 8 according to user story
    result = is_polite(3)
    assert result == 8

def test_politeness_n_4():
    # n=4, expected output is 10 according to user story
    result = is_polite(4)
    assert result == 10

def test_politeness_n_10():
    # n=10, expected output is 16 according to user story
    result = is_polite(10)
    assert result == 16