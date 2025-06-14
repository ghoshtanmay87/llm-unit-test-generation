def min_val(listval):
     min_val = min(i for i in listval if isinstance(i, int))
     return min_val

import pytest

def test_list_with_multiple_integers_and_other_types():
    # The function filters only integers: 3, 1, 4, 2. The minimum integer among these is 1.
    input_data = [3, 1, 4, 'a', 2]
    expected = 1
    assert min_val(input_data) == expected

def test_list_with_negative_and_positive_integers():
    # All elements are integers. The minimum integer is -5.
    input_data = [-5, 0, 7, 3]
    expected = -5
    assert min_val(input_data) == expected

def test_list_with_integers_and_floats():
    # Only integers 3 and 4 are considered. The minimum integer is 3.
    input_data = [2.5, 3, 1.1, 4]
    expected = 3
    assert min_val(input_data) == expected

def test_list_with_only_one_integer():
    # Only one integer 10 is present, so it is the minimum.
    input_data = ['x', 10, 3.5, None]
    expected = 10
    assert min_val(input_data) == expected

def test_list_with_all_non_integers_raises_value_error():
    # No integers in the list, so min() raises ValueError.
    input_data = ['a', 2.2, None, 'b']
    with pytest.raises(ValueError):
        min_val(input_data)

def test_list_with_integers_and_booleans():
    # Booleans are instances of int: True==1, False==0. Minimum is False (0).
    input_data = [True, False, 2, 3]
    expected = False
    assert min_val(input_data) == expected

def test_list_with_large_integers():
    # All elements are integers. The minimum integer is 999.
    input_data = [1000, 5000, 999, 10000]
    expected = 999
    assert min_val(input_data) == expected