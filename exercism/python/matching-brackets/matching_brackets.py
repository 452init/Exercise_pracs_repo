def is_paired(input_string):
	stack = []
	openning_braces = '{[('
	closing_braces = '])}'
	mapping_braces = {'(': ')', '{': '}', '[': ']'}
	
	if input_string == '':
		return True
	for i in input_string:
		if i in openning_braces:
			stack.append(i)
		elif i in closing_braces:
			if len(stack) == 0:
				return False
			if mapping_braces[stack[-1]] == i:
				stack.pop()
			elif mapping_braces[stack[-1]] != i:
				return False
	if len(stack) == 0:
		return True
	else:
		return False
