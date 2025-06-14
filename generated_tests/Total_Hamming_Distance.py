def Total_Hamming_Distance(n):   
    i = 1
    sum = 0
    while (n // i > 0):  
        sum = sum + n // i  
        i = i * 2     
    return sum

import pytest

def test_total_hamming_distance_n_0():
    # Calculate total Hamming distance for n=0
    n = 0
    expected = 0
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_1():
    # Calculate total Hamming distance for n=1
    n = 1
    expected = 1
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_2():
    # Calculate total Hamming distance for n=2
    n = 2
    expected = 2
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_3():
    # Calculate total Hamming distance for n=3
    n = 3
    expected = 4
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_4():
    # Calculate total Hamming distance for n=4
    n = 4
    expected = 5
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_5():
    # Calculate total Hamming distance for n=5
    n = 5
    expected = 8
    assert Total_Hamming_Distance(n) == expected

def test_total_hamming_distance_n_10():
    # Calculate total Hamming distance for n=10
    n = 10
    expected = 17
    assert Total_Hamming_Distance(n) == expected