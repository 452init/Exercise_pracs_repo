import itertools
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('Cannot be a prime number!')

    for n in itertools.islice(prime_generator(), number):
        nth_prime = n
    return nth_prime

def prime_generator():
    candidate = 2

    while True:
        is_prime = True
        for num in range(2, int(candidate**.5)+1):
            if candidate % num == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 1
