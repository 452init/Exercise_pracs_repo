def rotate(text, key):
	new_position = ''
	for i in text:
		if i.isalpha():
			if i.islower():
				position = ord(i) - ord('a')
				shifted_position = (position + key) % 26
				new_position += chr(shifted_position + ord('a'))
			elif i.isupper():
				position = ord(i) - ord('A')
				shifted_position = (position + key) % 26
				new_position += chr(shifted_position + ord('A'))
		else:
			new_position += i
	return new_position
