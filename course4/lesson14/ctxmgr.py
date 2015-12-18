#!/usr/bin/env python3


class ctx:
    def __init__(self, raising=True):
        self.raising = raising

    def __enter__(self):
        dummyobj = object()
        return dummyobj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            print("Gracefully supressing ValueError")
            return self.raising
        elif exc_type:
            return not self.raising


if __name__ == "__main__":
    import unittest

    class ctsTestsuite(unittest.TestCase):
        def test_exception(self):
            with self.assertRaises(ZeroDivisionError):
                with ctx() as c:
                    1/0

        def test_exception_catched(self):
            with ctx() as c:
                int("Cause TypeError.")

    unittest.main()
