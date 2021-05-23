class Node:
	def __init__(self, data=None, left=None, right=None):
		self._left = left
		self._data = data
		self._right = right

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

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, left):
		self._data = data


def spiral(root):
    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) > 0 or len(stack2) > 0:
        while len(stack1) > 0:

            curr_node = stack1.pop()
            print(curr_node.data)

            if curr_node.left:
                stack2.append(curr_node.left)

            if curr_node.right:
                stack2.append(curr_node.right)

        while len(stack2) > 0:

            curr_node = stack2.pop()
            print(curr_node.data)

            if curr_node.right:
                stack1.append(curr_node.right)

            if curr_node.left:
                stack1.append(curr_node.left)

def spiral_reverse(root):
    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) > 0 or len(stack2) > 0:
        while len(stack1) > 0:

            curr_node = stack1.pop()
            print(curr_node.data)

            if curr_node.right:
                stack2.append(curr_node.right)
            if curr_node.left:
                stack2.append(curr_node.left)

        while len(stack2) > 0:

            curr_node = stack2.pop()
            print(curr_node.data)

            if curr_node.left:
                stack1.append(curr_node.left)

            if curr_node.right:
                stack1.append(curr_node.right)


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.right = Node(7)
    tree.right.left = Node(18)
    tree.right.right.right = Node(8)
    tree.left.right.left = Node(17)
    tree.left.right.right = Node(6)
    tree.left.right.left.left = Node(19)

    spiral_reverse(tree)
