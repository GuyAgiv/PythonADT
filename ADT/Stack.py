from LinkedList import *

class Stack:

    # Constructor of Linked List
    def __init__(self):
        self._theStack = LinkedList()

    def isEmpty(self):
        return self._theStack.length() == 0

    def push(self, theValue):
        self._theStack.headInsert(theValue)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty!")
        else:
            return self._theStack.removeFromHead()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty!")
        else:
            return self._theStack.getHead().GetValue()

    def __str__(self):
        print '--The Stack--'
        stackList = list()
        while not self.isEmpty():
            stackList.append(self.pop())
        for i in reversed(stackList):
            self.push(i)

        return str(stackList)
