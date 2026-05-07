def is_paired(input_string):
	stack = []
	mapped_braces = {'(': ')', '[': ']', '{': '}'}
	closing_braces = set(mapped_braces.values())

	for char in input_string:
		if char in mapped_braces:
			stack.append(char)
		elif char in closing_braces:
			if not stack or mapped_braces[stack[-1]] != char:
				return False
			stack.pop()
	return not stack
