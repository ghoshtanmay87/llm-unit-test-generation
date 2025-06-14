def encode_cyclic(s: str):
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str):
    return encode_cyclic(encode_cyclic(s))

import pytest

def test_decode_empty_string_returns_empty_string():
    # Decoding an empty string returns an empty string
    s = ''
    expected = ''
    assert decode_cyclic(s) == expected

def test_decode_string_length_1_returns_same_string():
    # Decoding a string of length 1 returns the same string
    s = 'A'
    expected = 'A'
    assert decode_cyclic(s) == expected

def test_decode_string_length_2_returns_same_string():
    # Decoding a string of length 2 returns the same string
    s = 'AB'
    expected = 'AB'
    assert decode_cyclic(s) == expected

def test_decode_string_length_3_rotates_group_twice():
    # Decoding a string of length 3 rotates the group twice
    s = 'ABC'
    expected = 'CAB'
    assert decode_cyclic(s) == expected

def test_decode_string_length_4_rotates_first_group_twice_leaves_last_char():
    # Decoding a string of length 4 rotates the first group twice and leaves the last character
    s = 'ABCD'
    expected = 'CABD'
    assert decode_cyclic(s) == expected

def test_decode_string_length_6_rotates_two_groups_twice_each():
    # Decoding a string of length 6 rotates two groups twice each
    s = 'ABCDEF'
    expected = 'CABFDE'
    assert decode_cyclic(s) == expected

def test_decode_string_length_7_rotates_two_groups_twice_leaves_last_char():
    # Decoding a string of length 7 rotates two groups twice and leaves last character
    s = 'ABCDEFG'
    expected = 'CABFDEG'
    assert decode_cyclic(s) == expected

def test_decode_string_multiple_full_groups():
    # Decoding a string with multiple full groups
    s = 'ABCDEFGHIJK'
    expected = 'CABFDEIGHJK'
    assert decode_cyclic(s) == expected