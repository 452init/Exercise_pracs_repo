import string
def build_row(row_num, total_rows, alphabets):
	letter_position = min(row_num, total_rows-1-row_num)
	spaces = (total_rows//2)*' '
	letter = alphabets[letter_position]
	
	if letter == 'A':
		first_row = spaces + letter+ spaces
		return first_row
	else:
		outer_spaces = (total_rows//2 - letter_position) * ' '
		inner_spaces = (letter_position*2-1)* ' '

		return outer_spaces + letter + inner_spaces + letter + outer_spaces


def rows(letter):
	alphabets = string.ascii_uppercase

	if letter not in alphabets:
		raise TypeError('Not a valid input!')

	letter_index = alphabets.find(letter)
	total_rows = letter_index*2+1
	result_list = ([build_row(rows, total_rows, alphabets) for rows in range(total_rows)])

	return result_list
