#!/usr/bin/python3
import classic

def test_hash():
    hsh = classic.Hash()
    assert isinstance(hsh, dict)
    assert isinstance(hsh, classic.Hash)
    assert hsh['a'] == None
    hsh['a'] = 1
    assert hsh['a'] == 1

    hsh = classic.Hash({'a':1, 'b':2})
    assert hsh['a'] == 1
    assert hsh['b'] == 2
    assert hsh['c'] == None

    hsh = classic.Hash(hsh)
    assert isinstance(hsh, dict)
    assert isinstance(hsh, classic.Hash)
    assert hsh['a'] == 1

if __name__ == '__main__':
    test_hash()
    print ('[done]')