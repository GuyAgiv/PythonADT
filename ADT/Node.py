class Node:

    # The constructor of the Node class
    def __init__(self, value=None, nextNode=None):
        self.__value = value
        self.__nextNode = nextNode

    # Value Getter
    def GetValue(self):
        return self.__value

    # Value Setter
    def SetValue(self, value):
        self.__value = value

    # NextNode Getter
    def GetNextNode(self):
        return self.__nextNode

    # NextNode Setter
    def SetNextNode(self, newNextNode):
        self.__nextNode = newNextNode
