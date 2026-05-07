def square_root(number):
	epsilon = .0000001
	est_sqr = number/2

	while True:
	    comparison_num = (est_sqr+number/est_sqr)/2
	    if abs(comparison_num-est_sqr)<epsilon:
		    break
	    est_sqr=comparison_num

	return int(est_sqr)
