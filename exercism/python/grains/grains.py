def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        number_of_grain_on_chesboard = 2 ** (number - 1)
    return number_of_grain_on_chesboard

def total():
	total_returned = 0
	for num in range(1, 65):
		total_returned += square(num)
	return total_returned
