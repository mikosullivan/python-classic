#!/usr/bin/python3
import classic

def test_array():
    arr = classic.Array(['a', 'b', 'c'])
    assert isinstance(arr, list)
    assert isinstance(arr, classic.Array)
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

    arr = classic.Array()
    arr.push('a')
    arr.push('b')
    arr.push('c')
    arr = classic.Array(arr)
    assert arr[0] == 'a'
    assert arr[1] == 'b'
    assert arr[2] == 'c'

    arr = classic.Array()
    assert arr.shift() == None

if __name__ == '__main__':
    test_array()
    print ('[done]')