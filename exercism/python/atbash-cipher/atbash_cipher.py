def atbash_transform(mirror_version):
	list_char = []

	for char in mirror_version.lower():
		if 'a' <= char <= 'z':
			list_char.append(chr(ord('z') - ord(char) + ord('a')))
		elif char.isdigit():
			list_char.append(char)
		else:
			continue
	return ''.join(list_char)

def encode(plain_text):
	result_cipher = atbash_transform(plain_text)
	return ' '.join(result_cipher[i:i+5] for i in range(0, len(result_cipher), 5))


def decode(ciphered_text):
	result_string = atbash_transform(ciphered_text)
	return result_string
