def say(number):
	num_dict = {
			0: 'zero',
			1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
			7: 'seven', 8: 'eight', 9: 'nine',
			10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
			15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
			30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
			}
	t = 1000
	m = t*1000
	b = m*1000

	if number < 0 or number > 999_999_999_999:
		raise ValueError('input out of range')
	if number < 20:
		return num_dict[number]
	if number < 100:
		if number%10 == 0: return num_dict[number]
		else: return num_dict[number//10 * 10] + '-' + num_dict[number%10]
	if number < t:
		if number%100 == 0: return num_dict[number//100] + ' hundred'
		else: return num_dict[number//100] + ' hundred ' + say(number%100)
	if number < m:
		if number%t == 0: return say(number//t) + ' thousand'
		else: return say(number//t) + ' thousand ' + say(number%t)
	if number < b:
		if number%m == 0: return say(number//m) + ' million'
		else: return say(number//m) + ' million ' + say(number%m)
	if number%b == 0:
		return say(number//b) + ' billion'
	else: return say(number//b) + ' billion ' + say(number%b)
