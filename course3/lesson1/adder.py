#!/usr/bin/env python3

def object_adder(a, b):
    """Adds two object together"""
    if type(a) is not int or type(b) is not int:
        raise TypeError("Object is not of type int")
    return a + b

import sys
print(sys.argv)

"""Too complicated to have two functions, as adder() can be just three lines:

def adder(a, b):
    if either of the args is not an int:
        raise TypeError
    return a + b

That's it.  Just replace the pseudocode with working Python in the first line.

I am mainly interested in your assertRaises tests.  One does not call the callable in those, the arguments stay separate, like this:

    self.assertRaises(TypeError, adder, 1.0, 2)  # should pass because 1.0 is a float.

Give it another whirl!


-Kirby"""