
class Tile:
		
	def __init__(self,terrain_type, highest,lowest = None ):
		"""
		Initialises the terrain tile and attributes
		"""
		self.terrain_type = terrain_type
		self.highest =highest
		if lowest != None:
			self.lowest = lowest
		elif lowest is None:
			self.lowest = None
		self.occupant = None #indicates whether there are occupants on the tile
		self.is_explored = False #indicates whether the tile is explored
	
	def elevation(self):
		"""
		Returns an integer value of the elevation number 
		of the terrain object
		"""
		return self.highest , self.lowest
		
	
	def is_shaded(self):
		"""
		Returns True if the terrain tile is shaded, otherwise False
		"""
		if self.terrain_type == 'shaded':
			return True
		else:
			return False
	
	def set_occupant(self, rover):
		"""
		1.Sets the occupant [rover] on the terrain tile, 2.changes the elevation of the rover according to the tile, 3.and marks the tile as being explored.
		"""
		self.occupant = rover #1
		rover.higher = self.highest #2
		rover.lower = self.lowest #2
		self.is_explored = True #3
	
	def get_occupant(self):
		"""
		Gets the entity on the terrain tile
		If nothing is on this tile, it should return None
		"""
		if self.occupant == None:
			return None
		else:
			return self.occupant
		
	def del_occupant(self): 
		"""deletes the occupant on the terrian, in case the rover moves pass the tile"""
		self.occupant = None
	
	
