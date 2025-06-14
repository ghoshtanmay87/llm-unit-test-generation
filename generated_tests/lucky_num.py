def lucky_num(n):
 List=range(-1,n*n+9,2)
 i=2
 while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
 return List[1:n+1]

import pytest

def test_lucky_num_n_1():
    # Calculate lucky numbers for n=1
    result = lucky_num(1)
    expected = [1]
    assert result == expected, f"Expected {expected} but got {result}"

def test_lucky_num_n_2():
    # Calculate lucky numbers for n=2
    result = lucky_num(2)
    expected = [1, 3]
    assert result == expected, f"Expected {expected} but got {result}"

def test_lucky_num_n_5():
    # Calculate lucky numbers for n=5
    result = lucky_num(5)
    expected = [1, 3, 7, 9, 13]
    assert result == expected, f"Expected {expected} but got {result}"

def test_lucky_num_n_10():
    # Calculate lucky numbers for n=10
    result = lucky_num(10)
    expected = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    assert result == expected, f"Expected {expected} but got {result}"

def test_lucky_num_n_0_edge_case():
    # Calculate lucky numbers for n=0 (edge case)
    result = lucky_num(0)
    expected = []
    assert result == expected, f"Expected {expected} but got {result}"