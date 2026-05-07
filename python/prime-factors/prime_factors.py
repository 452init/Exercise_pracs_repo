import math
def find_all_factors(n):
	factors = []
	while n % 2 == 0:
		factors.append(2)
		n = n//2
	for num in range(3, int(n**.5)+1, 2):
		while n % num == 0:
			factors.append(num)
			n = n//num
	return n, factors
def factors(value):
	prime_factors_list = []

	remaining, prime_factors_list = find_all_factors(value)
	
	if remaining > 1:
		prime_factors_list.append(remaining)
	return prime_factors_list
