# 'Hi my name is eashan' -- Reverse

# def reverse_string(value):
# 	value = list(value)
# 	temp = list()

# 	if type(value) is not str:
# 		# print('Enter String')
# 		return 'Enter String'
# 	for index in range(len(value), 0, -1):
# 		temp.append(value[index-1])


# 	return str(temp)

# print(reverse_string(['Hi my name is Eashan']))

def reverse_string(value):

	if type(value) is not str:
		# print('Enter String')
		return 'Enter String'

	value = list(value)
	value.reverse()
	return str(value)

print(reverse_string('Hi my name is Eashan'))