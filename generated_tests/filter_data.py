def filter_data(students,h,w):
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result

import pytest

def test_filter_students_height_and_weight_above_or_equal_thresholds():
    students = {'Alice': [170, 65], 'Bob': [160, 70], 'Charlie': [180, 60]}
    h = 165
    w = 60
    expected_output = {'Alice': [170, 65], 'Charlie': [180, 60]}
    assert filter_data(students, h, w) == expected_output

def test_no_students_meet_height_and_weight_criteria():
    students = {'Dave': [150, 50], 'Eve': [155, 55]}
    h = 160
    w = 60
    expected_output = {}
    assert filter_data(students, h, w) == expected_output

def test_all_students_meet_height_and_weight_criteria():
    students = {'Frank': [180, 80], 'Grace': [175, 70]}
    h = 170
    w = 60
    expected_output = {'Frank': [180, 80], 'Grace': [175, 70]}
    assert filter_data(students, h, w) == expected_output

def test_students_meet_height_but_not_weight_criteria():
    students = {'Hank': [180, 55], 'Ivy': [175, 59]}
    h = 170
    w = 60
    expected_output = {}
    assert filter_data(students, h, w) == expected_output

def test_students_meet_weight_but_not_height_criteria():
    students = {'Jack': [165, 65], 'Kara': [160, 70]}
    h = 170
    w = 60
    expected_output = {}
    assert filter_data(students, h, w) == expected_output

def test_empty_students_dictionary():
    students = {}
    h = 170
    w = 60
    expected_output = {}
    assert filter_data(students, h, w) == expected_output

def test_thresholds_zero_all_students_included():
    students = {'Liam': [150, 50], 'Mia': [160, 55]}
    h = 0
    w = 0
    expected_output = {'Liam': [150, 50], 'Mia': [160, 55]}
    assert filter_data(students, h, w) == expected_output