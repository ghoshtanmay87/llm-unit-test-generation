def numerical_letter_grade(grades):
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append('A+')
        elif gpa > 3.7:
            letter_grade.append('A')
        elif gpa > 3.3:
            letter_grade.append('A-')
        elif gpa > 3.0:
            letter_grade.append('B+')
        elif gpa > 2.7:
            letter_grade.append('B')
        elif gpa > 2.3:
            letter_grade.append('B-')
        elif gpa > 2.0:
            letter_grade.append('C+')
        elif gpa > 1.7:
            letter_grade.append('C')
        elif gpa > 1.3:
            letter_grade.append('C-')
        elif gpa > 1.0:
            letter_grade.append('D+')
        elif gpa > 0.7:
            letter_grade.append('D')
        elif gpa > 0.0:
            letter_grade.append('D-')
        else:
            letter_grade.append('E')
    return letter_grade

import pytest

def test_exact_4_0_gpa_returns_A_plus():
    grades = [4.0]
    expected = ['A+']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_3_7_returns_A():
    grades = [3.8]
    expected = ['A']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_3_7_returns_A_minus():
    grades = [3.7]
    expected = ['A-']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_3_0_returns_B_plus():
    grades = [3.1]
    expected = ['B+']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_3_0_returns_B():
    grades = [3.0]
    expected = ['B']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_2_3_returns_B_minus():
    grades = [2.4]
    expected = ['B-']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_2_3_returns_C_plus():
    grades = [2.3]
    expected = ['C+']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_1_7_returns_C():
    grades = [1.8]
    expected = ['C']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_1_7_returns_C_minus():
    grades = [1.7]
    expected = ['C-']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_1_0_returns_D_plus():
    grades = [1.1]
    expected = ['D+']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_1_0_returns_D():
    grades = [1.0]
    expected = ['D']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_0_7_returns_D():
    grades = [0.8]
    expected = ['D']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_0_7_returns_D_minus():
    grades = [0.7]
    expected = ['D-']
    assert numerical_letter_grade(grades) == expected

def test_gpa_just_above_0_0_returns_D_minus():
    grades = [0.1]
    expected = ['D-']
    assert numerical_letter_grade(grades) == expected

def test_gpa_exactly_0_0_returns_E():
    grades = [0.0]
    expected = ['E']
    assert numerical_letter_grade(grades) == expected

def test_gpa_below_0_0_returns_E():
    grades = [-0.5]
    expected = ['E']
    assert numerical_letter_grade(grades) == expected

def test_multiple_gpas_with_mixed_values():
    grades = [4.0, 3.5, 2.9, 1.5, 0.5, 0.0]
    expected = ['A+', 'A-', 'B', 'C-', 'D-', 'E']
    assert numerical_letter_grade(grades) == expected