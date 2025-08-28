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


def sublist(list_one, list_two):
	len1 = len(list_one)
	len2 = len(list_two)
	curr_win = []
	checker = 0

	if not list_one and list_one == list_two:
		return EQUAL
	elif list_one and not list_two:
		return SUPERLIST
	elif not list_one and list_two:
		return SUBLIST
	elif list_one and list_two:
		if len1 == len2:
			for num in range(len1):
				if list_one[num] == list_two[num]:
					checker +=1
			if checker == len1:
				return EQUAL
			return UNEQUAL
		elif len1 > len2:
			for i in range(len1 - len2 +1):
				curr_win = list_one[i:i+len2]

				if curr_win == list_two:
					return SUPERLIST
			return UNEQUAL
		else:
			for i in range(len2 - len1 +1):
				curr_win = list_two[i:i+len1]

				if curr_win == list_one:
					return SUBLIST
		return UNEQUAL
