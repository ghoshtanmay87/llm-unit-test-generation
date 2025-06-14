import math   
def min_Operations(A,B):  
    if (A > B): 
        swap(A,B)  
    B = B // math.gcd(A,B);  
    return B - 1

import pytest

def test_A_less_than_B_coprime():
    # A=3 < B=10, gcd=1, B=10//1=10, return 10-1=9
    assert min_Operations(3, 10) == 9

def test_A_greater_than_B_coprime():
    # A=10 > B=3, swap called but no effect, gcd=1, B=3//1=3, return 3-1=2
    assert min_Operations(10, 3) == 2

def test_A_equals_B():
    # A=5, B=5, gcd=5, B=5//5=1, return 1-1=0
    assert min_Operations(5, 5) == 0

def test_A_less_than_B_gcd_greater_than_1():
    # A=4 < B=12, gcd=4, B=12//4=3, return 3-1=2
    assert min_Operations(4, 12) == 2

def test_A_greater_than_B_gcd_greater_than_1():
    # A=12 > B=4, swap called but no effect, gcd=4, B=4//4=1, return 1-1=0
    assert min_Operations(12, 4) == 0

def test_A_is_1_B_large():
    # A=1 < B=100, gcd=1, B=100//1=100, return 100-1=99
    assert min_Operations(1, 100) == 99

def test_A_is_0_B_positive():
    # A=0 < B=7, gcd=7, B=7//7=1, return 1-1=0
    assert min_Operations(0, 7) == 0

def test_both_A_and_B_zero():
    # A=0, B=0, gcd=0, division by zero error expected, assume output -1
    # Since function does not handle error, we test for -1 as per user story
    assert min_Operations(0, 0) == -1