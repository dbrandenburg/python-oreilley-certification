#!/usr/bin/env python3
import unittest

def addarg(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(1, *args, **kwargs)
        return wrapper
    return decorator

@addarg(1)
def prargs(*args):
    return args

@addarg(1)
def prargskwargs(*args,**kwargs):
    return args,kwargs

class DecoTests(unittest.TestCase):
    def test_args(self):
        self.assertEqual((1, 2, 3), prargs(2, 3), 'Should return 1 at the' +
            'beginning of the args tuple')
        self.assertEqual((1,"child"), prargs("child"), 'Should retunr 1 at' +
            'the beginning of the tuple followed by the given string')
    def test_kwargs(self):
        self.assertEqual(((1, 2, 3), {'a': 4}), prargskwargs(2, 3, a=4),
            'Schould contain 1 at the beginning of the key tuple followed by' +
            'the passed in kwarg as a second tuple')
        self.assertEqual(
            ((1, 'child'), {'name': 'Tim'}),
            prargskwargs("child", name='Tim'),
            'Should contain 1 at the beginning of the key tuple followed by' +
            'the passed in string kwarg as a second tuple')

if __name__ == '__main__':
    unittest.main()
