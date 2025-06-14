def count_duplic(lists):
    element = []
    frequency = []
    if not lists:
        return element
    running_count = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            running_count += 1
        else:
            frequency.append(running_count)
            element.append(lists[i])
            running_count = 1
    frequency.append(running_count)
    element.append(lists[i+1])
    return element,frequency

import pytest

def test_empty_input_list_returns_empty_lists():
    # The function immediately returns empty element and frequency lists when input is empty.
    input_data = []
    expected_output = ([], [])
    assert count_duplic(input_data) == expected_output

def test_single_element_list_returns_element_and_frequency_1():
    # With one element, the loop does not run, but the last element and its count 1 are appended before return.
    input_data = [5]
    expected_output = ([5], [1])
    assert count_duplic(input_data) == expected_output

def test_list_with_all_identical_elements_returns_one_element_and_its_count():
    # All elements are equal, so running_count increments to 4, and only one element 2 with frequency 4 is returned.
    input_data = [2, 2, 2, 2]
    expected_output = ([2], [4])
    assert count_duplic(input_data) == expected_output

def test_list_with_no_duplicates_returns_each_element_with_frequency_1():
    # Each element differs from the next, so frequency 1 is appended for each element.
    input_data = [1, 2, 3, 4]
    expected_output = ([1, 2, 3, 4], [1, 1, 1, 1])
    assert count_duplic(input_data) == expected_output

def test_list_with_mixed_duplicates_returns_correct_elements_and_frequencies():
    # 1 repeats twice, 2 once, 3 thrice, and 4 once, matching the frequency counts.
    input_data = [1, 1, 2, 3, 3, 3, 4]
    expected_output = ([1, 2, 3, 4], [2, 1, 3, 1])
    assert count_duplic(input_data) == expected_output

def test_list_with_duplicates_at_the_end():
    # 5 and 6 appear once, 7 appears three times at the end, frequencies reflect this.
    input_data = [5, 6, 7, 7, 7]
    expected_output = ([5, 6, 7], [1, 1, 3])
    assert count_duplic(input_data) == expected_output