def test_numbers_3_4():
    assert 3*4 == 12

def test_strings_a_3():
    assert "a"*3 == 'aaa'

def test_subtraction_5_2():
    assert 5 - 2 == 3

def test_list_1_2_3():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a == b

def test_tuple_1_2_3():
    a = (1, 2, 3)
    b = (1, 2, 3)
    assert a == b

def test_string_Abc():
    assert "Abc" == "Abc"

def test_string_abC():
    assert "abC" == "abC"

def test_division_8_2():
    assert 8 / 2 == 4

def test_exponent_2_3():
    assert 2 ** 3 == 8

def test_dict_capitals():
    capitals = {1: "Moscow", 2: "Paris", 3: "Toronto"}
    assert 1 in capitals
