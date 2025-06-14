import re
def road_rd(street):
  return (re.sub('Road$', 'Rd.', street))

import pytest

def test_street_name_ending_with_road_is_replaced():
    # The input string ends with 'Road', so it should be replaced with 'Rd.'
    input_street = 'Main Road'
    expected = 'Main Rd.'
    assert road_rd(input_street) == expected

def test_street_name_not_ending_with_road_remains_unchanged():
    # The input string does not end with 'Road', so it should remain unchanged
    input_street = 'Main Street'
    expected = 'Main Street'
    assert road_rd(input_street) == expected

def test_street_name_containing_road_but_not_at_end_remains_unchanged():
    # The input string contains 'Road' but not at the end, so it should remain unchanged
    input_street = 'Broadway'
    expected = 'Broadway'
    assert road_rd(input_street) == expected

def test_street_name_ending_with_road_in_mixed_case_not_replaced():
    # The input string ends with 'road' in lowercase, so no replacement due to case sensitivity
    input_street = 'Main road'
    expected = 'Main road'
    assert road_rd(input_street) == expected

def test_street_name_with_multiple_words_ending_with_road_is_replaced():
    # The input string ends with 'Road', so it should be replaced with 'Rd.'
    input_street = 'Old Country Road'
    expected = 'Old Country Rd.'
    assert road_rd(input_street) == expected