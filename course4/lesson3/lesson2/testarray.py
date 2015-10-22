"""
Test list-of-list array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)

    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i==j and i==k)

    def _index(self, a, r, c, l):
        return a[r, c, l]

    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a ,-1, 1, 2)
        self.assertRaises(KeyError, self._index, a ,10, 1, 2)
        self.assertRaises(KeyError, self._index, a ,1, -1, 2)
        self.assertRaises(KeyError, self._index, a ,1, 10, 2)

if __name__ == "__main__":
    unittest.main()
