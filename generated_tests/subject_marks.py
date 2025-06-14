def subject_marks(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[1])
 return subjectmarks

import pytest

def test_sorting_subject_marks_in_ascending_order():
    input_data = {'subjectmarks': [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]}
    expected_output = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    assert subject_marks(**input_data) == expected_output

def test_sorting_subject_marks_with_identical_scores():
    input_data = {'subjectmarks': [('Social sciences', 82), ('English', 88), ('Maths', 88), ('Science', 90)]}
    expected_output = [('Social sciences', 82), ('English', 88), ('Maths', 88), ('Science', 90)]
    assert subject_marks(**input_data) == expected_output

def test_sorting_subject_marks_with_all_subjects_having_same_score():
    input_data = {'subjectmarks': [('English', 90), ('Maths', 90), ('Science', 90), ('Social sciences', 90)]}
    expected_output = [('English', 90), ('Maths', 90), ('Science', 90), ('Social sciences', 90)]
    assert subject_marks(**input_data) == expected_output

def test_sorting_subject_marks_with_single_subject():
    input_data = {'subjectmarks': [('English', 95)]}
    expected_output = [('English', 95)]
    assert subject_marks(**input_data) == expected_output

def test_sorting_subject_marks_with_no_subjects():
    input_data = {'subjectmarks': []}
    expected_output = []
    assert subject_marks(**input_data) == expected_output