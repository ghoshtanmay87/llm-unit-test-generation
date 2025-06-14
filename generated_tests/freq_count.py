import collections
def freq_count(list1):
  freq_count= collections.Counter(list1)
  return freq_count

import pytest

def test_count_frequency_of_elements_in_empty_list():
    input_data = {'list1': []}
    expected_output = {}
    assert freq_count(**input_data) == expected_output