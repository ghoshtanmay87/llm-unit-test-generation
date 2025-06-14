def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

import pytest

def test_max_sum_n_0_base_case():
    # For n=0, the function returns res[0] which is initialized to 0.
    assert get_max_sum(0) == 0

def test_max_sum_n_1_base_case():
    # For n=1, the function returns res[1] which is initialized to 1.
    assert get_max_sum(1) == 1

def test_max_sum_n_2():
    # res[2] = max(2, res[1]+res[0]+res[0]+res[0]) = max(2, 1+0+0+0) = 2.
    assert get_max_sum(2) == 2

def test_max_sum_n_5():
    # For i=5:
    # int(5/2)=2, int(5/3)=1, int(5/4)=1, int(5/5)=1
    # Sum = res[2]+res[1]+res[1]+res[1] = 2+1+1+1=5
    # max(5,5)=5
    assert get_max_sum(5) == 5

def test_max_sum_n_10():
    # For i=10:
    # int(10/2)=5, int(10/3)=3, int(10/4)=2, int(10/5)=2
    # Sum = res[5]+res[3]+res[2]+res[2] = 5+3+2+2=12
    # max(10,12)=12
    assert get_max_sum(10) == 12

def test_max_sum_n_12():
    # For i=12:
    # int(12/2)=6, int(12/3)=4, int(12/4)=3, int(12/5)=2
    # Sum = res[6]+res[4]+res[3]+res[2] = 7+4+3+2=16
    # max(12,16)=16
    assert get_max_sum(12) == 16

def test_max_sum_n_15():
    # For i=15:
    # int(15/2)=7, int(15/3)=5, int(15/4)=3, int(15/5)=3
    # Sum = res[7]+res[5]+res[3]+res[3] = 7+5+3+3=18
    # max(15,18)=18
    assert get_max_sum(15) == 18