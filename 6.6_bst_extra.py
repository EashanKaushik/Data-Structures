from classes.binary_search_tree import Node, BST
from classes.stack import Stack

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

	def height(self):

		if not self.root:
			return 0
		else:
			lh = self.height_recursion(self.root.left)
			rh = self.height_recursion(self.root.right)
			h = max(lh, rh) + 1
			return h



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

	print(tree.height())