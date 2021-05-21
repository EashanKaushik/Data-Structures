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
