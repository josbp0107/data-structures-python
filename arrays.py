from random import randint
import random

"""
Code used for Create an array in python
Methods:
    1. Length
    2. List representation
    3. Membership
    4. Index
    5. Remplacement
"""

class Array:
    """Represent an Array"""
    def __init__(self, capacity, fill_value=None):
        """
        Args:
            capacity(int): static size of the Array
            fill_value(any, optional): Value at each position. Default is None.
        """
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        """Return capacity of the array."""
        return len(self.items)

    def __list__(self):
        """Return list of elements in array."""
        return list(self.items)

    def __iter__(self):
        """Supports traversal with a for loop.""" 
        return iter(self.items)
    
    def __getitem__(self,index):
        """Subscrit operator for a access at index."""
        return self.items[index]
    
    def __setitem__(self,index,new_item):
        """Subscrit operator for remplacement at index."""
        self.items[index] = new_item
    
    def __replace__(self):
        """Return list with items modified by random values"""
        return [ self.__setitem__(i,random.randint(0,100)) for i in range(self.capacity) ]
    
    def __sumArrays__(self):
        """Return sum of all elements in array"""
        return sum(self.items)
    
    