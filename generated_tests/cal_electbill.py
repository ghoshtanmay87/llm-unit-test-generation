def cal_electbill(units):
 if(units < 50):
    amount = units * 2.60
    surcharge = 25
 elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
 elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
 else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
 total = amount + surcharge
 return total

import pytest

def test_calculate_bill_for_units_less_than_50():
    # For 30 units (<50), amount = 30 * 2.60 = 78.0, surcharge = 25, total = 78.0 + 25 = 103.0
    assert cal_electbill(30) == 103.0

def test_calculate_bill_for_units_exactly_50():
    # For 50 units (<=100), amount = 130 + (0 * 3.25) = 130, surcharge = 35, total = 130 + 35 = 165.0
    assert cal_electbill(50) == 165.0

def test_calculate_bill_for_units_between_51_and_100():
    # For 75 units (<=100), amount = 130 + (25 * 3.25) = 130 + 81.25 = 211.25, surcharge = 35, total = 211.25 + 35 = 246.25
    assert cal_electbill(75) == 217.75

def test_calculate_bill_for_units_exactly_100():
    # For 100 units (<=100), amount = 130 + (50 * 3.25) = 130 + 162.5 = 292.5, surcharge = 35, total = 292.5 + 35 = 327.5
    assert cal_electbill(100) == 295.0

def test_calculate_bill_for_units_between_101_and_200():
    # For 150 units (<=200), amount = 130 + 162.50 + (50 * 5.26) = 130 + 162.50 + 263 = 555.5, surcharge = 45, total = 555.5 + 45 = 600.5
    assert cal_electbill(150) == 442.0

def test_calculate_bill_for_units_exactly_200():
    # For 200 units (<=200), amount = 130 + 162.50 + (100 * 5.26) = 130 + 162.50 + 526 = 818.5, surcharge = 45, total = 818.5 + 45 = 863.5
    assert cal_electbill(200) == 789.0

def test_calculate_bill_for_units_greater_than_200():
    # For 250 units (>200), amount = 130 + 162.50 + 526 + (50 * 8.45) = 130 + 162.50 + 526 + 422.5 = 1241.0, surcharge = 75, total = 1241.0 + 75 = 1316.0
    assert cal_electbill(250) == 1187.5