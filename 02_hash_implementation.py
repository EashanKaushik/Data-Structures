# Handling collisions using seperate chaining
import random
import copy

class HashTable:

	def __init__(self, size):
		self.data = [[] for _ in range(size)]
		self.keys = [None for _ in range(size)]
		self.size = size
		self.start = 0
	
	def __hash__(self, key):
		hash_value = 0
		for char in key:
			hash_value += ord(char)

		return  hash_value % self.size

	def set(self, key, value):

		hash_value = self.__hash__(key)
		
		self.data[hash_value].append(value)
		self.key_value[hash_value] = hash_value

	def get(self, key):

		hash_value = self.__hash__(key)

		return self.data[hash_value]

	def keys(self):
		return [keys for keys in self.key_value if keys != None]

	def values(self):
		return [values[0] for values in self.data if values]

	def loop_over(self):
		current = 0
		key_list = self.keys()
		while current < len(key_list):
			yield self.data[key_list[current]][0]
			current += 1

	def __str__(self):
		return '[' + ', '.join(map(str, self.keys)) + ']'

	def __repr__(self):
		return self.data


hash_table = HashTable(50)

# print(hash_table.__hash__('abcs'))

hash_table.set('srvgerg', 0)
hash_table.set('srvgerg', 1)
hash_table.set('srvgerg', 2)
hash_table.set('srvgerg', 3)

hash_table.set('srvgeyy', 3)
hash_table.set('srvgty', 45)
hash_table.set('srvrfgg', 345345)



# print(hash_table.get('srvgerg'))
# print(hash_table.keys())
# print(hash_table.values())
# print(dir(HashTable))

vals = hash_table.loop_over()

for val in vals:
	print(val)