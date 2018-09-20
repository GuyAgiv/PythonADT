from TwoThreeTreeNode import *

class TwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        print "Tree insert: " + str(value)
        if self.root is None:
            self.root = TwoThreeTreeNode(value)
        else:
            self.root.insert(TwoThreeTreeNode(value))
            while self.root.GetParentNode():
                self.root = self.root.GetParentNode()
        return True

    def search(self, value):
        return self.root.find(value)

    def remove(self, item):
        self.root.remove(item)

    def preorder(self):
        self.root.internalPreorder()


