def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')

    count = 0
    num_to_check = 2
    last_prime = 0

    while count < number:
        is_prime = True
        for num in range(2, int(num_to_check**.5)+1):
            if num_to_check % num == 0:
                is_prime = False
                break
        if is_prime:
            last_prime = num_to_check
            count += 1
        if count == number:
            return last_prime
        num_to_check += 1
