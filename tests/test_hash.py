#!/usr/bin/python3
from collections_classic import Hash

def test_hash():
    hsh = Hash()
    assert isinstance(hsh, dict)
    assert isinstance(hsh, Hash)
    assert hsh['a'] == None
    hsh['a'] = 1
    assert hsh['a'] == 1

    hsh = Hash({'a':1, 'b':2})
    assert hsh['a'] == 1
    assert hsh['b'] == 2
    assert hsh['c'] == None

    hsh = Hash(hsh)
    assert isinstance(hsh, dict)
    assert isinstance(hsh, Hash)
    assert hsh['a'] == 1

if __name__ == '__main__':
    test_hash()
    print ('[done]')