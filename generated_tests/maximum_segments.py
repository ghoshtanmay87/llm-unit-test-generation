def maximum_segments(n, a, b, c) : 
	dp = [-1] * (n + 10) 
	dp[0] = 0
	for i in range(0, n) : 
		if (dp[i] != -1) : 
			if(i + a <= n ): 
				dp[i + a] = max(dp[i] + 1, 
							dp[i + a]) 
			if(i + b <= n ): 
				dp[i + b] = max(dp[i] + 1, 
							dp[i + b]) 
			if(i + c <= n ): 
				dp[i + c] = max(dp[i] + 1, 
							dp[i + c]) 
	return dp[n]

import pytest

def test_max_segments_n5_lengths_5_3_2():
    # Maximum segments when n=5 and segment lengths are 5, 3, 2
    n, a, b, c = 5, 5, 3, 2
    expected = 2
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n7_lengths_5_5_2():
    # Maximum segments when n=7 and segment lengths are 5, 5, 2
    n, a, b, c = 7, 5, 5, 2
    expected = 2
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n7_lengths_5_2_2():
    # Maximum segments when n=7 and segment lengths are 5, 2, 2
    n, a, b, c = 7, 5, 2, 2
    expected = 3
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n9_lengths_2_2_2():
    # Maximum segments when n=9 and segment lengths are 2, 2, 2
    n, a, b, c = 9, 2, 2, 2
    expected = -1
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n10_lengths_2_3_5():
    # Maximum segments when n=10 and segment lengths are 2, 3, 5
    n, a, b, c = 10, 2, 3, 5
    expected = 5
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n0_lengths_1_2_3():
    # Maximum segments when n=0 and segment lengths are 1, 2, 3
    n, a, b, c = 0, 1, 2, 3
    expected = 0
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n1_lengths_2_3_4():
    # Maximum segments when n=1 and segment lengths are 2, 3, 4
    n, a, b, c = 1, 2, 3, 4
    expected = -1
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n8_lengths_3_3_3():
    # Maximum segments when n=8 and segment lengths are 3, 3, 3
    n, a, b, c = 8, 3, 3, 3
    expected = -1
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n6_lengths_1_2_3():
    # Maximum segments when n=6 and segment lengths are 1, 2, 3
    n, a, b, c = 6, 1, 2, 3
    expected = 6
    assert maximum_segments(n, a, b, c) == expected

def test_max_segments_n11_lengths_2_5_6():
    # Maximum segments when n=11 and segment lengths are 2, 5, 6
    n, a, b, c = 11, 2, 5, 6
    expected = 3
    assert maximum_segments(n, a, b, c) == expected