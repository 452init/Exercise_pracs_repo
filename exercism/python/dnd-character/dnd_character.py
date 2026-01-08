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
		result = [random.randint(1, 5) for _ in range(3)]
		return sum(result)

def modifier(value):
	return (value-10)//2
