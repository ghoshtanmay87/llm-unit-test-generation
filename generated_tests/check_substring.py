import re 
def check_substring(string, sample) : 
  if (sample in string): 
      y = "\A" + sample 
      x = re.search(y, string) 
      if x : 
          return ("string starts with the given substring") 
      else : 
          return ("string doesnt start with the given substring") 
  else : 
      return ("entered string isnt a substring")

import pytest

def test_sample_substring_at_start():
    # Sample substring is at the start of the string
    result = check_substring(string='hello world', sample='hello')
    assert result == 'string starts with the given substring'

def test_sample_substring_inside_not_start():
    # Sample substring is inside the string but not at the start
    result = check_substring(string='say hello world', sample='hello')
    assert result == "string doesnt start with the given substring"

def test_sample_substring_not_found():
    # Sample substring is not found in the string
    result = check_substring(string='goodbye world', sample='hello')
    assert result == "entered string isnt a substring"

def test_sample_substring_is_entire_string():
    # Sample substring is the entire string
    result = check_substring(string='hello', sample='hello')
    assert result == 'string starts with the given substring'

def test_empty_sample_substring():
    # Empty sample substring
    result = check_substring(string='hello world', sample='')
    assert result == 'string starts with the given substring'