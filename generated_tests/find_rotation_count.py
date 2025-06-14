def find_rotation_count(A):
    (left, right) = (0, len(A) - 1)
    while left <= right:
        if A[left] <= A[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % len(A)
        prev = (mid - 1 + len(A)) % len(A)
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        elif A[mid] <= A[right]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = mid + 1
    return -1

import pytest

def test_array_not_rotated_at_all():
    A = [1, 2, 3, 4, 5]
    expected_output = 0
    assert find_rotation_count(A) == expected_output

def test_array_rotated_2_times():
    A = [4, 5, 1, 2, 3]
    expected_output = 2
    assert find_rotation_count(A) == expected_output

def test_array_rotated_4_times_one_less_than_length():
    A = [2, 3, 4, 5, 1]
    expected_output = 4
    assert find_rotation_count(A) == expected_output

def test_array_rotated_1_time():
    A = [5, 1, 2, 3, 4]
    expected_output = 1
    assert find_rotation_count(A) == expected_output

def test_array_rotated_3_times():
    A = [3, 4, 5, 1, 2]
    expected_output = 3
    assert find_rotation_count(A) == expected_output

def test_single_element_array():
    A = [10]
    expected_output = 0
    assert find_rotation_count(A) == expected_output

def test_array_rotated_half_its_length():
    A = [4, 5, 6, 7, 1, 2, 3]
    expected_output = 4
    assert find_rotation_count(A) == expected_output

def test_array_rotated_0_times_with_duplicates_at_ends():
    A = [1, 1, 1, 1, 1]
    expected_output = 0
    assert find_rotation_count(A) == expected_output