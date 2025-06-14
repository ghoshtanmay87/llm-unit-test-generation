def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys

    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True

import pytest

def test_matching_lengths_with_consistent_color_pattern_mapping():
    colors = ['red', 'red', 'blue']
    patterns = ['striped', 'striped', 'dotted']
    expected = True
    assert is_samepatterns(colors, patterns) == expected

def test_different_lengths_of_colors_and_patterns():
    colors = ['red', 'blue']
    patterns = ['striped', 'dotted', 'plain']
    expected = False
    assert is_samepatterns(colors, patterns) == expected

def test_same_number_of_unique_patterns_and_colors_but_inconsistent_color_mapping():
    colors = ['red', 'blue', 'blue']
    patterns = ['striped', 'striped', 'dotted']
    expected = False
    assert is_samepatterns(colors, patterns) == expected

def test_number_of_unique_patterns_and_colors_differ():
    colors = ['red', 'red', 'blue']
    patterns = ['striped', 'dotted', 'plain']
    expected = False
    assert is_samepatterns(colors, patterns) == expected

def test_all_patterns_and_colors_are_the_same():
    colors = ['green', 'green', 'green']
    patterns = ['solid', 'solid', 'solid']
    expected = True
    assert is_samepatterns(colors, patterns) == expected