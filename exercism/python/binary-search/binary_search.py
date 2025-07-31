def find(search_list, value):
	sorted_array = sorted(search_list)
	x, y = 0, len(sorted_array) - 1
	
	while x <= y:
		mid_of_array = (x+y) // 2
		if sorted_array[mid_of_array] == value:
			return mid_of_array
		elif sorted_array[mid_of_array] < value:
			x = mid_of_array + 1
		else:
			y = mid_of_array - 1
	raise ValueError('value not in array')
