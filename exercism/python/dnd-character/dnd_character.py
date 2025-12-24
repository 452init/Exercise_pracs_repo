import random
class Character:
	def __init__(self):
		self.strength = self.roll_dice()
		self.dexterity = self.roll_dice()
		self.constitution = self.roll_dice()
		self.intelligence = self.roll_dice()
		self.wisdom = self.roll_dice()
		self.charisma = self.roll_dice()

		self.modifier = modifier(self.constitution)
		self.hitpoints =  self.modifier + 10


	def roll_dice(self):
		roll = [random.randint(1, 6) for _ in range(4)]
		roll.remove(min(roll))
		return sum(roll)

	def ability(self):
		return self.roll_dice()

def modifier(value):
	return (value-10)//2
