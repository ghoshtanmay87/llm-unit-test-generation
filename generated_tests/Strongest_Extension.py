def Strongest_Extension(class_name, extensions):
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val
    ans = class_name + '.' + strong
    return ans

import pytest

def test_single_extension_with_mixed_case_letters():
    # Only one extension 'Dog' is present. Uppercase letters: 'D' (1), lowercase letters: 'o', 'g' (2).
    # Value = 1 - 2 = -1. Since it's the only extension, it is selected.
    class_name = 'Animal'
    extensions = ['Dog']
    expected = 'Animal.Dog'
    assert Strongest_Extension(class_name, extensions) == expected

def test_multiple_extensions_with_varying_uppercase_and_lowercase_counts():
    # Values: 'Car' -> val = -1; 'BIKE' -> val = 4; 'bicycle' -> val = -7.
    # Highest val is 4 for 'BIKE'.
    class_name = 'Vehicle'
    extensions = ['Car', 'BIKE', 'bicycle']
    expected = 'Vehicle.BIKE'
    assert Strongest_Extension(class_name, extensions) == expected

def test_extensions_with_equal_values_first_one_chosen():
    # 'APPLE' = 5, 'BANANA' = 6, 'CHERRY' = 6.
    # Highest val is 6. The function picks the first with highest val: 'BANANA'.
    class_name = 'Fruit'
    extensions = ['APPLE', 'BANANA', 'CHERRY']
    expected = 'Fruit.BANANA'
    assert Strongest_Extension(class_name, extensions) == expected

def test_extensions_with_no_alphabetic_characters():
    # No alphabetic characters, val=0 for all.
    # The first extension '123' is chosen.
    class_name = 'Number'
    extensions = ['123', '4567', '89']
    expected = 'Number.123'
    assert Strongest_Extension(class_name, extensions) == expected

def test_extensions_with_mixed_letters_and_digits():
    # 'A1b2' val=0; 'C3D4' val=2; 'e5F6' val=0.
    # Highest val=2 for 'C3D4'.
    class_name = 'Code'
    extensions = ['A1b2', 'C3D4', 'e5F6']
    expected = 'Code.C3D4'
    assert Strongest_Extension(class_name, extensions) == expected

def test_extensions_with_equal_val_later_extension_does_not_replace_earlier():
    # 'AbC' val=1; 'aBC' val=1; 'ABC' val=3.
    # Highest val=3 for 'ABC'.
    class_name = 'Test'
    extensions = ['AbC', 'aBC', 'ABC']
    expected = 'Test.ABC'
    assert Strongest_Extension(class_name, extensions) == expected

def test_extensions_with_all_lowercase_letters():
    # 'tree' val=-4, 'flower' val=-6, 'grass' val=-5.
    # Highest val is -4 for 'tree'.
    class_name = 'Plant'
    extensions = ['tree', 'flower', 'grass']
    expected = 'Plant.tree'
    assert Strongest_Extension(class_name, extensions) == expected