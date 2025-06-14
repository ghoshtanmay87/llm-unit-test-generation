def bf(planet1, planet2):
    planet_names = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return planet_names[planet1_index + 1:planet2_index]
    else:
        return planet_names[planet2_index + 1:planet1_index]

import pytest

def test_planets_in_order_mercury_to_earth():
    # Mercury index is 0, Earth index is 2, so planets between indices 1 and 2 are ('Venus',).
    result = bf('Mercury', 'Earth')
    assert result == ('Venus',)

def test_planets_in_reverse_order_mars_to_venus():
    # Mars index is 3, Venus index is 1, so planets between indices 2 and 3 are ('Earth',).
    result = bf('Mars', 'Venus')
    assert result == ('Earth',)

def test_same_planet_input_returns_empty_tuple():
    # Input planets are the same, so function returns empty tuple as per condition.
    result = bf('Jupiter', 'Jupiter')
    assert result == ()

def test_invalid_planet_name_returns_empty_tuple():
    # Pluto is not in the planet_names tuple, so function returns empty tuple.
    result = bf('Pluto', 'Earth')
    assert result == ()

def test_planets_with_multiple_in_between_venus_to_saturn():
    # Venus index 1, Saturn index 5, planets between indices 2 and 5 are ('Earth', 'Mars', 'Jupiter').
    result = bf('Venus', 'Saturn')
    assert result == ('Earth', 'Mars', 'Jupiter')

def test_planets_with_multiple_in_between_neptune_to_mars():
    # Neptune index 7, Mars index 3, planets between indices 4 and 7 are ('Jupiter', 'Saturn', 'Uranus').
    result = bf('Neptune', 'Mars')
    assert result == ('Jupiter', 'Saturn', 'Uranus')

def test_adjacent_planets_earth_to_mars_returns_empty_tuple():
    # Earth index 2, Mars index 3, no planets between indices 3 and 2, so empty tuple.
    result = bf('Earth', 'Mars')
    assert result == ()

def test_adjacent_planets_mars_to_earth_returns_empty_tuple():
    # Mars index 3, Earth index 2, no planets between indices 3 and 2, so empty tuple.
    result = bf('Mars', 'Earth')
    assert result == ()