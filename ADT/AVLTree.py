from ADT.BinarySearchTree import *

class AVLTree(BinarySearchTree):

    def __init__(self):
        super(AVLTree,self).__init__()

    def insert(self, value):
        theNewNode = super(AVLTree, self).insert(value)
        self._examineInsert(theNewNode)

    def _examineInsert(self, theNewNode, path=[]):
        if theNewNode.GetParentNode() == None:
            return
        path = [theNewNode] + path

        leftHeight = self.getNodeHeight(theNewNode.GetParentNode().GetLeftNode())
        rightHeight = self.getNodeHeight(theNewNode.GetParentNode().GetRightNode())

        if abs(leftHeight - rightHeight) > 1:
            path = [theNewNode.GetParentNode()] + path
            self._rebalanceNode(path[0], path[1], path[2])
            return

        theNewHeight = 1 + theNewNode.GetHeight()
        if theNewHeight > theNewNode.GetParentNode().GetHeight():
            theNewNode.GetParentNode().SetHeight(theNewHeight)

        self._examineInsert(theNewNode.GetParentNode(), path)


    def getNodeHeight(self, node):
        if node == None:
            return 0
        return node.getNodeHeight()

    def _examineRemove(self, currentNode):
        if currentNode == None:
            return

        leftHeight = self.getNodeHeight(currentNode.GetLeftNode())
        rightHeight = self.getNodeHeight(currentNode.GetRightNode())

        if abs(leftHeight - rightHeight) > 1:
            y = self._getTallerChild(currentNode)
            x = self._getTallerChild(y)
            self._rebalanceNode(currentNode, y, x)

        self._examineRemove(currentNode.GetParentNode())

    def _rebalanceNode(self, z, y, x):
        if y == z.GetLeftNode() and x == y.GetLeftNode():
            self._rightRotate(z)
        elif y == z.GetLeftNode() and x == y.GetRightNode():
            self._leftRotate(y)
            self._rightRotate(z)
        elif y == z.GetRightNode() and x == y.GetRightNode():
            self._leftRotate(z)
        elif y == z.GetRightNode() and x == y.GetLeftNode():
            self._rightRotate(y)
            self._leftRotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def _rightRotate(self, z):
        sub_root = z.GetParentNode()
        y = z.GetLeftNode()
        t3 = y.GetRightNode()
        y.SetRightNode(z)
        z.SetParentNode(y)
        z.SetLeftNode(t3)
        if t3 != None:
            t3.SetParentNode(z)
        y.SetParentNode(sub_root)
        if y.GetParentNode() == None:
            self.setRoot(y)
        else:
            if y.GetParentNode().GetLeftNode() == z:
                y.GetParentNode().SetLeftNode(y)
            else:
                y.GetParentNode().SetRightNode(y)
        z.SetHeight(1 + max(self.getNodeHeight(z.GetLeftNode()), self.getNodeHeight(z.GetRightNode())))
        y.SetHeight(1 + max(self.getNodeHeight(y.GetLeftNode()), self.getNodeHeight(y.GetRightNode())))

    def _leftRotate(self, z):
        sub_root = z.GetParentNode()
        y = z.GetRightNode()
        t2 = y.GetLeftNode()
        y.SetLeftNode(z)
        z.SetParentNode(y)
        z.SetRightNode(t2)
        if t2 != None:
            t2.SetParentNode(z)
        y.SetParentNode(sub_root)
        if y.GetParentNode() == None:
            self.setRoot(y)
        else:
            if y.GetParentNode().GetLeftNode() == z:
                y.GetParentNode().SetLeftNode(y)
            else:
                y.GetParentNode().SetRightNode(y)
        z.SetHeight(1 + max(self.getNodeHeight(z.GetLeftNode()), self.getNodeHeight(z.GetRightNode())))
        y.SetHeight(1 + max(self.getNodeHeight(y.GetLeftNode()), self.getNodeHeight(y.GetRightNode())))


    def _getTallerChild(self, CurrentNode):
        left = self.getNodeHeight(CurrentNode.GetLeftNode())
        right = self.getNodeHeight(CurrentNode.GetRightNode())
        return CurrentNode.GetLeftNode() if left >= right else CurrentNode.GetRightNode()







