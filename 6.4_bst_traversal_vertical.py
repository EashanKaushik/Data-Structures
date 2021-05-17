from classes.binary_search_tree import Node, BST
from classes.queue import Queue


class BSTVertical(BST):
	"""docstring for BSTAdvance"""
	def __init__(self):
		super(BSTVertical, self).__init__()

	# Vertical Traversal
	def vertical_traversal(self):
		line_map = dict()
		queue = Queue()
		
		queue.queue([0, self.root])
		line_map[0] = [self.root.data]

		while not queue.is_empty():
			
			curr_value, curr_node = tuple(queue.dequeue())

			if curr_node.left:
				queue.queue([curr_value - 1, curr_node.left])

				if curr_value - 1 in line_map.keys():
					line_map[curr_value - 1].append(curr_node.left.data)
				else:
					line_map[curr_value - 1] = [curr_node.left.data]
			
			if curr_node.right:
				queue.queue([curr_value + 1, curr_node.right])

				if curr_value + 1 in line_map.keys():
					line_map[curr_value + 1].append(curr_node.right.data)
				else:
					line_map[curr_value + 1] = [curr_node.right.data]

		print(line_map)
		for key in sorted(line_map.keys()):
			for value in line_map[key]:
				print(value)


if __name__ == '__main__':
	tree = BSTVertical()

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

	tree.vertical_traversal()