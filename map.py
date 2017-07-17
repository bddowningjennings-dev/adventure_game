from room import Room
from item import Item, Weapon, Key, Food
from npc import Npc, Rat, Goblin, Troll

#room one setup
r1 = Room('This room is dimly lit.')
r1.addItem(Weapon('rusty sword', 'Something Shinny caught your eye. It looks like a sword.', 'this sword has been crafted by the gods', 'sword', 5, 'slash'))
r1.addItem(Food('apple', 'A juicy look apple sits here.', 'This apple is to perfect to eat.'))
r1.addNpc(Rat(), Rat())
r =Rat()
print r



#room two setup
r2 = Room('This room has a window in the corner.')
r2.addItem(Key('key','A key lies here.', 'This key probably opens a door nearby.', 1))
r2.addItem( Weapon('rock','A small rock. nothing great.','This rock is quite nice when you look at it. ','rock', 1,  'boop'))
r2.addNpc(Goblin())



#room three setup
r3= Room('There is a merchant in the corner. He looks shady.')


#room four setup
r4= Room('this is a road. its leading west.')
r2.addNpc(Goblin(), Troll() )

#room five setup
r5= Room("this is the end of the road. There is an ocean that seems to have strong currents. No, you can't swim. There seems to be a room to your south")
r5.addItem( Weapon('rock','A small rock. nothing great.','This rock is quite nice when you look at it. ','rock', 1,  'boop'))
r5.addItem( Weapon('rock','A small rock. nothing great.', 'This rock is quite nice when you look at it. ','rock', 1,  'boop'))

#room six setup
r6= Room("You are at a main enterance of a building.")




#room seven setup
r7= Room("You are inside a small hallway")







world = [
	[0,r3,r2,r4,r5],
	[0,0,r1,0,r6],
	[0,0,0,0,r7],
]