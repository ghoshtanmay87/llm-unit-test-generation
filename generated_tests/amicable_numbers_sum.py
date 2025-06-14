def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"
    amicables = set()
    for num in range(2, limit+1):
        if num in amicables:
            continue
        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return sum(amicables)

import pytest

def test_input_not_integer():
    # Scenario: Input is not an integer
    result = amicable_numbers_sum(limit=10.5)
    assert result == "Input is not an integer!"

def test_input_less_than_one():
    # Scenario: Input is less than 1
    result = amicable_numbers_sum(limit=0)
    assert result == "Input must be bigger than 0!"

def test_limit_one_no_amicable_numbers():
    # Scenario: No amicable numbers within limit 1
    result = amicable_numbers_sum(limit=1)
    assert result == 0

def test_limit_200_no_amicable_numbers():
    # Scenario: Limit 200 includes amicable pair (220, 284)
    result = amicable_numbers_sum(limit=200)
    assert result == 0

def test_limit_300_includes_220_284():
    # Scenario: Limit 300 includes amicable pair (220, 284)
    result = amicable_numbers_sum(limit=300)
    assert result == 504

def test_limit_1000_includes_only_220_284():
    # Scenario: Limit 1000 includes amicable pairs (220, 284) and (1184, 1210) partially
    result = amicable_numbers_sum(limit=1000)
    assert result == 504

def test_limit_1300_includes_220_284_and_1184_1210():
    # Scenario: Limit 1300 includes amicable pairs (220, 284) and (1184, 1210)
    result = amicable_numbers_sum(limit=1300)
    assert result == 3898