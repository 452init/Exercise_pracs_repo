def is_paired(input_string):
	stack = []
	mapped_braces = {'(': ')', '[': ']', '{': '}'}
	mismatched_braces = ''

	for char in input_string:
		if char in mapped_braces.keys():
			stack.append(char)
		elif char not in mapped_braces.keys() and char not in mapped_braces.values() and char == '\\':
			continue
		elif char in mapped_braces.values():
			if len(stack) == 0:
				mismatched_braces += char
				return not mismatched_braces
			#Raises KeyError incase any object that is not an openning bracket is added to the stack
			if mapped_braces[stack[-1]] == char:
				stack.pop()
			else:
				return False
	return len(stack) == 0


#How would you handle this problem if you also needed to track the positions of mismatched brackets for error reporting?
#What if you needed to support custom bracket pairs that could be defined at runtime?
#How would you modify your approach if brackets could be escaped (like \[ shouldn't count)?
