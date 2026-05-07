def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    num = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for n in range(1, number):
        if number % n == 0:
            num += n
    if num == number:
        return "perfect"
    elif num > number:
        return "abundant"
    else:
        return "deficient"
