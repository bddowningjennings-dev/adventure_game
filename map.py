from room import Room
from item import Item, Weapon, Key, Food, Armor
from npc import Npc, Rat, Goblin, Troll, KingRat, Merchant, BabyDragon, Dragon, Giant, Kraken, Cthulhu


#room one setup
r1 = Room('This room is dimly lit. There is a door with a lock on it to the north.')
r1.addItem(Weapon('rusty sword', 'Something rusty lies on the ground. It looks like a sword.', 'this sword has been crafted by the gods', 'sword', 5, 'slash'))
r1.addItem(Food('apple', 'A juicy look apple sits here.', 'This apple is to perfect to eat.'))
r1.doors['north']['locked'] = True
r1.doors['north']['key_id'] = '1n'
r1.addNpc(Rat(), Rat())
r =Rat()




#room two setup
r2 = Room('This room has a window in the corner.')
r2.addItem( Weapon('rock','A small rock. nothing great.','This rock is quite nice when you look at it. ','rock', 1,  'boop'))
r2.addNpc(Goblin())



#room three setup
r3= Room('This is a heavily forested area.')


#room four setup
r4= Room('This is a road. its leading west and east.')
r2.addNpc(Goblin(), Troll() )

#room five setup
r5= Room("This is the end of the road. There is an ocean that seems to have strong currents. No, you can't swim. There seems to be a room to your south")
r5.addItem( Weapon('rock','A small rock. nothing great.','This rock is quite nice when you look at it. ','rock', 1,  'boop'))
r5.addItem( Weapon('rock','A small rock. nothing great.', 'This rock is quite nice when you look at it. ','rock', 1,  'boop'))
r5Merchant = Merchant()
r5Merchant.addItem(Armor('common armor', 'A pile of armor lies here. Looks shiny.', 'This armor is decent.', 30))
r5Merchant.addItem(Weapon('Rusty broadsword','Two handed broadsword.','What a rusty boardsword.  ','sword', 11,  'slash'))
r5Merchant.addItem(Food('pizza','Is that pizza on the ground?','Papa Johns pizza. With Pepporoni. My god.', 21))
r5.addNpc(r5Merchant)

#room six setup
r6= Room("You are at a main enterance of a building called the Champions hallway.")




#room seven setup
r7= Room("You are inside a small hallway. There is a large room to the south. ")
r7.addNpc(Rat(), Rat(),Rat(), Rat())



#room eight
r8 = Room('To your south, you see a small cave. East of you seems to be a path. ')
r8.addNpc(KingRat())
r8.addItem(Armor('rusty armor', 'A pile of rusty armor lies here.', 'This armor has seen better days.', 20))

r9 = Room('Seems to be a large room.')
r9.addNpc(Rat(), Rat(),Rat(), Rat())
r9.npcs[0].inventory.append(Key('key','A key lies here.', 'This key probably opens a door nearby.', '1n'))


r10 = Room('You are in a cave.Its wet in here. There seems to be a room to the south.')
r10.addNpc(Goblin(), Troll(), Rat(), Rat(),Rat(), Rat())



r11 = Room('You are in a cave. Its wet in here.')
r11.addNpc(Dragon())



r12 = Room('This room is full of your greatest fears.')
r12.addNpc(Dragon(), Giant(), KingRat())


r13 = Room('You are in a cave. Its wet in here. There seems to be a large room to the south.')
r13.addNpc(Goblin(), Giant(), Rat(), Rat(),Rat(), Rat())

r14 = Room("You are in the champion's room. There is a locked door to your south.")
r14.addNpc(Dragon(),Dragon(),Dragon(),Kraken())
r14.doors['south']['locked'] = True
r14.doors['south']['key_id'] = '14s'
r14.npcs[2].inventory.append(Key('key','A key lies here.', 'This key probably opens a door nearby.', '14s'))

r15 = Room("You are in the final room. This room will test your stength.")
r15.addNpc(Kraken(),Kraken(), Cthulhu() )





world = [
	[r8,r3,r2,r4,r5],
	[r10 ,0 ,r1 ,0 ,r6 ],
	[r13 ,0 ,r9 ,0 ,r7 ],
	[r11,0 ,0 ,0 , r12 ],
	[0, 0 ,0 ,0 , r14 ],
	[0, 0 ,0 ,0 , r15 ]
]