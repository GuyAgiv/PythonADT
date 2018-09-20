import sys

from ADT.Node import *

class LinkedList:

    # Constructor of Linked List
    def __init__(self, head = None):
        self.__head = head

    # Insertion operation ( insert the value to the beginning of the List )
    def headInsert(self, value):
        newNode = Node(value)
        newNode.SetNextNode(self.__head)
        self.__head = newNode

    def length(self):
        iterator = self.__head
        counter = 0

        while iterator:
            counter += 1
            iterator = iterator.GetNextNode()

        return counter

    def isExist(self, theValue):
        iterator = self.__head
        isExist = False

        while iterator and not isExist:
            if iterator.GetValue() == theValue:
                isExist = True
            else:
                iterator = iterator.GetNextNode()

        return isExist

    def removeNodeByValue(self, theValue):
        iterator = self.__head
        prevNode = None
        isFound = False

        isExist = self.isExist(theValue)

        if isExist == True:
            if self.__head.GetValue() == theValue:
                self.__head = self.__head.GetNextNode()
            else:
                while not isFound:
                    if iterator.GetValue() == theValue:
                        isFound = True
                    else:
                        prevNode = iterator
                        iterator = iterator.GetNextNode()
                prevNode.SetNextNode(iterator.GetNextNode())
        else:
            raise ValueError("Requested node to delete was'nt found!")

    def consolePrint(self):
        iterator = self.__head
        if self.length() > 0:
            while iterator:
                sys.stdout.write(str(iterator.GetValue()))
                if iterator.GetNextNode():
                    sys.stdout.write(' -> ')
                iterator = iterator.GetNextNode()
        else:
            raise RuntimeError('Sorry but list is empty!')

    def removeFromHead(self):
        theDeletedNode = self.__head.GetValue()
        self.__head = self.__head.GetNextNode()
        return theDeletedNode

    def getHead(self):
        return self.__head

    def insert(self, value):
        if self.__head == None:
            self.headInsert(value)
            self.__tail = self.getHead()
        else:
            iterator = self.__head

            while iterator.GetNextNode() != None:
                iterator = iterator.GetNextNode()

            newNode = Node(value)

            iterator.SetNextNode(newNode)
    def __str__(self):
        iterator = self.__head
        linkedList = list()
        while iterator:
            linkedList.append(iterator.GetValue())
            iterator = iterator.GetNextNode()
        return str(linkedList)


