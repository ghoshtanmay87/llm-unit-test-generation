def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))

import pytest

def test_m_less_than_n_should_return_minus_one():
    # Since m (3) is less than n (5), the function immediately returns -1.
    assert rounded_avg(5, 3) == -1

def test_n_equals_m_single_number_average():
    # Only one number (4) in the range. Average is 4. Rounded average is 4. Binary representation is '0b100'.
    assert rounded_avg(4, 4) == '0b100'

def test_range_1_to_3_average_is_2():
    # Sum of numbers 1+2+3=6. Count is 3. Average is 6/3=2. Rounded average is 2. Binary is '0b10'.
    assert rounded_avg(1, 3) == '0b10'

def test_range_2_to_5_average_is_3_point_5_rounded_to_4():
    # Sum is 2+3+4+5=14. Count is 4. Average is 14/4=3.5. Rounded average is 4. Binary is '0b100'.
    assert rounded_avg(2, 5) == '0b100'

def test_range_0_to_0_single_number_zero():
    # Only one number 0. Average is 0. Rounded average is 0. Binary is '0b0'.
    assert rounded_avg(0, 0) == '0b0'

def test_range_10_to_12_average_is_11():
    # Sum is 10+11+12=33. Count is 3. Average is 11. Rounded average is 11. Binary is '0b1011'.
    assert rounded_avg(10, 12) == '0b1011'

def test_range_3_to_7_average_is_5():
    # Sum is 3+4+5+6+7=25. Count is 5. Average is 5. Rounded average is 5. Binary is '0b101'.
    assert rounded_avg(3, 7) == '0b101'