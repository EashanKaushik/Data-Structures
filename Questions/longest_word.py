
# without regular expression
def longest_word(sen):

	chars = list(sen)

	values = {'maximum':0}
	count = 0
	left = 0
	indices = set()

	while(left < len(chars)):

		if (ord(chars[left]) >= 65 and ord(chars[left]) <= 90) or (ord(chars[left]) >= 97 and ord(chars[left]) <= 122):
			print(chars[left])
			count += 1
			indices.add(left)
		else:
			print('|||')
			count = 0
			indices = set()

		if count > values['maximum']:
			values['maximum'] = count
			values['indices'] = indices
		left += 1

	return values


print(longest_word('India123 and lowerww'))



