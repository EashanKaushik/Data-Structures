from classes.binary_search_tree import Node, BST
from classes.stack import Stack
from classes.queue import Queue

class BSTExtra(BST):
	"""docstring for BSTAdvance"""
	def __init__(self):
		super(BSTExtra, self).__init__()

	def height_recursion(self,root):

		if not root:
			return 0
		else:
			lh = self.height_recursion(root.left)
			rh = self.height_recursion(root.right)
			h = max(lh, rh) + 1
			return h

	# height using recursion
	def height(self):

		if not self.root:
			return 0
		else:
			lh = self.height_recursion(self.root.left)
			rh = self.height_recursion(self.root.right)
			h = max(lh, rh) + 1
			return h

	# level order count
	def level_order_count(self):

		if not self.root:
			return 0

		queue = Queue()
		queue.queue(self.root)
		count = 0

		while not queue.is_empty():
			curr_node = queue.dequeue()
			count += 1

			if curr_node.left:
				queue.queue(curr_node.left)

			if curr_node.right:
				queue.queue(curr_node.right)

		return count

	# inorder count
	def count(self):

		if not self.root:
			return 0

		stack = Stack()
		curr_node = self.root
		count = 0

		while not stack.is_empty() or curr_node:

			if curr_node:
				stack.push(curr_node)
				curr_node = curr_node.left
				count += 1
			else:
				curr_node = stack.pop()
				curr_node = curr_node.right

		return count

	# leaf count
	def leaf_count(self):

		if not self.root:
			return 0

		queue = Queue()
		curr_node = self.root
		queue.queue(curr_node)
		count = 0

		while not queue.is_empty():
			curr_node = queue.dequeue()

			if not curr_node.left and not curr_node.right:
				count += 1
			else:
				if curr_node.left:
					queue.queue(curr_node.left)

				if curr_node.right:
					queue.queue(curr_node.right)

		return count

	# boundary traversal
	def boundary_traversal(self):

		if not self.root:
			return
		else:
			print(self.root.data)

		# left side
		curr_node = self.root

		while curr_node.left:
			# if not leaf node
			if curr_node.left.left or curr_node.left.right:
				print(curr_node.left.data)
			curr_node = curr_node.left

		# leaf node
		curr_node = self.root
		stack = Stack()

		while not stack.is_empty() or curr_node:

			if curr_node:
				stack.push(curr_node)
				curr_node = curr_node.left
			else:
				curr_node = stack.pop()
				if not curr_node.left and not curr_node.right:
					print(curr_node.data)
				curr_node = curr_node.right

		# right nodes
		stack = Stack()
		curr_node = self.root

		while curr_node.right:
			if curr_node.right.left or curr_node.right.right:
				stack.push(curr_node.right)
			curr_node = curr_node.right

		while not stack.is_empty():
			print(stack.pop())

	# reverse boundary traversal
	def reverse_boundary_traversal(self):

		if not self.root:
			return
		else:
			print(self.root.data)

		# right nodes
		curr_node = self.root

		while curr_node.right:
			if curr_node.right.left or curr_node.right.right:
				print(curr_node.right.data)
			curr_node = curr_node.right

		# leaf nodes
		stack = Stack()
		curr_node = self.root

		while not stack.is_empty() or curr_node:

			if curr_node:
				stack.push(curr_node)
				curr_node = curr_node.right
			else:
				curr_node = stack.pop()
				if not curr_node.left and not curr_node.right:
					print(curr_node.data)
				curr_node = curr_node.left

		# left nodes
		stack = Stack()
		curr_node = self.root

		while curr_node.left:
			stack.push(curr_node.left.data)
			curr_node = curr_node.left

		while not stack.is_empty():
			print(stack.pop())


if __name__ == '__main__':
	tree = BSTExtra()

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

	tree.reverse_boundary_traversal()
