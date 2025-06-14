def find_demlo(s): 
	l = len(s) 
	res = "" 
	for i in range(1,l+1): 
		res = res + str(i) 
	for i in range(l-1,0,-1): 
		res = res + str(i) 
	return res

import pytest

def test_find_demlo_empty_string():
    # Input is an empty string
    s = ''
    expected = ''
    assert find_demlo(s) == expected

def test_find_demlo_length_1():
    # Input string of length 1
    s = 'a'
    expected = '1'
    assert find_demlo(s) == expected

def test_find_demlo_length_2():
    # Input string of length 2
    s = 'ab'
    expected = '121'
    assert find_demlo(s) == expected

def test_find_demlo_length_3():
    # Input string of length 3
    s = 'abc'
    expected = '12321'
    assert find_demlo(s) == expected

def test_find_demlo_length_5():
    # Input string of length 5
    s = 'hello'
    expected = '123454321'
    assert find_demlo(s) == expected