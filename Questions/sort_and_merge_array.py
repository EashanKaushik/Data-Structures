# array1 = [0,1,3,5,7]
# array2 = [2,4,6,8]

# 
# def merge_and_sort(array1, array2):

# 	array1_index = 0
# 	array2_index = 0
# 	temp = 0

# 	for array1_index in range(len(array1)): # O(n^3) however space complexity O(1)
# 		if array2[array2_index] < array1[array1_index]:
# 			temp = array2[array2_index]
# 			array2[array2_index] = array1[array1_index]
# 			array1[array1_index] = temp

# 			array2_index = 0

# 			# Insertion Sort
# 			for i in range(1, len(array2)):
# 				key = array2[i]
# 				j = i-1
# 				while j >= 0 and key < array2[j] :
# 					array2[j + 1] = array2[j]
# 					j -= 1
# 				array2[j + 1] = key

# 	print(array1, array2)

# merge_and_sort(array2 ,array1)

# Gap Algorithm
array1 = [1, 4, 7, 8, 10]
array2 = [2, 3, 9]
import math
def merge_and_sort(array1, array2):

	len_array1 = len(array1)
	len_array2 = len(array2)

	gap = math.ceil((len_array1 + len_array2) / 2)
	gap_integer = (len_array1 + len_array2) / 2
	print(f'Initial: {gap}')
	while (gap_integer >= 1):

		start = 0
		end = start + gap
		print(f' Outer: {start}, {gap}, {end} ' )
		while(end < len_array1 + len_array2):
			# print(2)
			print(f' Inner: {start}, {gap}, {end} ' )

			if start < len_array1:
				
				if end < len_array1:
					if array1[start] > array1[end]:
						temp = array1[start]
						array1[start] = array1[end]
						array1[end] = temp
				elif end >= len_array1:
					if array1[start] > array2[end - len_array1]:
						temp = array1[start]
						array1[start] = array2[end - len_array1]
						array2[end - len_array1] = temp

			elif start >= len_array1:

				if array2[start - len_array1] > array2[end - len_array1]:
					temp = array2[start - len_array1]
					array2[start - len_array1] = array2[end - len_array1]
					array2[end - len_array1] = temp


			start = start + 1
			end = start + gap
		gap_integer = gap / 2
		gap = math.ceil(gap/2)

	print(array1, array2)

merge_and_sort(array2 ,array1)

