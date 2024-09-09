#!/usr/bin/python3
from collections_classic import Array

def test_array():
    arr = Array(['a', 'b', 'c'])
    assert isinstance(arr, list)
    assert isinstance(arr, Array)
    assert len(arr) == 3
    assert arr[0] == 'a'
    assert arr[1] == 'b'
    assert arr[2] == 'c'
    assert arr[3] == None
    assert arr[-1] == 'c'
    assert arr[-2] == 'b'
    assert arr[-3] == 'a'
    assert arr[-4] == None
    arr.push('d')
    assert arr[3] == 'd'
    assert arr[-1] == 'd'
    assert arr.shift() == 'a'
    assert arr[0] == 'b'

    arr = Array()
    arr.push('a')
    arr.push('b')
    arr.push('c')
    arr = Array(arr)
    assert arr[0] == 'a'
    assert arr[1] == 'b'
    assert arr[2] == 'c'

    arr = Array()
    assert arr.shift() == None

if __name__ == '__main__':
    test_array()
    print ('[done]')