class SpaceAge:
	EARTH_YEAR_IN_SECONDS = 31_557_600
	MERCURY = 0.2408467
	VENUS = 0.61519726
	EARTH = 1.0
	SATURN = 29.447498
	MARS = 1.8808158
	JUPITER= 11.862615
	URANUS = 84.016846
	NEPTUNE = 164.79132
	def __init__(self, seconds):
		self.seconds = seconds
		self.age_on_earth = seconds / self.EARTH_YEAR_IN_SECONDS
	def on_mercury(self):
		return (round(self.age_on_earth/self.MERCURY, 2))
	def on_venus(self):
		return (round(self.age_on_earth/self.VENUS, 2))
	def on_earth(self):
		return (round(self.age_on_earth/self.EARTH, 2))
	def on_mars(self):
		return (round(self.age_on_earth/self.MARS, 2))
	def on_jupiter(self):
		return (round(self.age_on_earth/self.JUPITER, 2))
	def on_saturn(self):
		return (round(self.age_on_earth/self.SATURN, 2))
	def on_uranus(self):
		return (round(self.age_on_earth/self.URANUS, 2))
	def on_neptune(self):
		return (round(self.age_on_earth/self.NEPTUNE, 2))
