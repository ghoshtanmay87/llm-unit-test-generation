from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

import pytest

def test_parse_music_simple_single_notes():
    music_string = 'o o| .|'
    expected_output = [4, 2, 1]
    assert parse_music(music_string) == expected_output

def test_parse_music_repeated_notes_extra_spaces():
    music_string = 'o o o|  .|  o|'
    expected_output = [4, 4, 2, 1, 2]
    assert parse_music(music_string) == expected_output

def test_parse_music_leading_trailing_spaces():
    music_string = '  o| .| o  '
    expected_output = [2, 1, 4]
    assert parse_music(music_string) == expected_output

def test_parse_music_single_note():
    music_string = 'o|'
    expected_output = [2]
    assert parse_music(music_string) == expected_output

def test_parse_music_empty_string():
    music_string = ''
    expected_output = []
    assert parse_music(music_string) == expected_output