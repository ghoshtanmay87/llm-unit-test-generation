import re
def find_adverb_position(text):
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))

import pytest

def test_find_first_adverb_simple_sentence():
    # Find the first adverb ending with 'ly' in a simple sentence
    text = 'She quickly ran to the store.'
    expected = (4, 11, 'quickly')
    assert find_adverb_position(text) == expected

def test_find_first_adverb_multiple_adverbs():
    # Find the first adverb ending with 'ly' when multiple are present
    text = 'He slowly and carefully opened the door.'
    expected = (3, 9, 'slowly')
    assert find_adverb_position(text) == expected

def test_no_adverb_ending_ly():
    # No adverb ending with 'ly' in the text
    text = 'She runs fast and well.'
    expected = None
    assert find_adverb_position(text) == expected

def test_adverb_at_start_of_text():
    # Adverb at the start of the text
    text = 'Happily, they agreed to the plan.'
    expected = (0, 7, 'Happily')
    assert find_adverb_position(text) == expected

def test_adverb_with_punctuation_after():
    # Adverb with punctuation immediately after
    text = 'She spoke softly, but clearly.'
    expected = (9, 15, 'softly')
    assert find_adverb_position(text) == expected

def test_adverb_with_uppercase_letters():
    # Adverb with uppercase letters
    text = 'Loudly and Proudly they shouted.'
    expected = (0, 6, 'Loudly')
    assert find_adverb_position(text) == expected

def test_adverb_embedded_in_longer_word():
    # Adverb embedded in a longer word
    text = 'The familyly event was unusual.'
    expected = (4, 11, 'familyly')
    assert find_adverb_position(text) == expected