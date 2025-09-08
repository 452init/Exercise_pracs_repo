def atbash_transform(text):
	list_char = []

	for char in text.lower():
		if 'a' <= char <= 'z':
			list_char.append(chr(ord('z') - ord(char) + ord('a')))
		elif char.isdigit():
			list_char.append(char)
	return ''.join(list_char)

def encode(plain_text):
	result_cipher = atbash_transform(plain_text)
	return ' '.join(result_cipher[i:i+5] for i in range(0, len(result_cipher), 5))


def decode(ciphered_text):
	result_string = atbash_transform(ciphered_text)
	return result_string



"""Method Function used to preserve special characters and upper case letters in Atbash Cipher"""
def atbash_transform_with_structure(text):
	"""Transform only letters, keeping spaces and punctuation in place."""
	result = []

	for char in text:
		char_lower = char.lower()
		is_upper = char.isupper()
		if 'a' <= char.lower() <= 'z':
			transformed = chr(ord('a') - ord(char_lower) + ord('z'))
			#Preserves the uppercase letters incase they append in the text
			result.append(transformed.upper() if char_isupper else transformed)
		# Appends special characters to the result
		else:
			result.append(char)
	return ''.join(result)

def vigenere_cipher(letters):
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	position_list = []
	char_position = {x: pos for pos, x in enumerate(alphabets)}
	lower_case_one = text.lower()
	lower_case = lower_case_one.replace(' ', '')

	for index, char in enumerate(lower_case):
		'''checks if the char is first or last and does not modify it and ignores non alphabets'''
		if char.isalpha() and (index == 0 or index == len(lower_case) -1):
			position_list.append(char)
		else:
			'''ignores non alphabets and modifies all the letters between the first and last index'''
			if char.isalpha():
				result_char = char_position.get(char)
				new_index = (result_char+index) % len(alphabets)
				position_list.append(alphabets[new_index])
	return ''.join(position_list)
