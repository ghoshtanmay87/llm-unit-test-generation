def sequence(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

import pytest

def test_base_case_n_1():
    # For n=1, the function returns 1 directly as per the base case condition.
    assert sequence(1) == 1

def test_base_case_n_2():
    # For n=2, the function returns 1 directly as per the base case condition.
    assert sequence(2) == 1

def test_calculate_sequence_n_3():
    # sequence(3) = sequence(sequence(2)) + sequence(3 - sequence(2)) = sequence(1) + sequence(2) = 1 + 1 = 2.
    assert sequence(3) == 2

def test_calculate_sequence_n_4():
    # sequence(4) = sequence(sequence(3)) + sequence(4 - sequence(3)) = sequence(2) + sequence(2) = 1 + 1 = 2.
    assert sequence(4) == 2

def test_calculate_sequence_n_5():
    # sequence(5) = sequence(sequence(4)) + sequence(5 - sequence(4))
    # From above, sequence(4) = 2
    # So sequence(5) = sequence(2) + sequence(3) = 1 + 2 = 3.
    assert sequence(5) == 3

def test_calculate_sequence_n_6():
    # sequence(6) = sequence(sequence(5)) + sequence(6 - sequence(5))
    # sequence(5) = 3
    # So sequence(6) = sequence(3) + sequence(3) = 2 + 2 = 4.
    assert sequence(6) == 4

def test_calculate_sequence_n_7():
    # sequence(7) = sequence(sequence(6)) + sequence(7 - sequence(6)) = sequence(4) + sequence(3) = 2 + 2 = 4.
    assert sequence(7) == 4

def test_calculate_sequence_n_8():
    # sequence(8) = sequence(sequence(7)) + sequence(8 - sequence(7)) = sequence(4) + sequence(4) = 2 + 2 = 4.
    assert sequence(8) == 4