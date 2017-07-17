class Item(object):
	def __init__(self, name, vague, description):
		self.name = name
		self.vague = vague
		self.description =description
class Key(Item):
		def __init__(self, name, vague, description, id):
			super(Key, self).__init__(name, vague, description)
			self.type = 'key'
			self.id =id
			self.movable = True



class Weapon(Item):
	def __init__(self, name, vague, description, category, attack, noise):
		super(Weapon, self).__init__(name, vague, description)
		self.type = 'weapon'
		self.category = category
		self.attack = attack
		self.noise = noise
		self.movable = True

class Food(Item):
	def __init__(self, name, vague, description, heal =5):
		super(Food, self).__init__(name, vague, description)
		self.type = 'food'
		self.movable = True
		self.heal = heal


		










