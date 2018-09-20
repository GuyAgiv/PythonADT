from abc import ABCMeta,abstractmethod
from ADT.TreeNode import *

class BinaryTree(object):
    __metaclass__ = ABCMeta

    PRINTSTYLE_INORDER = 1
    PRINTSTYLE_POSTORDER = 2
    PRINTSTYLE_PREORDER = 3

    def __init__(self, root=None):
        self._root = root

    # Basics operations each binary tree have to override
    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass



    # Root getters & setters

    def getRoot(self):
        return self._root

    def setRoot(self, newRoot):
        self._root = newRoot

    # Check if tree is empty

    def isEmpty(self):
        return not bool(self._root)


    # Print methods

    def PrintTree(self, printStyleFlag = None):
        iterator = self._root
        if printStyleFlag == 2:
            self._printPostorder(iterator)
        elif printStyleFlag == 3:
            self._printPreorder(iterator)
        elif printStyleFlag is None or printStyleFlag == 1:
            self._printInorder(iterator)
        else:
            raise AttributeError("Print style flag value doesnt exist!")

    def _printInorder(self, iterator):
        if iterator is None:
            return
        else:
            self._printInorder(iterator.GetLeftNode())
            print iterator.GetValue()
            self._printInorder(iterator.GetRightNode())

    def _printPreorder(self, iterator):
        if iterator is None:
            return
        else:
            print iterator.GetValue()
            self._printPreorder(iterator.GetLeftNode())
            self._printPreorder(iterator.GetRightNode())

    def _printPostorder(self, iterator):
        if iterator is None:
            return
        else:
            self._printPostorder(iterator.GetLeftNode())
            self._printPostorder(iterator.GetRightNode())
            print iterator.GetValue()


