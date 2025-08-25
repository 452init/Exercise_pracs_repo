def is_paired(input_string):
	stack = []
	openning_braces = '{[('
	closing_braces = '])}'
	mapping_braces = {'(': ')', '{': '}', '[': ']'}

	for char in input_string:
		if char in openning_braces:
			stack.append(char)
		elif char in closing_braces:
			if len(stack) == 0:
				return False
			if mapping_braces[stack[-1]] == char:
				stack.pop()
			else:
				return False
	return len(stack) == 0
