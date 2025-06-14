from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

import pytest

def test_no_operations_balance_never_below_zero():
    operations = []
    expected = False
    assert below_zero(operations) == expected

def test_single_positive_operation_balance_stays_above_zero():
    operations = [5]
    expected = False
    assert below_zero(operations) == expected

def test_single_negative_operation_balance_below_zero_immediately():
    operations = [-1]
    expected = True
    assert below_zero(operations) == expected

def test_multiple_operations_balance_dips_below_zero_after_some_steps():
    operations = [3, -4, 2]
    expected = True
    assert below_zero(operations) == expected

def test_multiple_operations_balance_never_below_zero():
    operations = [2, 3, -1, 1]
    expected = False
    assert below_zero(operations) == expected

def test_balance_goes_below_zero_late_in_operations():
    operations = [10, -5, -3, -4]
    expected = True
    assert below_zero(operations) == expected

def test_balance_exactly_zero_after_each_operation_never_below_zero():
    operations = [1, -1, 2, -2]
    expected = False
    assert below_zero(operations) == expected

def test_multiple_negative_operations_balance_never_below_zero():
    operations = [5, -2, -3]
    expected = False
    assert below_zero(operations) == expected

def test_first_operation_zero_second_operation_negative_causing_below_zero():
    operations = [0, -1]
    expected = True
    assert below_zero(operations) == expected