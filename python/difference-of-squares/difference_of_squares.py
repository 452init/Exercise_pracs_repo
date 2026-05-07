def square_of_sum(number):
	squared_sum = 0
	for num in range(number + 1):
		squared_sum += num
	return squared_sum**2

def sum_of_squares(number):
	summed_squares = 0
	for num in range(number + 1):
		summed_squares += num**2
	return summed_squares

def difference_of_squares(number):
	squared_sum = 0
	summed_squares = 0
	for num in range(number + 1):
		squared_sum += num
		summed_squares += num**2
	return ((squared_sum**2) - summed_squares)
