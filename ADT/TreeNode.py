class TreeNode(object):
    # The constructor of the Tree Node class
    def __init__(self, value=None, leftNode = None, rightNode = None, parentNode = None):
        self._value = value
        self._leftNode = leftNode
        self._rightNode = rightNode
        self._parentNode = parentNode
        self._height = 1

    # Value Getter
    def GetValue(self):
        return self._value

    # Value Setter
    def SetValue(self, value):
        self._value = value

    # Left node Setter/Getter
    def GetLeftNode(self):
        return self._leftNode

    def SetLeftNode(self, newLeftNode):
        self._leftNode = newLeftNode

    # Right node Setter/Getter

    def GetRightNode(self):
        return self._rightNode

    def SetRightNode(self, newRightNode):
        self._rightNode = newRightNode

    # Parent node Setter/Getter
    def GetParentNode(self):
        return self._parentNode

    def SetParentNode(self, newParentNode):
        self._parentNode = newParentNode

    def GetHeight(self):
        return self._height

    def SetHeight(self, newHeight):
        self._height = newHeight




