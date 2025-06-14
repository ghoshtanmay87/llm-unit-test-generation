def max_profit(price, k):
    n = len(price)
    final_profit = [[None for x in range(n)] for y in range(k + 1)]
    for i in range(k + 1):
        for j in range(n):
            if i == 0 or j == 0:
                final_profit[i][j] = 0
            else:
                max_so_far = 0
                for x in range(j):
                    curr_price = price[j] - price[x] + final_profit[i-1][x]
                    if max_so_far < curr_price:
                        max_so_far = curr_price
                final_profit[i][j] = max(final_profit[i][j-1], max_so_far)
    return final_profit[k][n-1]

import pytest

def test_no_transactions_allowed_with_multiple_prices():
    # No transactions allowed (k=0) with multiple prices
    price = [10, 22, 5, 75, 65, 80]
    k = 0
    expected_output = 0
    assert max_profit(price, k) == expected_output

def test_single_transaction_allowed_with_increasing_and_decreasing_prices():
    # Single transaction allowed (k=1) with increasing and decreasing prices
    price = [10, 22, 5, 75, 65, 80]
    k = 1
    expected_output = 75
    assert max_profit(price, k) == expected_output

def test_two_transactions_allowed_with_multiple_price_peaks():
    # Two transactions allowed (k=2) with multiple price peaks
    price = [12, 14, 17, 10, 14, 13, 12, 15]
    k = 2
    expected_output = 10
    assert max_profit(price, k) == expected_output

def test_multiple_transactions_allowed_with_fluctuating_prices():
    # Multiple transactions allowed (k=3) with fluctuating prices
    price = [100, 180, 260, 310, 40, 535, 695]
    k = 3
    expected_output = 865
    assert max_profit(price, k) == expected_output

def test_single_day_price_list_with_any_k():
    # Single day price list (n=1) with any k
    price = [50]
    k = 5
    expected_output = 0
    assert max_profit(price, k) == expected_output

def test_prices_always_decreasing_with_multiple_transactions_allowed():
    # Prices always decreasing with multiple transactions allowed
    price = [100, 90, 80, 70, 60]
    k = 3
    expected_output = 0
    assert max_profit(price, k) == expected_output

def test_two_transactions_allowed_with_prices_having_multiple_peaks_and_valleys():
    # Two transactions allowed with prices having multiple peaks and valleys
    price = [3, 2, 6, 5, 0, 3]
    k = 2
    expected_output = 7
    assert max_profit(price, k) == expected_output