def dog_age(h_age):
 if h_age < 0:
 	exit()
 elif h_age <= 2:
	 d_age = h_age * 10.5
 else:
	 d_age = 21 + (h_age - 2)*4
 return d_age

import pytest

def test_dog_age_negative_input_exits(monkeypatch):
    # The function calls exit() for negative input, which raises SystemExit
    with pytest.raises(SystemExit):
        dog_age(-1)

def test_dog_age_zero_input_returns_zero():
    result = dog_age(0)
    assert result == 0.0

def test_dog_age_one_input_returns_10_point_5():
    result = dog_age(1)
    assert result == 10.5

def test_dog_age_two_input_returns_21_point_0():
    result = dog_age(2)
    assert result == 21.0

def test_dog_age_three_input_returns_25_point_0():
    result = dog_age(3)
    assert result == 25.0

def test_dog_age_five_input_returns_33_point_0():
    result = dog_age(5)
    assert result == 33.0

def test_dog_age_ten_input_returns_53_point_0():
    result = dog_age(10)
    assert result == 53.0