array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

#  Counting Sort
# 1
# def counting_sort(array):
# 	zero = 0
# 	one = 0
# 	two = 0

# 	for value in array: # O(n)
# 		if value == 0:
# 			zero += 1
# 		elif value == 1:
# 			one += 1
# 		elif value == 2:
# 			two += 1
# 		else:
# 			print('Error in input')
# 			break

# 	new_array = list()

# 	new_array.extend([0] * zero) # O(k)
# 	new_array.extend([1] * one) # O(p)
# 	new_array.extend([2] * two) # O(m)

# 	print(new_array)

# counting_sort(array)

# 2
# def counting_sort(array):

# 	max_element = max(array) # O(n)

# 	new_array = [0] * len(array)
# 	counts = [0] * (max_element + 1)

# 	for value in array: # O(n)
# 		counts[value] += 1

# 	for index in range(1, len(counts)): # O(n)
# 		counts[index] += counts[index - 1]

# 	for value in array: # O(n)
# 		new_array[counts[value]-1] = value
# 		counts[value] -= 1

# 	print(new_array)
# counting_sort(array)

# Dutch National Flag Algorithm

def dutch_national_flag(array):
	low = 0
	mid = 0
	high = len(array) - 1
	temp = None 
	while mid <= high:
		if array[mid] == 0:
			temp = array[mid]
			array[mid] = array[low]
			array[low] = temp
			mid += 1
			low += 1
		elif array[mid] == 1:
			mid += 1
		elif array[mid] == 2:
			temp = array[mid]
			array[mid] = array[high]
			array[high] = temp
			high -= 1

	print(array)

dutch_national_flag(array)