M = 100
def maxAverageOfPath(cost, N): 
	dp = [[0 for i in range(N + 1)] for j in range(N + 1)] 
	dp[0][0] = cost[0][0] 
	for i in range(1, N): 
		dp[i][0] = dp[i - 1][0] + cost[i][0] 
	for j in range(1, N): 
		dp[0][j] = dp[0][j - 1] + cost[0][j] 
	for i in range(1, N): 
		for j in range(1, N): 
			dp[i][j] = max(dp[i - 1][j], 
						dp[i][j - 1]) + cost[i][j] 
	return dp[N - 1][N - 1] / (2 * N - 1)

import pytest

def test_max_average_path_1x1_matrix():
    cost = [[5]]
    N = 1
    expected_output = 5.0
    assert maxAverageOfPath(cost, N) == expected_output

def test_max_average_path_2x2_increasing_values():
    cost = [[1, 2], [3, 4]]
    N = 2
    expected_output = 2.6666666666666665
    assert maxAverageOfPath(cost, N) == expected_output

def test_max_average_path_3x3_uniform_values():
    cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    N = 3
    expected_output = 1.0
    assert maxAverageOfPath(cost, N) == expected_output

def test_max_average_path_3x3_varying_values():
    cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 3
    expected_output = 5.8
    assert maxAverageOfPath(cost, N) == expected_output

def test_max_average_path_4x4_zeros_with_one_path():
    cost = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ]
    N = 4
    expected_output = 0.14285714285714285
    assert maxAverageOfPath(cost, N) == expected_output