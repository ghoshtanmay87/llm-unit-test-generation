from collections import Counter 
	
def second_frequent(input): 
	dict = Counter(input) 
	value = sorted(dict.values(), reverse=True)  
	second_large = value[1] 
	for (key, val) in dict.items(): 
		if val == second_large: 
			return (key)

import pytest

def test_list_with_multiple_elements_distinct_frequencies():
    # Frequencies: {1:1, 2:2, 3:3, 4:4}
    # Sorted frequencies descending: [4, 3, 2, 1]
    # Second largest frequency is 3, corresponding to key 3
    assert second_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 3

def test_list_with_two_elements_same_highest_frequency():
    # Frequencies: {5:2, 6:2, 7:1}
    # Sorted frequencies descending: [2, 2, 1]
    # Second largest frequency is 2
    # The function returns the first key with frequency 2, which is 5
    assert second_frequent([5, 5, 6, 6, 7]) == 5

def test_list_with_all_elements_same_frequency():
    # Frequencies: {8:1, 9:1, 10:1}
    # Sorted frequencies descending: [1, 1, 1]
    # Second largest frequency is 1
    # The function returns the first key with frequency 1, which is 8
    assert second_frequent([8, 9, 10]) == 8

def test_list_with_only_one_element():
    # Frequencies: {42:1}
    # Sorted frequencies descending: [1]
    # No second largest frequency, function will raise IndexError or fail
    # Expected output is None (undefined)
    # We test that the function raises IndexError
    with pytest.raises(IndexError):
        second_frequent([42])

def test_list_with_two_elements_different_frequencies():
    # Frequencies: {1:2, 2:1}
    # Sorted frequencies descending: [2, 1]
    # Second largest frequency is 1, corresponding to key 2
    assert second_frequent([1, 1, 2]) == 2