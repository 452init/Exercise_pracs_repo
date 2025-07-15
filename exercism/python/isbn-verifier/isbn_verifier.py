def is_valid(isbn):
    list_isbn = []
    verified_isbn = 0

    for i, n in enumerate(isbn):
        if n.isdigit():
            list_isbn.append(int(n))
        elif n == "X":
            if i == len(isbn) - 1:
                list_isbn.append(10)
            else:
                 return False
        elif n != "-":
            return False

    if len(list_isbn) != 10:
        return False

    for i in range(10):
        verified_isbn += list_isbn[i] * (10 - i)

    return verified_isbn % 11 == 0
