def multiples_of_num(m,n): 
    multiples_of_num= list(range(n,(m+1)*n, n)) 
    return list(multiples_of_num)

import pytest

def test_generate_first_5_multiples_of_3():
    result = multiples_of_num(m=5, n=3)
    expected = [3, 6, 9, 12, 15]
    assert result == expected

def test_generate_first_4_multiples_of_7():
    result = multiples_of_num(m=4, n=7)
    expected = [7, 14, 21, 28]
    assert result == expected

def test_generate_first_1_multiple_of_10():
    result = multiples_of_num(m=1, n=10)
    expected = [10]
    assert result == expected

def test_generate_first_0_multiples_of_5_edge_case():
    result = multiples_of_num(m=0, n=5)
    expected = []
    assert result == expected

def test_generate_first_3_multiples_of_1():
    result = multiples_of_num(m=3, n=1)
    expected = [1, 2, 3]
    assert result == expected

def test_generate_first_6_multiples_of_2():
    result = multiples_of_num(m=6, n=2)
    expected = [2, 4, 6, 8, 10, 12]
    assert result == expected