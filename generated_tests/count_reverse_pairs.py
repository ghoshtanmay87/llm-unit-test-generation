def count_reverse_pairs(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return str(res)

import pytest

def test_count_reverse_pairs_one_pair_of_reversed_strings():
    test_list = ['abc', 'cba', 'xyz']
    expected_output = '2'
    assert count_reverse_pairs(test_list) == expected_output

def test_count_reverse_pairs_palindromic_strings():
    test_list = ['madam', 'adam', 'mada', 'madam']
    expected_output = '3'
    assert count_reverse_pairs(test_list) == expected_output

def test_count_reverse_pairs_no_reverse_pairs():
    test_list = ['abc', 'def', 'ghi']
    expected_output = '0'
    assert count_reverse_pairs(test_list) == expected_output

def test_count_reverse_pairs_repeated_strings_and_reverses():
    test_list = ['ab', 'ba', 'ab', 'ba']
    expected_output = '6'
    assert count_reverse_pairs(test_list) == expected_output

def test_count_reverse_pairs_single_element():
    test_list = ['a']
    expected_output = '1'
    assert count_reverse_pairs(test_list) == expected_output