def rows(letter):
	alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	letter_index = alphabets.find(letter)

	diamond_size = letter_index*2+1
	center = diamond_size//2
	result_list = []

	for row in range(diamond_size):
		# Every time the loop runs, space_list is reassigned new spaces
		space_list = diamond_size*[' ']

		# The d variable holds the minimum number equivalent to the right letter for each row and builds up the diamond shape prototype
		d = min(row, diamond_size-1-row)

		# The variables hold position to which the letters go to
		left_index = center - d
		right_index = center + d

		# The letters are placed at the right positon building up the diamond
		space_list[left_index] = alphabets[d]
		space_list[right_index] = alphabets[d]

		alphabet_positions = ''.join(space_list)
		result_list.append(alphabet_positions)
	return result_list
