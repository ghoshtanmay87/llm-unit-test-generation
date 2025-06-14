def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)

import pytest

def test_max_val_multiple_integers():
    # List with multiple integers and no other types
    input_data = [1, 3, 2, 5, 4]
    expected = 5
    assert max_val(input_data) == expected

def test_max_val_integers_and_strings():
    # List with integers and strings mixed
    input_data = [1, 'a', 3, 'b', 2]
    expected = 3
    assert max_val(input_data) == expected

def test_max_val_negative_and_positive_integers():
    # List with negative and positive integers
    input_data = [-10, -5, 0, 5, 10]
    expected = 10
    assert max_val(input_data) == expected

def test_max_val_integers_and_floats():
    # List with integers and floats
    input_data = [1, 2.5, 3, 4.0, 2]
    expected = 3
    assert max_val(input_data) == expected

def test_max_val_single_integer():
    # List with only one integer
    input_data = ['a', 'b', 7, 'c']
    expected = 7
    assert max_val(input_data) == expected

def test_max_val_all_non_integers_raises():
    # List with all non-integer types should raise ValueError
    input_data = ['a', 2.5, None, 'b']
    with pytest.raises(ValueError):
        max_val(input_data)