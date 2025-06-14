def sorted_models(models):
 sorted_models = sorted(models, key = lambda x: x['color'])
 return sorted_models

import pytest

def test_sort_models_by_color_distinct_strings():
    models = [
        {'name': 'ModelA', 'color': 'red'},
        {'name': 'ModelB', 'color': 'blue'},
        {'name': 'ModelC', 'color': 'green'}
    ]
    expected = [
        {'name': 'ModelB', 'color': 'blue'},
        {'name': 'ModelC', 'color': 'green'},
        {'name': 'ModelA', 'color': 'red'}
    ]
    assert sorted_models(models) == expected

def test_sort_models_by_color_with_duplicate_colors():
    models = [
        {'name': 'ModelX', 'color': 'yellow'},
        {'name': 'ModelY', 'color': 'yellow'},
        {'name': 'ModelZ', 'color': 'black'}
    ]
    expected = [
        {'name': 'ModelZ', 'color': 'black'},
        {'name': 'ModelX', 'color': 'yellow'},
        {'name': 'ModelY', 'color': 'yellow'}
    ]
    assert sorted_models(models) == expected

def test_sort_models_by_color_mixed_case_colors():
    models = [
        {'name': 'Model1', 'color': 'Blue'},
        {'name': 'Model2', 'color': 'blue'},
        {'name': 'Model3', 'color': 'Apple'}
    ]
    expected = [
        {'name': 'Model3', 'color': 'Apple'},
        {'name': 'Model1', 'color': 'Blue'},
        {'name': 'Model2', 'color': 'blue'}
    ]
    assert sorted_models(models) == expected

def test_sort_models_by_color_empty_list():
    models = []
    expected = []
    assert sorted_models(models) == expected

def test_sort_models_by_color_all_identical_colors():
    models = [
        {'name': 'ModelA', 'color': 'gray'},
        {'name': 'ModelB', 'color': 'gray'},
        {'name': 'ModelC', 'color': 'gray'}
    ]
    expected = [
        {'name': 'ModelA', 'color': 'gray'},
        {'name': 'ModelB', 'color': 'gray'},
        {'name': 'ModelC', 'color': 'gray'}
    ]
    assert sorted_models(models) == expected