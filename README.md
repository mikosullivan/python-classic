# python-classic
Classic arrays and hashes for python.

```
from classic import Array, Hash

arr = Array()
arr.shift() # removes and returns the first element; if array is empty, returns None
arr.unshift() # prepends an element
arr.push() # appends an element to the end of the array

hsh = Hash()
hsh[key] # returns the element at key; returns None if element does not exist
hsh.delete(key) # deletes the element at key
```