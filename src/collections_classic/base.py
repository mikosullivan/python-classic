class Array(list):
    def shift(self):
        '''
        Removes and returns the first element of the array.
        Returns None if the array is empty.
        '''
        
        if len(self) == 0:
            return None
        else:
            return self.pop(0)

    def unshift(self, value):
        '''
        Inserts a new element at the beginning of the array.
        '''
        self.insert(0, value)
    
    def push(self, value):
        '''
        Appends a new element to the end of the array.
        '''
        
        self.append(value)

    def __getitem__(self, idx):
        '''
        Returns the value at the specified index.
        Supports negative indexing.
        Returns None if the index is out of range.
        '''
        if isinstance(idx, int):
            if idx >= 0:
                if idx >= len(self):
                    return None
                else:
                    return super().__getitem__(idx)
            else:
                if abs(idx) > len(self):
                    return None
                else:
                    return super().__getitem__(len(self) + idx)
        else:
            return super().__getitem__(idx)

class Hash(dict):
    def __getitem__(self, key):
        '''
        Returns the value associated with the specified key.
        Returns None if the key is not found.
        '''
        if key in self:
            return super().__getitem__(key)
        else:
            return None
    
    delete = dict.pop