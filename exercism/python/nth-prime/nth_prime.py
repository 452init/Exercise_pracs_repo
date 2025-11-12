def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('Cannot be a prime number!')

    count = 0
    num_to_check = 2
    last_prime = 0
    
    while count < number:
        if num_to_check == 2:
            is_prime = True
            count += 1
            last_prime = 2
            num_to_check = 3
            continue

        if is_prime_number(num_to_check):
            last_prime = num_to_check
            count += 1
        num_to_check += 2
    return last_prime

def is_prime_number(n):
    is_prime = True
    for num in range(2, int(n**.5)+1):
        if n % num == 0:
            return not is_prime
    return is_prime
