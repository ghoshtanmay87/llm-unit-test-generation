def sum_range_list(list1, m, n):                                                                                                                                                                                                
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += list1[i]                                                                                                                                                                                                  
    return sum_range

import pytest

def test_sum_elements_index_0_to_2_positive_integers():
    # Sum elements at indices 0, 1, and 2: 1 + 2 + 3 = 6
    result = sum_range_list([1, 2, 3, 4, 5], 0, 2)
    assert result == 6

def test_sum_elements_index_1_to_3_positive_integers():
    # Sum elements at indices 1, 2, and 3: 20 + 30 + 40 = 90
    result = sum_range_list([10, 20, 30, 40, 50], 1, 3)
    assert result == 90

def test_sum_single_element_when_m_equals_n():
    # Sum only the element at index 2: 15
    result = sum_range_list([5, 10, 15, 20], 2, 2)
    assert result == 15

def test_sum_elements_index_0_to_last_index():
    # Sum all elements: 3 + 6 + 9 + 12 = 30
    result = sum_range_list([3, 6, 9, 12], 0, 3)
    assert result == 30

def test_sum_elements_with_negative_and_positive_numbers():
    # Sum elements at indices 1, 2, and 3: 2 + (-3) + 4 = 3
    result = sum_range_list([-1, 2, -3, 4, -5], 1, 3)
    assert result == 3