def sum_of_multiples(limit, multiples):
	set_of_multiples = set()
	for num in multiples:
		if num == 0:
			continue
		for unique in range(num, limit, num):
			set_of_multiples.add(unique)
	return sum(set_of_multiples)
