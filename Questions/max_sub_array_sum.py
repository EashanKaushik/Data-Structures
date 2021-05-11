# array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# array = [-1, -2, -3, 9]
# array = [-1, -2, -3, 9, -3]
# array = [-1, -2, -3, 9, 11]
array = [-2, -1]
 

# maximum = {'maxi': 0, 'start': None, 'end': None } # {max: __, start:___, end:___}
# sumi = 0

# for index in range(len(array)): # O(n^2)
# 	sumi = array[index]

# 	if index + 1 < len(array):
# 		for j in range(index + 1, len(array)):
# 			if sumi > maximum['maxi']:
# 				maximum['maxi'] = sumi
# 				maximum['start'] = index
# 				maximum['end'] = j
# 			sumi = sumi + array[j]
# 	else:
# 		if sumi > maximum['maxi']:
# 			maximum['maxi'] = sumi
# 			maximum['start'] = index
# 			maximum['end'] = j

# print(maximum)

# Kadane's Algorithm

def kadana_algorithm(array):
	current_sum = 0
	maximum = array[0]
	for value in array:
		current_sum += value

		maximum = max(current_sum, maximum)
		if current_sum < 0:
			current_sum = 0
			continue
	print(maximum)

kadana_algorithm(array)

