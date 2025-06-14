def get_Number(n, k): 
    arr = [0] * n; 
    i = 0; 
    odd = 1; 
    while (odd <= n):   
        arr[i] = odd; 
        i += 1; 
        odd += 2;
    even = 2; 
    while (even <= n): 
        arr[i] = even; 
        i += 1;
        even += 2; 
    return arr[k - 1];

import pytest

def test_retrieve_1st_element_n_5():
    # The array is [1, 3, 5, 2, 4], 1st element is 1
    assert get_Number(5, 1) == 1

def test_retrieve_3rd_element_n_5():
    # The array is [1, 3, 5, 2, 4], 3rd element is 5
    assert get_Number(5, 3) == 5

def test_retrieve_5th_element_n_5():
    # The array is [1, 3, 5, 2, 4], 5th element is 4
    assert get_Number(5, 5) == 4

def test_retrieve_4th_element_n_6():
    # The array is [1, 3, 5, 2, 4, 6], 4th element is 2
    assert get_Number(6, 4) == 2

def test_retrieve_6th_element_n_6():
    # The array is [1, 3, 5, 2, 4, 6], 6th element is 6
    assert get_Number(6, 6) == 6

def test_retrieve_1st_element_n_1():
    # The array is [1], 1st element is 1
    assert get_Number(1, 1) == 1

def test_retrieve_7th_element_n_10():
    # The array is [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], 7th element is 4
    assert get_Number(10, 7) == 4

def test_retrieve_10th_element_n_10():
    # The array is [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], 10th element is 10
    assert get_Number(10, 10) == 10