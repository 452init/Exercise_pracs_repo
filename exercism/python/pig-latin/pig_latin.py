def translate(text):
	my_list = text.split()
	vowels = 'aeiou'
	final_list = []
	result = ''

	for word in my_list:
		return_string = ''
		new_list = list(word)
		first_two_letters = word[0:2]
		if first_two_letters == 'xr' or first_two_letters == 'yt':
			new_list.append('ay')
			return ''.join(new_list)
		if first_two_letters == 'qu':
			return_string += new_list.pop(0)
			return_string += new_list.pop(0)
		if 'y' in new_list and 'y' not in new_list[0]:
			vowels += 'y'
		if not any(l in vowels for l in new_list):
			new_list.append('ay')
		else:
			while new_list[0] not in vowels:
				next_two_letters = ''.join(new_list[0:2])
				if next_two_letters == 'qu':
					return_string += new_list.pop(0)
					return_string += new_list.pop(0)
				else:
					return_string += new_list.pop(0)
		final_list.append(''.join(new_list) + return_string + 'ay')
		result = ' '.join(final_list)
	return result
