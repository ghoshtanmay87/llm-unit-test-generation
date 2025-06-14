def first_Factorial_Divisible_Number(x): 
    i = 1;
    fact = 1; 
    for i in range(1,x): 
        fact = fact * i 
        if (fact % x == 0): 
            break
    return i

import pytest

def test_first_factorial_divisible_number_x_1():
    # Find the first number i where i! is divisible by x=1
    x = 1
    expected_output = 1
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_2():
    # Find the first number i where i! is divisible by x=2
    x = 2
    expected_output = 1
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_3():
    # Find the first number i where i! is divisible by x=3
    x = 3
    expected_output = 2
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_4():
    # Find the first number i where i! is divisible by x=4
    x = 4
    expected_output = 3
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_5():
    # Find the first number i where i! is divisible by x=5
    x = 5
    expected_output = 4
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_6():
    # Find the first number i where i! is divisible by x=6
    x = 6
    expected_output = 3
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_7():
    # Find the first number i where i! is divisible by x=7
    x = 7
    expected_output = 6
    assert first_Factorial_Divisible_Number(x) == expected_output

def test_first_factorial_divisible_number_x_10():
    # Find the first number i where i! is divisible by x=10
    x = 10
    expected_output = 5
    assert first_Factorial_Divisible_Number(x) == expected_output