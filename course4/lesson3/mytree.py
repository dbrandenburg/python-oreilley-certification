'''
Created on Aug 18, 2011

@author: sholden
'''
class Tree:
    def __init__(self, key, data):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.data = data
        self.left = self.right = None
    def insert(self, key, data):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield (self.key, self.data)
        if self.right:
            for n in self.right.walk():
                yield n
    def find(self, search):
        "Generate the keys from the tree in sorted order including data."
        if search == self.key:
            return self.data
        elif search < self.key and self.left:
            return self.left.find(search)
        elif self.right:
            return self.right.find(search)
        else:
            raise KeyError(search + " not found")

if __name__ == '__main__':
    t = Tree("D", "dataD")
    for c in "BJQKFAC":
        t.insert(c, "data")

    print(t.find("C"))
