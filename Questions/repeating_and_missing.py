array = [4, 3, 6, 2, 1, 1] # len = 6 numbers from 1-6
# Missing = 5 and Repeating = 1

def missing_and_repeating(array):

	index_array = [0] * len(array)
	
	for value in array:
		index_array[value-1] += 1

	print(index_array)
	repeating = 0
	for index, value in enumerate(index_array):
		if value > repeating:
			repeating = index + 1
		if value == 0:
			missing = index + 1

	print(f'Repeating: {repeating}, Missing: {missing}')

missing_and_repeating(array)
missing_and_repeating([3, 1, 3])