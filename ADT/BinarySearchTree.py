from ADT.BinaryTree import *

class BinarySearchTree(BinaryTree):

    # Constructor of Binary Tree
    def __init__(self, root = None):
        super(BinarySearchTree, self).__init__()

    def search(self, value):
        if self.isEmpty():
            raise ValueError("Tree is empty!")

        else:
            iterator = self._root
            while iterator:
                if value == iterator.GetValue():
                    break
                elif value < iterator.GetValue():
                    iterator = iterator.GetLeftNode()
                else:
                    iterator = iterator.GetRightNode()
            # If value did'nt found , None value will return .. else the node will return.
            return iterator

    def remove(self, value):
        theRequestedNode = self.search(value)
        if theRequestedNode is None:
            return None
        if theRequestedNode.GetLeftNode() is None or theRequestedNode.GetLeftNode() is None:
            y = theRequestedNode
        else:
            y = self._treeSuccessor(theRequestedNode)
            theRequestedNode.SetValue(y.GetValue())

        if y.GetLeftNode() is not None:
            x = y.GetLeftNode()
        else:
            x = y.GetRightNode()
        if x is not None:
            x.SetParentNode(y.GetParentNode())

        # Which child is y to update his father..
        if y.GetParentNode() is not None:
            if y == y.GetParentNode().GetLeftNode():
                y.GetParentNode().SetLeftNode(x)
            else:
                y.GetParentNode().SetRightNode(x)
        else:
            self._root = x

        return y

    def findMinimum(self, node=None):
        if self.isEmpty():
            return None
        elif node is None:
            node = self.getRoot()

        while node.GetLeftNode():
            node = node.GetLeftNode()

        return node.GetValue()

    def findMaximum(self, node = None):
        if self.isEmpty():
            return None
        elif node is None:
            node = self.getRoot()

        while node.GetRightNode():
            node = node.GetRightNode()

        return node.GetValue()

    def _treeSuccessor(self, node):
        if node.GetRightValue() is not None:
            return self.findMinimum(node.GetRightValue())
        y = node.GetParentNode()

        while y is not None and node == y.GetRightNode():
            node = y
            y = y.GetParentNode()

        return y

    def insert(self, value):
        theNewNodeParent = None
        newNode = TreeNode(value)
        iterator = self._root
        while iterator is not None:
            theNewNodeParent = iterator
            if value < iterator.GetValue():
                iterator = iterator.GetLeftNode()
            else:
                iterator = iterator.GetRightNode()
        newNode.SetParentNode(theNewNodeParent)

        if theNewNodeParent is None:
            self._root = newNode
        elif newNode.GetValue() < theNewNodeParent.GetValue():
            theNewNodeParent.SetLeftNode(newNode)
        else:
            theNewNodeParent.SetRightNode(newNode)
        return newNode


