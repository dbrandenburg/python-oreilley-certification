#!/usr/bin/env python3
"""
test_composable.py" performs simple tests of composable functions.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x*x

def power(x):
    "Powers two numbers with each other."
    return x*x

class ComposableTestCase(unittest.TestCase):

    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)

    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)

    def test_power(self):
         powerer = Composable(power)
         power_of_power_a = powerer ** 3
         power_of_power_b = powerer * powerer * powerer
         for v, r in ((1, 1), (5, 390625)):
             self.assertEqual(power_of_power_a(v), r)
             self.assertEqual(power_of_power_b(v), r)
             self.assertEqual(power_of_power_a(v), power_of_power_b(v))

    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc ** "this is a string"
        with self.assertRaises(ValueError):
            fc = fc ** -3

if __name__ == "__main__":
    unittest.main()
