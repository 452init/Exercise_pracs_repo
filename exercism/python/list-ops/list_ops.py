def append(list1, list2):
	for elem in list2:
		list1.append(elem)
		for x in list1:
			if x == []:
				list1.remove(x)
	return list1


def concat(lists):
	new_list = []
	for elem in lists:
		new_list += elem
	return new_list


def filter(function, list):
	new_list = []
	for elem in list:
		if function(elem) == True:
			new_list.append(elem)
		else:
			continue
	return new_list


def length(list):
    return len(list)


def map(function, list):
	updated_list = []
	for elem in list:
		updated_list.append(function(elem))
	return updated_list


def foldl(function, list, initial):
	for elem in list:
		initial = function(initial, elem)
	return initial


def foldr(function, list, initial):
	for elem in reversed(list):
		initial = function(initial, elem)
	return initial


def reverse(list):
	reversed_lits = []
	reversed_list = [elem for elem in reversed(list)]
	return reversed_list
