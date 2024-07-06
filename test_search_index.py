from search_index import search_index

def test_list_len_is_1():
    assert 0 == search_index(0, [0])

def test_list_len_is_2():
    assert 0 == search_index(0, [0,1])
    assert 1 == search_index(1, [0,1])

def test_list_len_is_3():
    assert 0 == search_index(0, [0,1,2])
    assert 1 == search_index(1, [0,1,2])
    assert 2 == search_index(2, [0,1,2])

def test_empty_list():
    assert -1 == search_index(3, [])

def test_value_not_exist():
    assert -1 == search_index(3, [0,1,2])
