from classes.binary_search_tree import Node, BST
from classes.queue import Queue

class BSTAdvance(BST):
	"""docstring for BSTAdvance"""
	def __init__(self):
		super(BSTAdvance, self).__init__()
	# Recursion
	# Inorder
	def inorder_traversal(self):
		
		if self.root:
			self.inorder_traversal_inner(self.root.left)

			print(self.root.data)

			self.inorder_traversal_inner(self.root.right)

	def inorder_traversal_inner(self, root):
		if root:
			self.inorder_traversal_inner(root.left)

			print(root.data)

			self.inorder_traversal_inner(root.right)

	# Preorder
	def preorder_traversal(self):
		
		if self.root:
			print(self.root.data)
			
			self.preorder_traversal_inner(self.root.left)

			self.preorder_traversal_inner(self.root.right)

	def preorder_traversal_inner(self, root):
		if root:
			print(root.data)
			
			self.preorder_traversal_inner(root.left)

			self.preorder_traversal_inner(root.right)

	# Postorder
	def postorder_traversal(self):
		
		if self.root:			
			self.postorder_traversal_inner(self.root.left)

			self.postorder_traversal_inner(self.root.right)
			
			print(self.root.data)

	def postorder_traversal_inner(self, root):
		if root:
			self.postorder_traversal_inner(root.left)

			self.postorder_traversal_inner(root.right)

			print(root.data)

	# Level order
	def levelorder_traversal(self):
		queue = Queue()

		if not self.root:
			return None
		else:
			queue.queue(self.root)

			while not queue.is_empty():

				next_node = queue.dequeue()
				
				print(next_node.data)
				
				if next_node.left:
					queue.queue(next_node.left)
				if next_node.right:
					queue.queue(next_node.right)

if __name__ == '__main__':
	tree = BSTAdvance()

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

	tree.levelorder_traversal()