def commands(binary_str):
	secret_handshake = []
	secret_words = ['wink','double blink','close your eyes','jump']
	
	for i, c in zip(reversed(binary_str), secret_words):
		if i == '1':
			secret_handshake.append(c)
	if binary_str[0] == '1':
		reversed_secret_handshake = list(reversed(secret_handshake))
		return reversed_secret_handshake
	return secret_handshake
