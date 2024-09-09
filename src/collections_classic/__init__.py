"""
Provides classes for arrays and hashes that work like in other languages like Ruby and Perl.

    from classic import Array, Hash

    arr = Array()
    arr.shift() # removes and returns the first element; if array is empty, returns None
    arr.unshift() # prepends an element
    arr.push() # appends an element to the end of the array

    hsh = Hash()
    hsh[key] # returns the element at key; returns None if element does not exist
    hsh.delete(key) # deletes the element at key

"""

__all__ = [
    'Array',
    'Hash',
]

__version__ = '0.1.0'


from .base import Array, Hash