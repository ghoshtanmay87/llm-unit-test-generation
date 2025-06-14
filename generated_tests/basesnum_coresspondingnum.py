def basesnum_coresspondingnum(bases_num,index):
  result = list(map(pow, bases_num, index))
  return result

import pytest

def test_powers_equal_length_lists_positive_integers():
    # Calculate powers for equal length lists with positive integers
    bases_num = [2, 3, 4]
    index = [3, 2, 1]
    expected_output = [8, 9, 4]
    assert basesnum_coresspondingnum(bases_num, index) == expected_output

def test_powers_with_zero_exponents():
    # Calculate powers with zero exponents
    bases_num = [5, 10, 7]
    index = [0, 0, 0]
    expected_output = [1, 1, 1]
    assert basesnum_coresspondingnum(bases_num, index) == expected_output

def test_powers_mixed_bases_and_exponents_including_one():
    # Calculate powers with mixed bases and exponents including 1
    bases_num = [9, 2, 5]
    index = [2, 1, 3]
    expected_output = [81, 2, 125]
    assert basesnum_coresspondingnum(bases_num, index) == expected_output

def test_powers_single_element_lists():
    # Calculate powers with bases and exponents as single-element lists
    bases_num = [7]
    index = [4]
    expected_output = [2401]
    assert basesnum_coresspondingnum(bases_num, index) == expected_output

def test_powers_bases_and_exponents_including_zero_base():
    # Calculate powers with bases and exponents including zero base
    bases_num = [0, 1, 2]
    index = [5, 3, 0]
    expected_output = [0, 1, 1]
    assert basesnum_coresspondingnum(bases_num, index) == expected_output