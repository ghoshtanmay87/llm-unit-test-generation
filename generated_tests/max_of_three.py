def max_of_three(num1,num2,num3): 
    if (num1 >= num2) and (num1 >= num3):
       lnum = num1
    elif (num2 >= num1) and (num2 >= num3):
       lnum = num2
    else:
       lnum = num3
    return lnum

import pytest

def test_max_of_three_num1_largest_distinct():
    # All three numbers are distinct with num1 being the largest
    result = max_of_three(num1=10, num2=5, num3=3)
    assert result == 10

def test_max_of_three_num2_largest_distinct():
    # All three numbers are distinct with num2 being the largest
    result = max_of_three(num1=4, num2=9, num3=7)
    assert result == 9

def test_max_of_three_num3_largest_distinct():
    # All three numbers are distinct with num3 being the largest
    result = max_of_three(num1=1, num2=2, num3=8)
    assert result == 8

def test_max_of_three_num1_num2_equal_largest():
    # Two numbers are equal and largest (num1 and num2 equal and largest)
    result = max_of_three(num1=7, num2=7, num3=5)
    assert result == 7

def test_max_of_three_num2_num3_equal_largest():
    # Two numbers are equal and largest (num2 and num3 equal and largest)
    result = max_of_three(num1=3, num2=6, num3=6)
    assert result == 6

def test_max_of_three_all_equal():
    # All three numbers are equal
    result = max_of_three(num1=5, num2=5, num3=5)
    assert result == 5

def test_max_of_three_negative_numbers_num3_largest():
    # Negative numbers with num3 being the largest
    result = max_of_three(num1=-10, num2=-20, num3=-5)
    assert result == -5

def test_max_of_three_mixed_signs_num1_largest():
    # Mixed positive and negative numbers with num1 being the largest
    result = max_of_three(num1=0, num2=-1, num3=-2)
    assert result == 0