def sum_of_multiples(limit, multiples):
    set_of_multiples = set()
    sum_of_unique_multiples = 0
    for num in multiples:
        for i in range(limit):
            set_of_multiples.add(num*i)
    for unique in set_of_multiples:
        if unique < limit:
            sum_of_unique_multiples += unique
    return sum_of_unique_multiples
