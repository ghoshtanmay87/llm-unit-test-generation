def profit_amount(actual_cost,sale_amount): 
 if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    return amount
 else:
    return None

import pytest

def test_profit_amount_actual_cost_greater_than_sale_amount():
    # Actual cost is greater than sale amount, resulting in a profit amount
    actual_cost = 150.0
    sale_amount = 100.0
    expected = 50.0
    assert profit_amount(actual_cost, sale_amount) == expected

def test_profit_amount_actual_cost_equal_to_sale_amount():
    # Actual cost is equal to sale amount, no profit amount
    actual_cost = 100.0
    sale_amount = 100.0
    expected = None
    assert profit_amount(actual_cost, sale_amount) is expected

def test_profit_amount_actual_cost_less_than_sale_amount():
    # Actual cost is less than sale amount, no profit amount
    actual_cost = 80.0
    sale_amount = 100.0
    expected = None
    assert profit_amount(actual_cost, sale_amount) is expected

def test_profit_amount_actual_cost_much_greater_than_sale_amount():
    # Actual cost is much greater than sale amount, large profit amount
    actual_cost = 1000.0
    sale_amount = 200.0
    expected = 800.0
    assert profit_amount(actual_cost, sale_amount) == expected

def test_profit_amount_actual_cost_and_sale_amount_zero():
    # Actual cost and sale amount are zero, no profit amount
    actual_cost = 0.0
    sale_amount = 0.0
    expected = None
    assert profit_amount(actual_cost, sale_amount) is expected