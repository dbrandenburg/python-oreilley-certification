#!/usr/bin/env python3

def object_adder(a, b):
    """Adds two object together"""
    if not datatype_errors(a, b):
        c = a + b
        return c

def datatype_errors(*args):
    """Raises an error in case of not supported datatypes. Returns None if all objects are of tpe integer"""
    for obj in args:
        try: 
            type(obj) is not int
        except:
            return obj, " is not of type int"
            raise TypeError("Object is not of type int")
    return

import sys
print(sys.argv)