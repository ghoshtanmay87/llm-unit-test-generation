def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2

import pytest

def test_replace_spaces_with_underscores_in_simple_sentence():
    result = replace_blank('hello world', '_')
    assert result == 'hello_world'

def test_replace_spaces_with_hyphens_in_sentence_with_multiple_spaces():
    result = replace_blank('a b c d', '-')
    assert result == 'a-b-c-d'

def test_replace_spaces_with_empty_string_to_remove_spaces():
    result = replace_blank('remove all spaces', '')
    assert result == 'removeallspaces'

def test_replace_spaces_with_asterisk_in_string_with_leading_and_trailing_spaces():
    result = replace_blank('  spaced out  ', '*')
    assert result == '**spaced*out**'

def test_no_spaces_in_input_string_replacement_character_does_not_affect_output():
    result = replace_blank('nospace', '#')
    assert result == 'nospace'

def test_replace_spaces_with_multiple_characters():
    result = replace_blank('multi space test', '--')
    assert result == 'multi--space--test'

def test_empty_string_input_returns_empty_string_regardless_of_replacement_character():
    result = replace_blank('', '@')
    assert result == ''