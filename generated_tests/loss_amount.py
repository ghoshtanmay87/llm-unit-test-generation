def loss_amount(actual_cost,sale_amount): 
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return None

import pytest

def test_loss_amount_sale_greater_than_actual_cost():
    # Sale amount is greater than actual cost, resulting in a positive loss amount
    actual_cost = 100.0
    sale_amount = 150.0
    expected = 50.0
    assert loss_amount(actual_cost, sale_amount) == expected

def test_loss_amount_sale_equal_to_actual_cost():
    # Sale amount is equal to actual cost, resulting in no loss amount
    actual_cost = 200.0
    sale_amount = 200.0
    expected = None
    assert loss_amount(actual_cost, sale_amount) is expected

def test_loss_amount_sale_less_than_actual_cost():
    # Sale amount is less than actual cost, resulting in no loss amount
    actual_cost = 300.0
    sale_amount = 250.0
    expected = None
    assert loss_amount(actual_cost, sale_amount) is expected

def test_loss_amount_sale_just_slightly_greater_than_actual_cost():
    # Sale amount just slightly greater than actual cost
    actual_cost = 99.99
    sale_amount = 100.0
    expected = 0.01
    assert loss_amount(actual_cost, sale_amount) == expected

def test_loss_amount_both_zero():
    # Both sale amount and actual cost are zero
    actual_cost = 0.0
    sale_amount = 0.0
    expected = None
    assert loss_amount(actual_cost, sale_amount) is expected