import re


def gameOver():
	print """
******************************************************
			Game Over :(

******************************************************

	"""

def attacker(player, world, capture):
	capture = ' '.join(capture)
	for npc in world[player.y][player.x].npcs:
		if re.search( capture, npc.type):
			if npc.attackable == True:
				npc.health -= player.attack
				print ''
				print '\033[35m You did {} damage to the {}!\033[37m'.format(player.attack, npc.type)
				if npc.health <= 0:
					print '\033[32m You killed the {}!\033[37m'.format(npc.type)
					npc.deathAction(world, player.y, player.x)
					world[player.y][player.x].npcs.remove(npc)
				else:
					player.health -= npc.attack
					print '\033[31m {} did {} damage to you!\033[37m'.format(npc.type, npc.attack)
					if player.health <= 0:
						print '\033[1m The {} has killed you.\033[37m'.format(npc.type)
						gameOver()
						quiter()

			return
		print """\033[31m
You can't attack what you can't see. Or can you????.
\033[37m
		"""



def equipper(player, world, capture):
	capture = ' '.join(capture)
	for item in player.inventory:
		if re.search( capture, item.name)  or  hasattr(item,'category') and re.search( capture, item.category):
			if item.type == 'weapon':
				player.hold = item
				player.inventory.remove(item)
				player.attack += item.attack
			 	print ''
				print '\033[32mYou are holding {}.\033[37m'.format(item.name)
				print ''
				return

	print "I don't see a {} in your inventory.".format(capture)


def remover(player,world, capture):
	capture = ' '.join(capture)
	if player.hold != None:
		if re.search( capture, player.hold.name) or re.search( capture, player.hold.type):
			player.inventory.append(player.hold)
			print """\033[32m You removed the {}. \033[37m

			""".format(player.hold.name)
			player.attack -= player.hold.attack
			player.hold = None

			return
	print """
\033[31m
You are not holding that.

\033[37m
		"""





def inventory(player, world, capture):
	items =  '\n' +'\n '.join('            {}                                               '.format(x.name) for x in player.inventory)
	
	print items
	print """

`````````````````````````````````````````````````````````````
  	name: {} |      health:{}     |     attack: {}                          
                                                            	
  	Holding: {}                                               
  	Carrying: {}                                              
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
````````````````````````````````````````````````````````````` 
	""".format(player.name, player.health, player.attack, player.hold.name if player.hold else 'Nothing', items)
def eatter(player, world, capture):
	capture = ' '.join(capture)
	for item in player.inventory:
		if re.search( capture, item.name) and item.type == 'food':
			sum = 0
			if item.heal >= 0:
				while sum < item.heal and player.health < player.max_health:
					player.health += 1
					sum += 1
			else:
				while sum > item.heal and player.health > 0:
					player.health -= 1
					sum -= 1
					if player.health == 0:
						print """ You have killed yourself. It's too late to change your eating habits."""
						gameOver()
						quit()

			
		 	player.inventory.remove(item)
		 	print """
		 	\033[32m
You ate the {}. you gained {} health.
			\033[37m
			 """.format(item.name, sum)
			return
	print "I don't see a {} here that you can eat. Are you dreaming of food again?".format(capture)



def helper():
	print """
	\033[93m
	Here are a list of commands:
	1) quit - Will quit the game.
	2) help - Will show a list of commands
	3) move - Will move in a direction. Should be followed by a 
	  cardinal direction (north, south, east, west)

	4) look - Looks around the current room
	5) dirs - Shows possible directions.
	6)inv  - gives you player stats and info on whats in your inventory
	7)get *item* - gets an item in the room.
	8) use  *item* - holds a weapon
	9)kill *enemy* - attacks enemy	


	\033[37m

	"""
def looker(player, world, capture):
	capture = ' '.join(capture)
	world[player.y][player.x].describe()

def quiter():
	print """
	\033[32m
	See you later.
	\033[37m
	"""
	exit()
def getPossDirections(player, world):
	dirs = []
	if player.y > 0 and world[player.y-1][player.x] != 0:
		dirs.append('north')
	if player.y < len(world)-1 and world[player.y+1][player.x] != 0 :
		dirs.append('south')
	if player.x > 0 and world[player.y][player.x-1] != 0 :
		dirs.append('west')

	if player.x < len(world[player.y])-1 and world[player.y][player.x+1] != 0 :
		dirs.append('east')
		print ''
	print "Possible directions you can move are:", ' '.join(dirs)
	print """
	"""


def getter(player, world, capture):
	capture = ' '.join(capture)
	results = False
	for item in world[player.y][player.x].items:
		if re.search( capture, item.name) or  hasattr(item,'category') and re.search( capture, item.category) :
			player.inventory.append(item)
		 	world[player.y][player.x].items.remove(item)
		 	print """
		 	\033[32m
You got a {}.
			\033[37m
			 """.format(item.name)
			return
	print "I don't see a {} here. I'm guessing you don't either.".format(capture)





def mover(player, world,capture):
	capture = capture[0]
	if capture != 'north' and capture != 'south' and capture != 'west' and capture != 'east':
		print """
\033[31m
That is not a direction.

\033[37m
		"""
	else:
		if capture == 'north' and  player.y > 0 and world[player.y-1][player.x] != 0:
			player.y -=1
			print """

You moved north.
			"""
			world[player.y][player.x].describe()
		elif capture == 'south' and player.y < len(world)-1 and world[player.y+1][player.x] != 0 :
			player.y +=1
			print """

You moved south.
			"""
			world[player.y][player.x].describe()

		elif capture == 'west' and player.x > 0 and world[player.y][player.x-1] != 0 :
			player.x -=1
			print """

You moved west.
			"""
			world[player.y][player.x].describe()

		elif capture == 'east' and player.x < len(world[player.y])-1 and world[player.y][player.x+1] != 0 :
			player.x +=1
			print """

You moved east.
			"""
			world[player.y][player.x].describe()
		else:
			print """
\033[31m
You can't do that.
\033[37m


			"""
	getPossDirections(player, world)

	
def command(input, player, world):
	capture = input.split()
	if not capture:
		return
	capture = [x.lower() for x in capture]
	if capture[0] == 'help':
		helper()
	if capture[0] == 'quit':
		quiter()
	if capture[0] == 'move':
		mover(player, world, capture[1::])
	if capture[0] == 'north' or capture[0] == 'south' or capture[0] == 'east' or capture[0] == 'west':
		mover(player, world, capture)
	if capture[0] == 'look':
		looker(player, world,capture[1::])
		getPossDirections(player, world)
	if capture[0] == 'dirs':
		getPossDirections(player, world)
	if capture[0] == 'get':
		getter(player, world, capture[1::])
	if capture[0] == 'equip' or capture[0] == 'use':
		equipper(player, world, capture[1::])
	if capture[0] == 'inv' or capture[0] == 'inventory':
		inventory(player, world, capture[1::])
	if capture[0] == 'rem' or capture[0] == 'remove':
		remover(player, world, capture[1::])
	if capture[0] == 'atk' or capture[0] == 'attack'  or capture[0] == 'hit'  or capture[0] == 'kill':
		attacker(player, world, capture[1::])
	if capture[0] == 'eat':
		eatter(player, world, capture[1::])





		
