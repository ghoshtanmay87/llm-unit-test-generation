def find_platform(arr, dep, n): 
    arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n): 
        if (arr[i] <= dep[j]):           
            plat_needed+= 1
            i+= 1
        elif (arr[i] > dep[j]):           
            plat_needed-= 1
            j+= 1
        if (plat_needed > result):  
            result = plat_needed           
    return result

import pytest

def test_single_train_minimal_input():
    arr = [900]
    dep = [910]
    n = 1
    expected = 1
    assert find_platform(arr, dep, n) == expected

def test_two_trains_no_overlap():
    arr = [900, 940]
    dep = [910, 1200]
    n = 2
    expected = 1
    assert find_platform(arr, dep, n) == expected

def test_two_trains_with_overlap():
    arr = [900, 905]
    dep = [910, 920]
    n = 2
    expected = 2
    assert find_platform(arr, dep, n) == expected

def test_three_trains_partial_overlap():
    arr = [900, 940, 950]
    dep = [910, 1200, 1120]
    n = 3
    expected = 2
    assert find_platform(arr, dep, n) == expected

def test_multiple_trains_all_overlapping():
    arr = [900, 901, 902, 903]
    dep = [910, 911, 912, 913]
    n = 4
    expected = 4
    assert find_platform(arr, dep, n) == expected

def test_trains_arriving_and_departing_same_time():
    arr = [900, 900, 900]
    dep = [900, 900, 900]
    n = 3
    expected = 3
    assert find_platform(arr, dep, n) == expected

def test_trains_staggered_arrivals_and_departures():
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = 6
    expected = 3
    assert find_platform(arr, dep, n) == expected