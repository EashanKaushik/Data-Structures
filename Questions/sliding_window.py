

def sliding_window(array):
	if (k <= 1):
		return 0

	product = 1
	left = 0
	right = 0

	while(right < len(array)):

		product *= array[right]

		while(product >= k):
			product /= array[left]
			left += 1

		result += right - left + 1

		right += 1

	return result