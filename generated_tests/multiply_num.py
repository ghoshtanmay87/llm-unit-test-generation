def multiply_num(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total/len(numbers)

import pytest

def test_multiply_and_average_positive_integers():
    # The product of the numbers is 1*2*3*4 = 24. Dividing by the length 4 gives 24/4 = 6.0.
    result = multiply_num([1, 2, 3, 4])
    assert result == 6.0

def test_multiply_and_average_single_element():
    # The product of the single element is 5. Dividing by length 1 gives 5/1 = 5.0.
    result = multiply_num([5])
    assert result == 5.0

def test_multiply_and_average_list_containing_zero():
    # The product includes zero, so product is 0. Dividing by length 3 gives 0/3 = 0.0.
    result = multiply_num([0, 10, 20])
    assert result == 0.0

def test_multiply_and_average_negative_numbers():
    # Product is (-1)*(-2)*(-3) = -6. Dividing by length 3 gives -6/3 = -2.0.
    # Note: expected_output in user story is 2.0 but reasoning says -2.0.
    # We must trust expected_output as per instructions.
    result = multiply_num([-1, -2, -3])
    assert result == 2.0

def test_multiply_and_average_floats():
    # Product is 1.5*2.0*3.0 = 9.0. Dividing by length 3 gives 9.0/3 = 3.0.
    result = multiply_num([1.5, 2.0, 3.0])
    assert result == 3.0