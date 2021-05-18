# Node class for develping Linked list
class Node:

	def __init__(self, data=None, left=None, right=None):
		self._data = data
		self._left = left
		self._right = right

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

	def __str__(self):
		return f'(data: {self._data} ---- left: {self._left} ----- right: {self._right})'



class BST:

	def __init__(self, root=None):
		self.root = None

	# insert operation
	def insert(self, value):

		if self.lookup(value):
			return None

		if self.root == None:
			self.root = Node(value)
		else:
			curr_node = self.root

			while 1:

				if curr_node.data < value:

					if not curr_node.right:
						curr_node.right = Node(value)
						break
					curr_node = curr_node.right
				elif curr_node.data > value:
					if not curr_node.left:
						curr_node.left = Node(value)
						break
					curr_node = curr_node.left
		print(f'inserted: {value}')

		return self

	# lookup operation
	def lookup(self, value):
		if self.root == None:
			return False
		else:
			curr_node = self.root
			while 1:
				if curr_node.data == value:
					return True
				elif curr_node.data < value:
					if not curr_node.right:
						return False
					curr_node = curr_node.right
				elif curr_node.data > value:
					if not curr_node.left:
						return False
					curr_node = curr_node.left

	# remove operation
	def remove(self, value):
		# check is root node is empty
		if self.root == None or not self.lookup(value):
			return None

		# parent of current node
		parent_node = curr_node = self.root

		while 1:

			# if match is found
			if curr_node.data == value:

				# if node has two child elements
				if curr_node.right and curr_node.left:

					prev_node = next_node = curr_node
					next_node = next_node.right

					while next_node.left != None:
						prev_node = next_node
						next_node = next_node.left

					if parent_node.right.data == value:
						prev_node.left = next_node.right
						parent_node.right = next_node
						next_node.left = curr_node.left
						next_node.right = curr_node.right
						curr_node.left = None
						curr_node.right = None

					elif parent_node.left.data == value:
						prev_node.left = next_node.right
						parent_node.left = next_node
						next_node.left = curr_node.left
						next_node.right = curr_node.right
						curr_node.left = None
						curr_node.right = None
					break

				# if node has two only right child
				elif curr_node.right:
					if parent_node.left.data == value:
						parent_node.left = curr_node.right
						curr_node.right = None
						curr_node.data = None
					elif parent_node.right.data == value:
						parent_node.right = curr_node.right
						curr_node.right == None
						curr_node.data == None
					break

				# if node has two only left child
				elif curr_node.left:
					if parent_node.right.data == value:
						parent_node.right = curr_node.left
						curr_node.left = None
						curr_node.data = None
					elif parent_node.left.data == value:
						parent_node.left = curr_node.left
						curr_node.left = None
						curr_node.data = None
					break

				# if node is a leaf
				else:
					if parent_node.left.data == value:
						parent_node.left = None
						curr_node.data = None
					elif parent_node.right.data == value:
						parent_node.right == None
						curr_node.data = None
					break

			# if match is not found
			# if current node has value less than value we need to remove
			elif curr_node.data < value:
				# only if right node exist
				if not curr_node.right:
					return None
				# parent node becomes current node
				parent_node = curr_node
				# current node is changed to next right node
				curr_node = curr_node.right
			# if current node has value greater than value we need to remove

			elif curr_node.data > value:
				# only if left node exist
				if not curr_node.left:
					return None
				# parent node becomes current node
				prev_node = curr_node
				# current node is changed to next left node
				curr_node = curr_node.left

		return self

	def __str__(self):
		return f'root: {self.root}'



if __name__ == '__main__':

	tree = BST()

	tree.insert(100)
	tree.insert(-10)
	tree.insert(1000)
	tree.insert(-50)
	tree.insert(-100)
	tree.insert(-20)
	tree.insert(50)
	tree.insert(20)
	tree.insert(10)
	tree.insert(0)
	tree.insert(30)
	tree.insert(25)
	tree.insert(27)
	tree.insert(40)
	tree.insert(35)
	tree.insert(45)

	tree.insert(70)
	tree.insert(60)
	tree.insert(90)
	print(tree.insert(80))
	print()
	print(tree.remove(50))

	# print(tree.lookup(6))
