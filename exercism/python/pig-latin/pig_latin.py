def translate(text):
	result_list = []
	for word in text.split():
		vowels = 'aeiou'
		return_str = ''
		if word[0] in vowels or word.startswith(('xr', 'yt')):
			i = 0
		elif word.startswith('qu'):
			return_str = 'qu'
			i = 2
		else:
			if word.find('y')>0:
				vowels += 'y'
			for i, c in enumerate(word):
				if c in vowels: break
				return_str += c
				if word[i:].startswith('qu'):
					return_str += 'u'
					i += 2
					break
		result_list.append(word[i:] + return_str + 'ay')
	return ' '.join(result_list)
