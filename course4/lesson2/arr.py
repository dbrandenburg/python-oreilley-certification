#!/usr/bin/env python3
"""
Class-based dict allowing tuple subscripting and sparse data
"""
import array as sys_array

class array:

    def __init__(self, M, N, O):
        "Create an M-element list of N-element row lists."
        self._data = {}
        self._rows = M
        self._cols = N
        self._layer = O

    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col, layer = self._validate_key(key)
        try:
            return self._data[row, col, layer]
        except KeyError:
            return  0

    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col, layer = self._validate_key(key)
        self._data[row, col, layer] = value

    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        row, col, layer = key
        if (
            0 <= row < self._rows and
            0 <= col < self._cols and
            0 <= layer < self._layer
            ):
            return key
        raise KeyError("Subscript out of range")
