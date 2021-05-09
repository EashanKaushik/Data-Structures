class UserDefinedStaticArray:

	def __init__(self, length):
		self.current = 0
		self.length = length
		self.data = list()

	# @property
	def get_data_value(self, index):
		return self.data[index]

	# @data_value.setter
	def set_data_value(self, index, value):
		if self.length > index:
			self.current += 1
			self.data[index] = value
		elif self.length > index and self.current < self.length:
			self.current += 1
			self.data[index] = value
		else:
			print('Array Overflow')

	def push(self,value):
		if self.current < self.length:
			self.data.append(value)
			self.current += 1
		
	def pop(self):
		if self.current > 0:
			self.current -= 1
			self.data.pop()
		else:
			print('Index Error')

	def insert(self, index, value):
		if self.length > index and self.current < self.length:
			self.current += 1
			self.data.insert(index, value)
		else:
			print('Array Overflow')

	def remove(self, value):
		if self.data.count(value) >= 1 and self.current > 0:
			self.current -= 1
			self.data.remove(value)
		else:
			print('Not Found')

	def __str__(self):
		return '[' + ', '.join(map(str, self.data)) + ']'

	def __repr__(self):
		return self.datas

	def __len__(self):
		return self.length


class UserDefinedDynamicArray:

	def __init__(self):
		self.length = 0
		self.data = list()

	def push(self,value):
		self.data.append(value)
		self.length += 1

		
	def pop(self):
		if self.length > 0:
			self.length -= 1
			self.data.pop()

	def insert(self, index, value):
		self.length += 1
		self.data.insert(index, value)
		
	def remove(self, value):
		if self.data.count(value) >= 1 and self.length > 0:
			self.length -= 1
			self.data.remove(value)
		else:
			print('Not Found')

	def __str__(self):
		return '[' + ', '.join(map(str, self.data)) + ']'

	def __repr__(self):
		return self.datas

	def __len__(self):
		return self.length


if __name__ == '__main__':
	arr = UserDefinedStaticArray(5)
	arr.push(1)
	arr.push(2)
	arr.push(3)
	arr.push(4)
	arr.push(5)
	arr.push(5)
	arr.pop()
	arr.pop()
	arr.insert(0, 100)
	arr.push(99)
	arr.remove(1)
	arr.push(5)
	arr.remove(100)
	arr.pop()
	arr.push(212)
	arr.push(5)
	print(arr)
	print(len(arr))
	print(arr.get_data_value(1))
	arr.set_data_value(0, 199999)
	print(arr)

