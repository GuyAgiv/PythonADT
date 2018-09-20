from ADT import *

'''
Dear inspector ,i tried to do my best
hopefully you'll like it.
there are some code snippets
so you can easily see how the library works..
some of the classes are abstract classes and were made to prevent code duplications and more reuseable code.

Best, Guy Agiv
'''

'''
Binary Tree is an abstract class which have 3 constants
for ordering the print style ( Inorder/Preorder/Postorder ) 
so whenever you want to print in different style ,
please call the base class BinaryTree.PRINT_<YOUR CHOSEN STYLE>
no matter if it AVLTree / Binary Search Tree
by default , INORDER print style is set on.
see example below..
thank you!

'''
##### Binary Search Tree #######

#   AVLTree works the same but behind the scenes using a rotations methods to prevent unbalanced tree

# x = BinarySearchTree()
#
# x.insert(3)
# x.insert(9)
# x.insert(13)
# x.insert(1)
# x.insert(23)
#
# z = x.findMinimum()
#
# y = x.findMaximum()
#
# x.remove(13)
#
# x.PrintTree(BinaryTree.PRINTSTYLE_INORDER)
#
# print 'Maximum is', y, 'Minimum is ', z


##### Linked List #######

myLinkedList = LinkedList()

myLinkedList.insert(9)
myLinkedList.insert(3)
myLinkedList.insert(4)

g = myLinkedList.length()

myLinkedList.removeNodeByValue(9)
myLinkedList.removeFromHead()
myLinkedList.isExist(9)
myLinkedList.consolePrint()

myLinkedList.headInsert(199)

print myLinkedList


##### MaxHeap #######

#Same as MinHeap, both of them inherit from BinaryHeap

myMaxHeap = MaxHeap()

myMaxHeap.getHeapList()

myMaxHeap.insert(3)

#....


##### Stack #######

myStack = Stack()

myStack.push(4)
myStack.push(13)

topElement = myStack.peek()

print myStack

##### TwoThree Tree #######

ttTree = TwoThreeTree()

ttTree.insert(13)
ttTree.preorder()
ttTree.search(13)
