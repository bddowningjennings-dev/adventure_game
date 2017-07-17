class Room(object):
	def __init__(self, description):
		self.description = description
		self.items = []
		self.npcs = []
		self.doors = {'north': {'status': False,  'locked': False, 'key_id': False},
		 'east': {'status': False,  'locked': False, 'key_id': False},
		 'south': {'status': False,  'locked': False, 'key_id': False},
		 'west': {'status': False,  'locked': False, 'key_id': False},
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

