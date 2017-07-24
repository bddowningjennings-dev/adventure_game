import math
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hold = None
		self.armor = None
		self.inventory =[]
		self.attack = 5
		self.max_health = 50
		self.health = 50
		self.y = 1
		self.x =2
		self.gold = 100
		self.armor = None
		self.level =1
		self.next_level = 300
		self.exp = 0

	def leveler(self):
		healthBonus = self.armor.health if self.armor != None  else 0
		attackBonus = self.hold.attack if self.hold != None  else 0
		while self.exp > self.next_level:
			self.level +=1
			print """\033[36m You are now level {}!\033[37m""".format(self.level)
			self.next_level =  int(self.next_level *2.5)
			self.attack = int(math.ceil((self.attack - attackBonus)  * 1.20) + attackBonus)
			self.health = int(math.ceil((self.health - healthBonus)  * 1.20) + healthBonus)
			self.max_health = int(math.ceil(self.max_health  * 1.20))




