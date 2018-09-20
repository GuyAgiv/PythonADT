from abc import ABCMeta, abstractmethod
from math import floor

class BinaryHeap(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._heapArr = list()
        self._heapSize = self.getHeapList().__len__()

    def getHeapList(self):
        return self._heapArr

    def getParent(self, nodeIdx):
        return int(floor((nodeIdx-1) / 2))

    def getHeapSize(self):
        return self._heapArr.__len__()

    def insert(self, value):
        self.getHeapList().append(value)
        self._heapifyUp(self.getHeapSize() - 1)

    def _heapifyUp(self, newNodeIdx):

        while newNodeIdx > 0 and  self._comparator(self.getHeapList()[self.getParent(newNodeIdx)], self.getHeapList()[newNodeIdx]):
            self.getHeapList()[self.getParent(newNodeIdx)], self.getHeapList()[newNodeIdx] = self.getHeapList()[newNodeIdx], self.getHeapList()[self.getParent(newNodeIdx)]
            newNodeIdx = self.getParent(newNodeIdx)


    #Using that method to check whether the idx of the newnode is compatible and greater/smaller than her childs..
    def _heapifyDown(self, newNodeIdx):
        leftChild = newNodeIdx * 2 + 1
        rightChild = newNodeIdx * 2 + 2

        # requiredIdx means it can be the largest value idx or smallest value idx depends of which heap we chosen max or min
        requiredIdx = newNodeIdx

        if leftChild <= self.getHeapSize() - 1 and self._comparator(self.getHeapList()[newNodeIdx], self.getHeapList()[leftChild]):
            requiredIdx = leftChild
        if rightChild <= self.getHeapSize() - 1 and self._comparator(self.getHeapList()[requiredIdx], self.getHeapList()[rightChild]):
            requiredIdx = rightChild


        if requiredIdx != newNodeIdx:
            self.getHeapList()[requiredIdx], self.getHeapList()[newNodeIdx] = self.getHeapList()[newNodeIdx], self.getHeapList()[requiredIdx]
            self._heapifyDown(requiredIdx)


    def remove(self, value):
        if value not in self.getHeapList():
            raise ValueError("The heap doesnt include that value!")
        else:

            for idx in range(0, self.getHeapSize()):
                if value == self.getHeapList()[idx]:
                    break

            # special case when we want to delete the last element...
            if idx == self.getHeapSize() - 1:
                del self.getHeapList()[-1]
            else:
                self.getHeapList()[idx] = self.getHeapList()[-1]
                del self.getHeapList()[-1]

                while idx > 0 and self._comparator(self.getHeapList()[self.getParent(idx)], self.getHeapList()[idx]):
                    self.getHeapList()[self.getParent(idx)], self.getHeapList()[idx] = self.getHeapList()[idx], self.getHeapList()[self.getParent(idx)]
                    idx = self.getParent(idx)

                self._heapifyDown(idx)


    @abstractmethod
    def _comparator(self, object1, object2):
        pass

    def __str__(self):
        return str(self.getHeapList())