def noprofit_noloss(actual_cost,sale_amount): 
  if(sale_amount == actual_cost):
    return True
  else:
    return False

import pytest

def test_sale_amount_equals_actual_cost():
    # Since sale_amount equals actual_cost, the function returns True indicating no profit no loss.
    actual_cost = 100.0
    sale_amount = 100.0
    assert noprofit_noloss(actual_cost, sale_amount) is True

def test_sale_amount_greater_than_actual_cost_profit_scenario():
    # Sale amount is greater than actual cost, so the function returns False indicating profit, not no profit no loss.
    actual_cost = 100.0
    sale_amount = 150.0
    assert noprofit_noloss(actual_cost, sale_amount) is False

def test_sale_amount_less_than_actual_cost_loss_scenario():
    # Sale amount is less than actual cost, so the function returns False indicating loss, not no profit no loss.
    actual_cost = 200.0
    sale_amount = 150.0
    assert noprofit_noloss(actual_cost, sale_amount) is False

def test_both_actual_cost_and_sale_amount_zero():
    # Both values are equal (zero), so the function returns True indicating no profit no loss.
    actual_cost = 0.0
    sale_amount = 0.0
    assert noprofit_noloss(actual_cost, sale_amount) is True

def test_sale_amount_and_actual_cost_negative_but_equal():
    # Sale amount equals actual cost even though both are negative, so the function returns True indicating no profit no loss.
    actual_cost = -50.0
    sale_amount = -50.0
    assert noprofit_noloss(actual_cost, sale_amount) is True