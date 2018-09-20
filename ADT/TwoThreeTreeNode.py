
class TwoThreeTreeNode:
    def __init__(self, value, parentNode=None):
        self._valuesList = list([value])
        self._parentNode = parentNode
        self._childsList = list()

    def __str__(self):
        if self._parentNode:
            return str(self._parentNode._valuesList) + ' : ' + str(self._valuesList)

    # Less than .. python method. for comparisons..
    def __lt__(self, node):
        return self._valuesList[0] < node._valuesList[0]


    ## Getters


    def GetParentNode(self):
        return self._parentNode

    def GetValuesList(self):
        return self._valuesList

    def GetChildsList(self):
        return self._childsList

    ###

    def isLeaf(self):
        return len(self._childsList) == 0

    # merge new_node sub-tree into self node
    def mergeSubtree(self, newNode):

        # self node being set to be the parent of all the new node childs.
        for child in newNode._childsList:
            child._parentNode = self

        # merging values list of new node to self's values list
        self._valuesList.extend(newNode._valuesList)
        self._valuesList.sort()
        # merging the same but for the childs list
        self._childsList.extend(newNode._childsList)

        if len(self._childsList) > 1:
            self._childsList.sort()

        if len(self._valuesList) > 2:
            self._split()

    # find correct node to insert new node into tree
    def insert(self, newNode):

        # leaf node - add data to leaf and rebalance tree
        if self.isLeaf():
            self.mergeSubtree(newNode)

        # not leaf - find correct child to descend, and do recursive insert
        elif newNode._valuesList[0] > self._valuesList[-1]:
            self._childsList[-1].insert(newNode)
        else:
            for i in range(0, len(self._valuesList)):
                if newNode._valuesList[0] < self._valuesList[i]:
                    self._childsList[i].insert(newNode)
                    break

    # 3 items in node, split into new sub-tree and add to parent
    def _split(self):

        leftChild = TwoThreeTreeNode(self._valuesList[0], self)
        rightChild = TwoThreeTreeNode(self._valuesList[2], self)

        if self._childsList:
            self._childsList[0]._parentNode = leftChild
            self._childsList[1]._parentNode = leftChild
            self._childsList[2]._parentNode = rightChild
            self._childsList[3]._parentNode = rightChild
            leftChild._childsList = [self._childsList[0], self._childsList[1]]
            rightChild._childsList = [self._childsList[2], self._childsList[3]]


        self._childsList = [leftChild]
        self._childsList.append(rightChild)
        self._valuesList = [self._valuesList[1]]

        # now have new sub-tree, self. need to add self to its parent node
        if self._parentNode:
            if self in self._parentNode._childsList:
                self._parentNode._childsList.remove(self)

            self._parentNode.mergeSubtree(self)

        else:
            leftChild._parentNode = self
            rightChild._parentNode = self

    # find an item in the tree; return item, or False if not found

    def find(self, value):
        # print ("Find " + str(item))
        if value in self._valuesList:
            return value
        elif self.isLeaf():
            return False
        elif value > self._valuesList[-1]:
            return self._childsList[-1].find(value)
        else:
            for i in range(len(self._valuesList)):
                if value < self._valuesList[i]:
                    return self._childsList[i].find(value)

    def _remove(self, item):
        pass

    # print internalPreorder traversal
    def internalPreorder(self):
        print (self)
        for child in self._childsList:
            child.internalPreorder()


