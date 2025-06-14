def count_no (A,N,L,R): 
    count = 0
    for i in range (L,R + 1): 
        if (i % A != 0): 
            count += 1
        if (count == N): 
            break
    return (i)

import pytest

def test_count_first_number_not_divisible_by_3_in_1_to_10():
    # Count the 1st number in range [1, 10] not divisible by 3
    result = count_no(A=3, N=1, L=1, R=10)
    assert result == 1

def test_count_third_number_not_divisible_by_2_in_1_to_10():
    # Count the 3rd number in range [1, 10] not divisible by 2
    result = count_no(A=2, N=3, L=1, R=10)
    assert result == 5

def test_count_fifth_number_not_divisible_by_4_in_10_to_20():
    # Count the 5th number in range [10, 20] not divisible by 4
    result = count_no(A=4, N=5, L=10, R=20)
    assert result == 15

def test_count_seventh_number_not_divisible_by_5_in_1_to_10():
    # Count the 7th number in range [1, 10] not divisible by 5
    result = count_no(A=5, N=7, L=1, R=10)
    assert result == 8

def test_count_second_number_not_divisible_by_1_in_5_to_5():
    # Count the 2nd number in range [5, 5] not divisible by 1
    result = count_no(A=1, N=2, L=5, R=5)
    assert result == 5

def test_count_first_number_not_divisible_by_2_in_10_to_10():
    # Count the 1st number in range [10, 10] not divisible by 2
    result = count_no(A=2, N=1, L=10, R=10)
    assert result == 10

def test_count_fourth_number_not_divisible_by_2_in_1_to_5():
    # Count the 4th number in range [1, 5] not divisible by 2
    result = count_no(A=2, N=4, L=1, R=5)
    assert result == 5