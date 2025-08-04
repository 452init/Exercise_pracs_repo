def flatten(iterable):
	flattened_list = []
	for i in iterable:
		if isinstance(i, list):
			flattened_list.extend(flatten(i))
		elif i == None:
			continue
		else:
			flattened_list.append(i)
	return flattened_list
