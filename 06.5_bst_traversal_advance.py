from classes.binary_search_tree import Node, BST
from classes.queue import Queue


class BSTVertical(BST):
	"""docstring for BSTAdvance"""
	def __init__(self):
		super(BSTVertical, self).__init__()

	def top_view(self):

		line_map = dict()
		queue = Queue()

		curr_val = 0
		curr_node = self.root
		line_map[curr_val] = curr_node.data

		queue.queue(curr_val)
		queue.queue(curr_node)

		while not queue.is_empty():
			
			curr_val = queue.dequeue()
			curr_node = queue.dequeue()

			if curr_node.left:
				queue.queue([curr_val - 1, curr_node.left])

				if curr_val - 1 not in line_map.keys():

					line_map[curr_val - 1] = curr_node.left.data

			if curr_node.right:
				queue.queue([curr_val + 1, curr_node.right])

				if curr_val + 1 not in line_map.keys():

					line_map[curr_val + 1] = curr_node.right.data

		for key in sorted(line_map.keys()):

			print(line_map[key])

	def buttom_view(self):

		queue = Queue()
		line_map = dict()

		curr_node = self.root
		curr_val = 0

		queue.queue(curr_val)
		queue.queue(curr_node)

		while not queue.is_empty():
			
			curr_val = queue.dequeue()
			curr_node = queue.dequeue()

			if curr_node.left:
				queue.queue(curr_val - 1)
				queue.queue(curr_node.left)

				line_map[curr_val - 1] = curr_node.left.data

			if curr_node.right:
				queue.queue(curr_val + 1)
				queue.queue(curr_node.right)

				line_map[curr_val + 1] = curr_node.right.data

		print(line_map)
		for key in sorted(line_map.keys()):
			print(line_map[key])

	def right_view(self):

		queue = Queue()
		queue.queue(self.root)
		count = queue.size()

		while not queue.is_empty():

			curr_node = queue.dequeue()
			count -= 1

			if curr_node.left:
				queue.queue(curr_node.left)
			
			if curr_node.right:
				queue.queue(curr_node.right)

			if count == 0:

				print(curr_node.data)
				count = queue.size()

	def left_view(self):

		queue = Queue()
		queue.queue(self.root)
		count = queue.size()

		while not queue.is_empty():

			curr_node = queue.dequeue()
			count -= 1
			
			if curr_node.right:
				queue.queue(curr_node.right)

			if curr_node.left:
				queue.queue(curr_node.left)
			

			if count == 0:

				print(curr_node.data)
				count = queue.size()

	def diagonal_view(self):

		queue = Queue()
		curr_node = self.root
		curr_val = 0
		line_map = dict()

		queue.queue(curr_val)
		queue.queue(curr_node)
		line_map[curr_val] = [curr_node.data]

		while not queue.is_empty():
			curr_val = queue.dequeue()
			curr_node = queue.dequeue()

			if curr_node.left:
				queue.queue(curr_val + 1)
				queue.queue(curr_node.left)

				if curr_val + 1 in line_map.keys():
					line_map[curr_val + 1].append(curr_node.left.data)
				else:
					line_map[curr_val + 1] = [curr_node.left.data]

			if curr_node.right:
				queue.queue(curr_val)
				queue.queue(curr_node.right)

				line_map[curr_val].append(curr_node.right.data)

		print(line_map)


		for key in sorted(line_map.keys()):

			for val in line_map[key]:

				print(val)



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

	tree.buttom_view()