"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_contiguous_subsequence(longer_list, sub_list):
	
	long_len = len(longer_list)
	sub_len = len(sub_list)

	for i in range(long_len - sub_len +1):
		current_window = longer_list[i:i+sub_len]
		
		if current_window == sub_list:
			return True
	return False


def sublist(list_one, list_two):
	len1 = len(list_one)
	len2 = len(list_two)

	if list_one == list_two:
		return EQUAL
	elif list_one and not list_two:
		return SUPERLIST
	elif not list_one and list_two:
		return SUBLIST
	elif len1 > len2:
		if is_contiguous_subsequence(list_one, list_two):
			return SUPERLIST
	elif is_contiguous_subsequence(list_two, list_one):
		return SUBLIST
	return UNEQUAL
