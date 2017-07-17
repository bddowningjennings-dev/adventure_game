from item import Food, Weapon
import random
class Npc(object):
	def __init__(self,  health, attack):
		self.health = health
		self.attack = attack
		self.attackable = False
		self.inventory= []
	def __str__(self):
   		return self.description
   	def deathAction(self,world, y,x):
   		for item in self.inventory:
   			world[y][x].addItem(item)
   			print """ The {} dropped 1 {}.""".format(self.name if hasattr(self, 'name') else self.type, item.name)
	def genInventory(self, possibleItems, gen=3):
		count = 0
		while count <= gen:
			if random.randint(0,100) > 50:
				self.inventory.append(possibleItems[random.randint(0,len(possibleItems)-1)])
			count +=1




class Rat(Npc):
    def __init__(self,  health=10, attack=10):
        super(Rat, self).__init__(health, attack)
        self.type = 'rat'
        self.vague = 'A rat is in this space. He looks unclean.'
        self.description = 'On closer look, this rat looks like he has rabies.'
        self.attackable = True
        possibleItems =[
        	Food('cheese', 'The aroma emitting from the chuck of swiss cheese excites you.', 'This cheese looks semi edible', 6),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
        	]
        self.genInventory(possibleItems)

class Goblin(Npc):
    def __init__(self,  health=25, attack=15):
        super(Goblin, self).__init__(health, attack)
        self.type = 'goblin'
        self.vague = 'A mean looking goblin is hiding under some rubbish. '
        self.description = "I wouldn't start a fight with this goblin."
        self.attackable = True
        possibleItems =[
        	Food('morsel', "There's a small piece of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 7),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
			Weapon(' rusty dagger','A small dagger that is horrblely crafted and rusted.','This dagger has seen better days.','dagger', 7,  'slash!')
        	]
        self.genInventory(possibleItems)

class Troll(Npc):
    def __init__(self,  health=40, attack=10):
        super(Troll, self).__init__(health, attack)
        self.type = 'troll'
        self.vague = 'There is a troll in here.He looks unkept.'
        self.description = "I wouldn't start a fight with this Troll."
        self.attackable = True
        possibleItems =[
        	Food(' big morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 15),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
			Weapon(' Common sword',"You've seen this sword before. It's sold everywhere. What's it doing just sitting here?",'This sword is well kept.','sword', 14,  'slash!')
        	]
        self.genInventory(possibleItems)
 


 



