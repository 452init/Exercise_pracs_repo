def build_row(row_num, total_row, alphabets):
	space_list = total_row*[' ']
	center = total_row//2
	letter_position = min(row_num, total_row-1-row_num)

	left_index = center - letter_position
	right_index = center + letter_position
	space_list[left_index] = alphabets[letter_position]
	space_list[right_index] = alphabets[letter_position]

	return ''.join(space_list)

import string
def rows(letter):
	alphabets = string.ascii_uppercase

	if letter not in alphabets:
		raise TypeError('Not a valid input!')

	letter_index = alphabets.find(letter)
	total_rows = letter_index*2+1
	result_list = ([build_row(rows, total_rows, alphabets) for rows in range(total_rows)])

	return result_list
