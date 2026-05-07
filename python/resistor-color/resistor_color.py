def color_code(color):
	color_name = {
		'black': 0,
		'brown': 1,
		'red': 2,
		'orange': 3,
		'yellow': 4,
		'green': 5,
		'blue': 6,
		'violet': 7,
		'grey': 8,
		'white': 9,
	}
	return color_name.get(color, color_name)

def colors():
	color_band = color_code(None)
	return list(color_band.keys())
