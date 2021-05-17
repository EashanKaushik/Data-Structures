from classes.binary_search_tree import Node, BST
from classes.stack import Stack

class BSTMedium(BST):
	"""docstring for BSTAdvance"""
	def __init__(self):
		super(BSTMedium, self).__init__()

	def inorder_traversal(self):
		if not self.root:
			return
		else:
			stack = Stack()			
			curr_node = self.root

			while not stack.is_empty() or curr_node:

				if curr_node:
					stack.push(curr_node)
					curr_node = curr_node.left
				else:
					curr_node = stack.pop()
					print(curr_node.data)
					curr_node = curr_node.right

	def preorder_traversal(self):
		if not self.root:
			return
		else:
			stack = Stack()			
			curr_node = self.root

			while not stack.is_empty() or curr_node:

				if curr_node:
					stack.push(curr_node)
					print(curr_node.data)
					curr_node = curr_node.left
				else:
					curr_node = stack.pop()
					curr_node = curr_node.right

	def postorder_traversal(self):
		curr_node = self.root
		stack = Stack()
		output = Stack()

		while not stack.is_empty() or curr_node:
				
			if curr_node:
				output.push(curr_node.data)
				stack.push(curr_node)
				curr_node = curr_node.right
			else:
				curr_node = stack.pop()
				curr_node = curr_node.left

		while not output.is_empty():
			
			print(output.pop())


if __name__ == '__main__':
	tree = BSTMedium()

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

	tree.postorder_traversal()