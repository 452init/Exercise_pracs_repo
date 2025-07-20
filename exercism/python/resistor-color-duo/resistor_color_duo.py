def value(colors):
	color_num = ''
	color_dict = {
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
		if i in color_dict and len(color_num) < 2:
			color_num += str(color_dict.get(i))
	return int(color_num)
