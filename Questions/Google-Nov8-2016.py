# [1, 2, 3, 4] sum = 8   FALSE
# [1, 2, 4, 4] sum = 8	 TRUE

## Sorted
arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 4, 4]

# O(n^2)
# def pair_sum_array(arr):
# 	for index in range(0, len(arr)):

# 		for index_inner in range(index + 1, len(arr)):
# 			print(index, index_inner)

# 			if arr[index] + arr[index_inner] == 8:
# 				return True

# 	return False

# print(pair_sum_array(arr1))
# print(pair_sum_array(arr2))


# O(n) 
# def pair_sum_array(arr):
# 	low = 0
# 	high = len(arr)-1
# 	while(low < high):
# 		pair_sum = arr[low] + arr[high]

# 		if pair_sum == 8:
# 			return True
# 		elif pair_sum < 8:
# 			low += 1
# 		else:
# 			high +=1

# 	return False

# print(pair_sum_array(arr1))
# print(pair_sum_array(arr2))

## if not sorted

# O(n)
def pair_sum_array(arr):
	lookup = set()

	for value in arr:
		if 8 - value in lookup:
			return True
		else:
			lookup.add(8-value)
	return False

print(pair_sum_array(arr1))
print(pair_sum_array(arr2))