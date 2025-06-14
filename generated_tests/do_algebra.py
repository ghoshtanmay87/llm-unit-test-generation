def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)

import pytest

def test_single_addition_operation():
    # The expression constructed is '2+3'. Evaluating this yields 5.
    operator = ['+']
    operand = [2, 3]
    expected_output = 5
    assert do_algebra(operator, operand) == expected_output

def test_multiple_operations_with_addition_and_multiplication():
    # The expression constructed is '2+3*4'. According to operator precedence, 3*4=12, then 2+12=14.
    operator = ['+', '*']
    operand = [2, 3, 4]
    expected_output = 14
    assert do_algebra(operator, operand) == expected_output

def test_subtraction_and_division_operations():
    # The expression constructed is '10-4/2'. Division first: 4/2=2, then 10-2=8.
    operator = ['-', '/']
    operand = [10, 4, 2]
    expected_output = 8
    assert do_algebra(operator, operand) == expected_output

def test_single_multiplication_operation():
    # The expression constructed is '5*6'. Evaluating this yields 30.
    operator = ['*']
    operand = [5, 6]
    expected_output = 30
    assert do_algebra(operator, operand) == expected_output

def test_no_operators_single_operand():
    # With no operators, the expression is just '7'. Evaluating this yields 7.
    operator = []
    operand = [7]
    expected_output = 7
    assert do_algebra(operator, operand) == expected_output