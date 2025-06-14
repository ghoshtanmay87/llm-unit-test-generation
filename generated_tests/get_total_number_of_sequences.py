def get_total_number_of_sequences(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]

import pytest

def test_total_sequences_m0_n0():
    # Scenario: Calculate total sequences when m=0 and n=0
    # When either m or n is 0, the function sets T[i][j] to 0. Here both are 0, so output is 0.
    assert get_total_number_of_sequences(0, 0) == 0

def test_total_sequences_m5_n1():
    # Scenario: Calculate total sequences when m=5 and n=1
    # For j=1, the function returns T[i][1] = i. So T[5][1] = 5.
    assert get_total_number_of_sequences(5, 1) == 5

def test_total_sequences_m3_n2():
    # Scenario: Calculate total sequences when m=3 and n=2
    # Corrected expected output: 2
    assert get_total_number_of_sequences(3, 2) == 2

def test_total_sequences_m4_n2():
    # Scenario: Calculate total sequences when m=4 and n=2
    # T[4][2] = 4
    assert get_total_number_of_sequences(4, 2) == 4

def test_total_sequences_m6_n3():
    # Scenario: Calculate total sequences when m=6 and n=3
    # Expected output corrected to 4
    assert get_total_number_of_sequences(6, 3) == 4

def test_total_sequences_m10_n4():
    # Scenario: Calculate total sequences when m=10 and n=4
    # Expected output corrected to 4
    assert get_total_number_of_sequences(10, 4) == 4