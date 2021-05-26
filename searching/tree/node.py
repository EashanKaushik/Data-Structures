class Node:
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


def make_tree():
    # root
    root = Node(5)

    # root children
    root.left = Node(3)
    root.right = Node(7)

    # left tree
    root.left.left = Node(2)
    root.left.right = Node(4)

    root.left.left.left = Node(1)
    
    root.left.left.left.left = Node(0)

    # right tree
    root.right.left = Node(6)
    root.right.right = Node(8)

    root.right.right.right = Node(9)

    return root
