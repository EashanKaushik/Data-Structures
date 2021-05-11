# from bigO import BigO

def merge_sorted_array(arr1, arr2):
	len_arr1 = len(arr1)
	len_arr2 = len(arr2)
	sorted_array = list()

	if( len_arr2 > len_arr1):
		while(current_1 != len_arr1): # O(n)
			if arr1[current_1] < arr2[current_2]:
					sorted_array.append(arr1[current_1])
					current_1 += 1
			else:
				sorted_array.append(arr2[current_2])
				current_2 += 1

		sorted_array.extend(arr2[current_2:]) # O(k)
	else:
		while(current_2 != len_arr2):
			if arr1[current_1] < arr2[current_2]:
					sorted_array.append(arr1[current_1])
					current_1 += 1
			else:
				sorted_array.append(arr2[current_2])
				current_2 += 1
		sorted_array.extend(arr1[current_1: ])
	print(sorted_array)

merge_sorted_array([1, 3, 5, 7], [2, 4, 6, 8, 9, 10])
merge_sorted_array( [2, 4, 6, 8, 9, 10], [1, 3, 5, 7])

# lib = BigO()

# lib.test(merge_sorted_array, "random")