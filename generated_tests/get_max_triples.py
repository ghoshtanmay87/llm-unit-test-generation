def get_max_triples(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)

import pytest

def test_no_triples_for_n_1():
    # With n=1, the list A has one element: [1]. No triples (3 elements) can be formed, so the output is 0.
    assert get_max_triples(1) == 0

def test_no_triples_for_n_2():
    # With n=2, A = [1, 3]. Still no triples possible since we need 3 elements, so output is 0.
    assert get_max_triples(2) == 0

def test_one_triple_for_n_4():
    # A = [1, 3, 7, 13]. Only one triple sums to multiple of 3, so output is 1.
    assert get_max_triples(4) == 1

def test_four_triples_for_n_6():
    # A = [1, 3, 7, 13, 21, 31]
    # Total triples summing to multiple of 3: 4
    assert get_max_triples(6) == 4

def test_no_triple_for_n_3():
    # For n=3, A = [1, 3, 7]. The only triple is (1, 3, 7) with sum 11, 11 % 3 = 2, so no triple sums to multiple of 3.
    assert get_max_triples(3) == 0

def test_one_triple_for_n_5():
    # A = [1, 3, 7, 13, 21]. Only one triple sums to multiple of 3, so output is 1.
    assert get_max_triples(5) == 1