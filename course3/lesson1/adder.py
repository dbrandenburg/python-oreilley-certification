#!/usr/bin/env python3

def object_adder(a, b):
    """Adds two object together"""
    if type(a) is not int or type(b) is not int:
        raise TypeError("Object is not of type int")
    return a + b

import sys
print(sys.argv)
