def tetrahedral_number(n): 
	return (n * (n + 1) * (n + 2)) / 6

import pytest

def test_tetrahedral_number_n_0():
    # Calculate tetrahedral number for n=0
    result = tetrahedral_number(0)
    assert result == 0.0

def test_tetrahedral_number_n_1():
    # Calculate tetrahedral number for n=1
    result = tetrahedral_number(1)
    assert result == 1.0

def test_tetrahedral_number_n_2():
    # Calculate tetrahedral number for n=2
    result = tetrahedral_number(2)
    assert result == 4.0

def test_tetrahedral_number_n_3():
    # Calculate tetrahedral number for n=3
    result = tetrahedral_number(3)
    assert result == 10.0

def test_tetrahedral_number_n_4():
    # Calculate tetrahedral number for n=4
    result = tetrahedral_number(4)
    assert result == 20.0

def test_tetrahedral_number_n_5():
    # Calculate tetrahedral number for n=5
    result = tetrahedral_number(5)
    assert result == 35.0

def test_tetrahedral_number_n_10():
    # Calculate tetrahedral number for n=10
    result = tetrahedral_number(10)
    assert result == 220.0