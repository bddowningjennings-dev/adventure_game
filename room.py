class Room(object):
	def __init__(self, description):
		self.description = description
		self.items = []
		self.npcs = []
		self.doors = {
		'north': { 'locked': False, 'key_id': False},
		'east': {'locked': False, 'key_id': False},
		'south': { 'locked': False, 'key_id': False},
		'west': {'locked': False, 'key_id': False},
		 }
	def addItem(self, item):
		self.items.append(item)
		return self

	def addNpc(self, *args):
		for npc in args:
			self.npcs.append(npc)
	def describe(self):
		print "\033[36m"
		print self.description
		for item in self.items:
			print item.vague
		for npc in self.npcs:
			print npc.vague
		print "\033[37m"
	def unlocker(self,player, world, capture):
		for door, direction in self.doors.items():
			for item in player.inventory:
				if item.type == 'key' and direction['key_id'] == item.id:
					direction['locked'] = False
					print "\n\033[33m The door to the {} is unlocked.\n\033[37m".format(door)
					return
		print "\n\033[33m I dont see a door that can be unlocked with the keys you have.\n\033[37m"
				


	def doorCheck(self, direction):
		if self.doors[direction]['locked']== True:
			print "\n\033[33mThis door is locked! You better find the correct key.\n\033[37m"
			return False
			print """

You moved {}.
			""".format(direction)
		return True

	

