def mirror_func(mirror_version):
	list_char = []

	for char in mirror_version.lower():
		if 'a' <= char <= 'z':
			mirror = ord('z') - ord(char) + ord('a')
			list_char.append(chr(mirror))
		elif char.isdigit():
			list_char.append(char)
	char_string = ''.join(list_char)
	return char_string

def encode(plain_text):
	result_cipher = mirror_func(plain_text)
	return ' '.join(result_cipher[i:i+5] for i in range(0, len(result_cipher), 5))


def decode(ciphered_text):
	result_string = mirror_func(ciphered_text)
	return result_string
