from item import Food, Weapon
import random
class Npc(object):
	def __init__(self,  health=None, attack=None):
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

class Merchant(Npc):
    def __init__(self, vague = None, description = None):
        super(Merchant, self).__init__()
        self.type = 'merchant'
        self.vague = 'A merchant looks ready to sell you something.'
        self.description = 'This merchant looks as if he knows a thing or two.'
    def addItem(self,  item):
        if item.type == 'weapon':
            if item.attack <= 20:
                cost = 20
            elif item.attack > 20 and item.attack < 40:
                cost = 40
            elif item.attack > 40 and item.attack < 80:
                cost = 60
            elif item.attack > 80 and item.attack < 120:
                cost = 80

        if item.type == 'food':
            if item.heal <= 20:
                cost = 20
            elif item.heal > 20 and item.heal < 40:
                cost = 40
            elif item.heal > 40 and item.heal < 80:
                cost = 60
            elif item.heal > 80 and item.heal < 120:
                cost = 80
        if item.type == 'armor':
            if item.health <= 20:
                cost = 20
            elif item.health > 20 and item.health < 40:
                cost = 40
            elif item.health > 40 and item.health < 80:
                cost = 60
            elif item.health > 80 and item.health < 120:
                cost = 80
        addItem = {'item': item, 'cost': cost}
        self.inventory.append(addItem)
    def listItems(self):
        print "\033[36m Heres what I got: \033[37m"
        for item in self.inventory:
             print "\033[36m I have a {} that will cost you {}.\033[37m".format(item['item'].name, item['cost'] )
             
    
    


class Rat(Npc):
    def __init__(self,  health=10, attack=15):
        super(Rat, self).__init__(health, attack)
        self.exp = 20
        self.gold = 5
        self.type = 'rat'
        self.vague = 'A rat is in this space. He looks unclean.'
        self.description = 'On closer look, this rat looks like he has rabies.'
        self.attackable = True
        possibleItems =[
        	Food('cheese', 'The aroma emitting from the chuck of swiss cheese excites you.', 'This cheese looks semi edible', 6

        		),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
        	]
        self.genInventory(possibleItems)

class Goblin(Npc):
    def __init__(self,  health=25, attack=15):
        super(Goblin, self).__init__(health, attack)
        self.exp = 200
        self.gold = 10
        self.type = 'goblin'
        self.vague = 'A mean looking goblin is hiding under some rubbish. '
        self.description = "I wouldn't start a fight with this goblin."
        self.attackable = True
        possibleItems =[
        	Food('morsel', "There's a small piece of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 7),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
			Weapon(' rusty dagger','A small dagger that is horribly crafted and rusted.','This dagger has seen better days.','dagger', 7,  'slash!')
        	]
        self.genInventory(possibleItems)

class Troll(Npc):
    def __init__(self,  health=40, attack=10):
        super(Troll, self).__init__(health, attack)
        self.exp = 300
        self.gold = 12
        self.type = 'troll'
        self.vague = 'There is a troll in here.He looks unkept.'
        self.description = "I wouldn't start a fight with this Troll."
        self.attackable = True
        possibleItems =[
        	Food(' big morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 15),
        	Food('garbage', 'A disgusting pile of garbage sits on the floor.', "The smell is horrible. I wouldn't eat it", -10),
			Weapon('common sword',"You've seen this sword before. It's sold everywhere. What's it doing just sitting here?",'This sword is well kept.','sword', 14,  'slash!')
        	]
        self.genInventory(possibleItems)


class KingRat(Npc):
    def __init__(self,  health=70, attack=15):
        super(KingRat, self).__init__(health, attack)
        self.exp = 1100
        self.gold = 12
        self.type = 'king rat'
        self.vague = 'There is a rat wearing a crown. He must be part of a royal family'
        self.description = "I wouldn't start a fight with this rat."
        self.attackable = True
        possibleItems =[
            Food(' large morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 40),
            Food(' big morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 15),
            Weapon(' king sword',"Legends have been told of this sword",'This sword is wvery nice. You should pawn it.','sword', 30,  'slash!')
            ]
        self.genInventory(possibleItems)
class BabyDragon(Npc):
    def __init__(self,  health=30, attack=20):
        super(BabyDragon, self).__init__(health, attack)
        self.exp = 1800
        self.gold = 30
        self.type = 'baby dragon'
        self.vague = 'There is a baby dragon breathing fire on the ground here. '
        self.description = "This dragon will grow to be a fine dragon. You better kill it now."
        self.attackable = True
        possibleItems =[
            Food(' large morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 40),
            Food(' big morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 15)
            ]
        self.genInventory(possibleItems)
class Dragon(Npc):
    def __init__(self,  health=60, attack=30):
        super(Dragon, self).__init__(health, attack)
        self.exp = 4000
        self.gold = 400
        self.type = 'dragon'
        self.vague = 'There is dragon breathing fire on the ground here. '
        self.description = " You better kill this dragon now.. before he has babies."
        self.attackable = True
        possibleItems =[
            Food(' large morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 40),
            Food(' big morsel', "There's a large chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 15),
            Weapon('dragon sword',"This sword has a red aura.",'This sword is wvery nice.','sword', 45, 'slash!')
            ]
        self.genInventory(possibleItems)
class Giant(Npc):
    def __init__(self,  health=80, attack=29):
        super(Giant, self).__init__(health, attack)
        self.exp = 2500
        self.gold = 200
        self.type = 'giant'
        self.vague = 'This giant is taller then everything.'
        self.description = " I wish I was a little bit taller..."
        self.attackable = True
        possibleItems =[
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            ]
        self.genInventory(possibleItems)


class Kraken(Npc):   
     def __init__(self,  health=100, attack=45):
        super(Kraken, self).__init__(health, attack)
        self.exp = 7000
        self.gold = 1000
        self.type = 'kraken'
        self.vague = 'Wow, no legendary sea monster was as horrifying as this kraken.'
        self.description = "Awaken."
        self.attackable = True
        possibleItems =[
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            ]

        self.inventory.append(Weapon('god sword',"This sword belonged to a god.",'This sword is very nice. You should pawn it.','sword', 74,  'slash!'))
        self.genInventory(possibleItems)



class Cthulhu(Npc):   
     def __init__(self,  health=160, attack=65):
        super(Cthulhu, self).__init__(health, attack)
        self.exp = 15000
        self.gold = 1000
        self.type = 'cthulhu'
        self.vague = 'That cthulhu is what nightmares are made of.'
        self.description = "shit."
        self.attackable = True
        possibleItems =[
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            Food(' huge morsel', "There's a huge chunk of uncooked meat on the ground.", 'You would cook this piece of meat if you knew how.', 55),
            ]
        self.genInventory(possibleItems)




 


 



