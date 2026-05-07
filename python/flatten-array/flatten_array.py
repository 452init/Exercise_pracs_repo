def flatten(iterable):
	flattened_list = []
	for elem in iterable:
		if isinstance(elem, list):
			flattened_list.extend(flatten(elem))
		elif elem is not None:
			flattened_list.append(elem)
	return flattened_list
