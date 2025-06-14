import re
def find_adverbs(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

import pytest

def test_find_first_adverb_simple_sentence():
    # Find the first adverb ending with 'ly' in a simple sentence
    text = 'She quickly ran to the store.'
    expected = '4-11: quickly'
    assert find_adverbs(text) == expected

def test_find_first_adverb_multiple_adverbs():
    # Find the first adverb when multiple adverbs are present
    text = 'He slowly and carefully walked away.'
    expected = '3-9: slowly'
    assert find_adverbs(text) == expected

def test_no_adverb_ending_ly():
    # No adverbs ending with 'ly' in the text
    text = 'She runs fast and well.'
    expected = None
    assert find_adverbs(text) == expected

def test_adverb_at_start_of_text():
    # Adverb at the very start of the text
    text = 'Quickly he left the room.'
    expected = '0-7: Quickly'
    assert find_adverbs(text) == expected

def test_adverb_at_end_of_text():
    # Adverb at the very end of the text
    text = 'He did it happily'
    expected = '10-17: happily'
    assert find_adverbs(text) == expected

def test_adverb_with_punctuation_after():
    # Adverb with punctuation immediately after
    text = 'She spoke softly, but firmly.'
    expected = '10-16: softly'
    assert find_adverbs(text) == expected

def test_multiple_adverbs_different_cases():
    # Multiple adverbs with different cases
    text = 'Loudly and clearly, he announced the news.'
    expected = '0-6: Loudly'
    assert find_adverbs(text) == expected

def test_adverb_embedded_in_longer_word():
    # Adverb embedded in a longer word
    text = 'The friendly neighborhood cat.'
    expected = '4-12: friendly'
    assert find_adverbs(text) == expected