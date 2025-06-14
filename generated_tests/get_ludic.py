def get_ludic(n):
	ludics = []
	for i in range(1, n + 1):
		ludics.append(i)
	index = 1
	while(index != len(ludics)):
		first_ludic = ludics[index]
		remove_index = index + first_ludic
		while(remove_index < len(ludics)):
			ludics.remove(ludics[remove_index])
			remove_index = remove_index + first_ludic - 1
		index += 1
	return ludics

import pytest

def test_get_ludic_n_1():
    # Scenario: Get ludic numbers for n=1
    # Reasoning: With n=1, the list starts as [1]. The while loop condition index=1 equals len(ludics)=1, so the loop does not run. The output is [1].
    result = get_ludic(1)
    assert result == [1]

def test_get_ludic_n_2():
    # Scenario: Get ludic numbers for n=2
    # Reasoning: Initial list: [1, 2]. index=1, first_ludic=2. remove_index=3 which is out of range, so no removals. Loop ends. Output is [1, 2].
    result = get_ludic(2)
    assert result == [1, 2]

def test_get_ludic_n_5():
    # Scenario: Get ludic numbers for n=5
    # Reasoning: Start: [1, 2, 3, 4, 5]
    # index=1, first_ludic=2
    # remove_index=3: remove ludics[3]=4 -> list becomes [1, 2, 3, 5]
    # remove_index=4+2-1=6 out of range
    # index=2, first_ludic=3
    # remove_index=5 out of range
    # index=3, first_ludic=5
    # remove_index=8 out of range
    # Loop ends. Output: [1, 2, 3, 5]
    result = get_ludic(5)
    assert result == [1, 2, 3, 5]

def test_get_ludic_n_10():
    # Scenario: Get ludic numbers for n=10
    # Reasoning: Start: [1,2,3,4,5,6,7,8,9,10]
    # index=1, first_ludic=2
    # remove_index=3: remove 4 -> [1,2,3,5,6,7,8,9,10]
    # remove_index=4+2-1=5: remove 6 -> [1,2,3,5,7,8,9,10]
    # remove_index=6+2-1=7: remove 8 -> [1,2,3,5,7,9,10]
    # remove_index=8+2-1=9: remove 10 -> [1,2,3,5,7,9]
    # index=2, first_ludic=3
    # remove_index=5: remove 9 -> [1,2,3,5,7]
    # remove_index=5+3-1=7 out of range
    # index=3, first_ludic=5
    # remove_index=8 out of range
    # Loop ends. Output: [1, 2, 3, 5, 7, 9]
    result = get_ludic(10)
    assert result == [1, 2, 3, 5, 7, 9]

def test_get_ludic_n_15():
    # Scenario: Get ludic numbers for n=15
    # Reasoning: Start: [1..15]
    # index=1, first_ludic=2
    # Remove every 2nd element starting at index 3: remove 4,6,8,10,12,14
    # List after removals: [1,2,3,5,7,9,11,13,15]
    # index=2, first_ludic=3
    # Remove every 3rd element starting at index 5: remove 9
    # List: [1,2,3,5,7,11,13,15]
    # index=3, first_ludic=5
    # Remove every 5th element starting at index 8: out of range, no removal
    # index=4, first_ludic=7
    # Remove every 7th element starting at index 11: out of range
    # index=5, first_ludic=11
    # Remove every 11th element starting at index 16: out of range
    # index=6, first_ludic=13
    # Remove every 13th element starting at index 19: out of range
    # index=7, first_ludic=15
    # Remove every 15th element starting at index 22: out of range
    # Loop ends. Output: [1, 2, 3, 5, 7, 9, 11, 13, 15]
    result = get_ludic(15)
    assert result == [1, 2, 3, 5, 7, 9, 11, 13, 15]