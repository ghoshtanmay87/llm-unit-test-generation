def last_Digit_Factorial(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0

import pytest

def test_last_digit_factorial_zero():
    # Input is zero, factorial of 0 is 1
    result = last_Digit_Factorial(0)
    assert result == 1

def test_last_digit_factorial_one():
    # Input is 1, factorial of 1 is 1
    result = last_Digit_Factorial(1)
    assert result == 1

def test_last_digit_factorial_two():
    # Input is 2, factorial of 2 is 2
    result = last_Digit_Factorial(2)
    assert result == 2

def test_last_digit_factorial_three():
    # Input is 3, factorial of 3 is 6
    result = last_Digit_Factorial(3)
    assert result == 6

def test_last_digit_factorial_four():
    # Input is 4, factorial of 4 is 24, last digit is 4
    result = last_Digit_Factorial(4)
    assert result == 4

def test_last_digit_factorial_five():
    # Input is 5, factorial of 5 is 120, last digit is 0
    result = last_Digit_Factorial(5)
    assert result == 0

def test_last_digit_factorial_ten():
    # Input is 10, factorial of 10 ends with 0
    result = last_Digit_Factorial(10)
    assert result == 0

def test_last_digit_factorial_hundred():
    # Input is 100, factorial of 100 ends with 0
    result = last_Digit_Factorial(100)
    assert result == 0