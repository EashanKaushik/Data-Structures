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

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

def mirror(root):
	if root:
		mirror(root.left)
		mirror(root.right)
		root.left, root.right = root.right, root.left

if __name__ == '__main__':
	tree = Node(2)
	tree.left = Node(0)
	tree.left.left = Node(-5)
	tree.left.right = Node(1)
	tree.right = Node(10)
	tree.right.left = Node(5)
	tree.right.right = Node(15)

	inorder(tree)
	mirror(tree)
	inorder(tree)
