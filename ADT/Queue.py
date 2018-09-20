# Implementation Linked list Circular Queue

from ADT.Node import *

class Queue:
    def __init__(self, head = None):
        self.__head = head
        self.__tail = head

    def isEmpty(self):
        return not bool(self.__head)

    def enqueue(self, theValue):
        newNode = Node(theValue)

        if self.isEmpty():
            self.__head = newNode
        else:
            self.__tail.SetNextNode(newNode)

        self.__tail = newNode
        self.__tail.SetNextNode(self.__head)

    def dequeue(self):
        if self.isEmpty():
            raise BufferError("Queue is Empty!!")
        else:
            theDequeuedVal = self.__head.GetValue()

            if self.__head == self.__tail:
                self.__head = self.__tail = None
            else:
                self.__head = self.__head.GetNextNode()
                self.__tail.SetNextNode(self.__head)

            return theDequeuedVal

    def front(self):
        return self.__head.GetValue()


    def printQueue(self):

        if self.__head != None:
            print self.__head.GetValue()
            iterator = self.__head.GetNextNode()
            while iterator is not self.__head and iterator is not None:
                print iterator.GetValue()
                iterator = iterator.GetNextNode()

    def __str__(self):
        queueList = list()
        if self.__head != None:
            queueList.append(self.__head.GetValue())
            iterator = self.__head.GetNextNode()
            while iterator is not self.__head and iterator is not None:
                queueList.append(iterator.GetValue())
                iterator = iterator.GetNextNode()
        return str(queueList)