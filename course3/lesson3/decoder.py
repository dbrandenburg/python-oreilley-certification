#!/usr/bin/env python3

"""
A simple iterator letter mapper.
"""
class alphabator:
    def __init__(self, lst):
        "Initialize the iterator object."
        self.lst = lst
        self.itemno = 0
    def __iter__(self):
        "This object is not an iterable."
        return self
    def __next__(self):
        "Return the next value in the output sequence."
        try:
            self.val = self.lst[self.itemno]
        except IndexError:
            raise StopIteration
        self.itemno += 1
        if self.val in range(1,27):
            self.val = chr(self.val + 64)
        return self.val

