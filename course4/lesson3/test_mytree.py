'''
Created on Mar 26, 2015

@author: jpenamar
'''
import unittest
from mytree import Tree
class TreeTestCase(unittest.TestCase):
    """Test the methods of the class Tree."""

    def setUp(self):
        self.tree = Tree('D', 'D data')
        self.tree.insert('Q', 'Q data')  # Insert in right node.
        self.tree.insert('A', 'A data')  # Insert in left node.

    def test_init(self):
        """Verify attributes are initialized as expected."""

        t = Tree('D', 'D data')
        self.assertEqual(t.key, 'D')
        self.assertEqual(t.data, 'D data')
        self.assertTrue(t.left == t.right == None)

    def test_insert(self):
        """Verify subtrees are inserted as expected."""

        t = self.tree
        # Test right subtree.
        self.assertEqual(t.right.key, 'Q')
        self.assertEqual(t.right.data, 'Q data')
        # Test left subtree.
        self.assertEqual(t.left.key, 'A')
        self.assertEqual(t.left.data, 'A data')
        # Test duplicates.
        self.assertRaises(ValueError, t.insert, 'Q', 'Q data')
        self.assertRaises(ValueError, t.insert, 'A', 'A data')

    def test_walk(self):
        """Verify keys, data are returned from tree in order, sorted by key."""

        t = self.tree.walk()
        for kv in [('A', 'A data'), ('D', 'D data'), ('Q', 'Q data')]:
            self.assertEqual(kv, next(t))


    def test_find(self):
        """Verify find() returns the correct data or raises KeyError."""

        t = self.tree
        self.assertEqual(t.find('Q'), 'Q data')
        self.assertEqual(t.find('A'), 'A data')
        self.assertRaises(KeyError, t.find, 'I')


if __name__ == '__main__':
    unittest.main()
