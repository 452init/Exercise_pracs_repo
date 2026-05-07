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

	top_half = [build_row(row, total_rows, alphabets)
	     for row in range(total_rows//2+1)]
	
	symmetry = top_half + top_half[(total_rows//2)-1::-1]

	if len(top_half)>1:
		return symmetry
	return top_half
