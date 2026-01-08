import random
class Character:
	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()

		self.constitution_modifier = modifier(self.constitution)
		self.hitpoints =  self.constitution_modifier + 10

	def ability(self):
		result = [random.randint(1, 6) for _ in range(4)]
		result = sorted(result)[1:]
		return sum(result)

def modifier(value):
	return (value-10)//2
