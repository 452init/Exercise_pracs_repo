def label(colors):
	color_ohms =''
	string_ohms_value =''
	ohms_correct_value = 0
	color_num =[]
	resistor_color_dict = {
		'black': 0,
		'brown': 1,
		'red': 2,
		'orange': 3,
		'yellow': 4,
		'green': 5,
		'blue': 6,
		'violet': 7,
		'grey': 8,
		'white': 9
	}

	for i in colors:
		if i in resistor_color_dict and len(color_num) < 3:
			color_num.append(resistor_color_dict.get(i))
	color_ohms += str(color_num[0])
	color_ohms += str(color_num[1])

	for n in range(color_num[2]):
		color_ohms += '0'
	ohms_num = int(color_ohms)
	if ohms_num >= 1000000000:
		ohms_correct_value = ohms_num//1000000000
		string_ohms_value = str(ohms_correct_value)
		string_ohms_value += ' gigaohms'
	elif ohms_num >= 1000000:
		ohms_correct_value = ohms_num//1000000
		string_ohms_value = str(ohms_correct_value)
		string_ohms_value += ' megaohms'
	elif ohms_num >= 1000:
		ohms_correct_value = ohms_num//1000
		string_ohms_value = str(ohms_correct_value)
		string_ohms_value += ' kiloohms'
	else:
		ohms_correct_value = ohms_num
		string_ohms_value = str(ohms_correct_value)
		string_ohms_value += ' ohms'
	return string_ohms_value
