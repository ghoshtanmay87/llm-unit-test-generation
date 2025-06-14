def No_of_cubes(N,K):
    No = 0
    No = (N - K + 1)
    No = pow(No, 3)
    return No

import pytest

def test_no_of_cubes_when_N_and_K_are_equal():
    # When N equals K, the expression (N - K + 1) equals 1, so the number of cubes is 1^3 = 1.
    N = 5
    K = 5
    expected_output = 1
    assert No_of_cubes(N, K) == expected_output

def test_no_of_cubes_when_K_is_1_and_N_is_3():
    # With N=3 and K=1, (N - K + 1) = 3, so the number of cubes is 3^3 = 27.
    N = 3
    K = 1
    expected_output = 27
    assert No_of_cubes(N, K) == expected_output

def test_no_of_cubes_when_N_is_4_and_K_is_2():
    # For N=4 and K=2, (N - K + 1) = 3, so the number of cubes is 3^3 = 27.
    N = 4
    K = 2
    expected_output = 27
    assert No_of_cubes(N, K) == expected_output

def test_no_of_cubes_when_N_is_10_and_K_is_3():
    # For N=10 and K=3, (N - K + 1) = 8, so the number of cubes is 8^3 = 512.
    N = 10
    K = 3
    expected_output = 512
    assert No_of_cubes(N, K) == expected_output

def test_no_of_cubes_when_N_is_1_and_K_is_1():
    # When N=1 and K=1, (N - K + 1) = 1, so the number of cubes is 1^3 = 1.
    N = 1
    K = 1
    expected_output = 1
    assert No_of_cubes(N, K) == expected_output