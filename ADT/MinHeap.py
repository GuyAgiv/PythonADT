from ADT.BinaryHeap import *

class MinHeap(BinaryHeap):

    def __init__(self):
        super(MinHeap, self).__init__()


    def _comparator(self, node1, node2):
        return node1 > node2

    def extractMin(self):
        if self.getHeapSize() == 0:
            raise BufferError('Heaps underflow!')
        minValue = self.getHeapList()[0]

        # Putting the last element in the root node.
        self.getHeapList()[0] = self.getHeapList()[-1]

        del self.getHeapList()[-1]
        if self.getHeapSize() > 0:
            self._heapifyDown(0)

        return minValue

