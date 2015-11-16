#!/usr/bin/env python3
class Sstr(str):
    def __lshift__(self, shift_count):
        lshifted = self[shift_count:] + self[:shift_count]
        return Sstr(lshifted)

    def __rshift__(self, shift_count):
        rshifted = self[-shift_count:] + self[:-shift_count]
        return Sstr(rshifted)
