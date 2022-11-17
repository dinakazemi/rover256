
class Rover:
	
	def __init__(self,x,y ):
		"""
		Initialises the rover
		"""
		self.x = x
		self.y = y
		self.number_of_tiles = 1 #rover's number of explored tiles
		self.charge = 100 #rover's charge
		self.higher = 0 #rover's higher elevation
		self.lower = None #rover's lower elevation which might not exist
	
	def set_elevation (self,tile):
		"""updates the elevation of the rover every time it changes its position"""
		self.higher = tile.highest
		self.lower = tile.lowest
	
	def get_elevation(self):
		"""returns the elevation of the rover"""
		return self.higher,self.lower
	
	
	def move(self, direction, cycles,planet):
		"""
		Moves the rover on the planet
		1. checks the direction of the movement
		2. checks whether the rover has reached the horizontal/vertical end or horizontal/vertical start of the planet. If so, it will adjust the values of the rover's x and y
		3. checks if the rover has the charge to do the movement.
		4. checks the elevation of the rover is consistent with the elevation of the next tile in the movement.
		5. if the tile has not been explored before, it will add the tiles by one.
		Note: the function has to keep track of which tile the rover is on each time!
		"""
		counter = 0
		
		if direction == 'N': #1

			while counter < cycles:#3
				
				tile = planet.tiles[((self.y-1)%planet.height)*planet.width+self.x]
				if self.charge==0 and (tile.is_shaded()):
					break
				if tile.lowest == None: #4
					"""checks if the rover can do the movement elevation wise"""
					if self.lower == None:
						if self.higher!=tile.highest:
							break
					elif self.lower!=None:
						if not (self.higher==tile.highest) and not(self.lower==tile.highest):
							
							break
				elif tile.lowest!=None: #4
					if self.lower == None:
						if not(self.higher == tile.highest) and not(self.higher==tile.lowest):
							break
					elif self.lower!=None:
						if not(self.higher == tile.highest) and not (self.higher == tile.lowest) and not(self.lower == tile.lowest) and not(self.lower==tile.highest):
							break
				self.set_elevation(tile) #updates the elevation of the rover each time it moves
				tile.set_occupant(self) #sets occupant on the tile the rover has just moved to
				
				if tile.is_explored==False:
					self.number_of_tiles+=1#5
				
				if tile.is_shaded(): #if the tile is shaded, then the rover loses charge
					self.charge -= 1
				#changing the tile each time the rover moves
				tile.set_occupant(self)
				tile.del_occupant() #deletes the occupant the rover has moved from
				self.y-=1
				if self.y < 0:#2
					self.y = planet.get_height()-1
				
				counter+=1
				
		elif direction == 'S': #1
			while counter < cycles : #3
				
				tile = planet.tiles[((self.y+1)%planet.height)*planet.width+self.x]
				if self.charge==0 and (tile.is_shaded()):
					break
				if tile.lowest == None: #4
					"""checks if the rover can do the movement elevation wise"""
					if self.lower == None:
						if self.higher!=tile.highest:
							
							break
					elif self.lower!=None:
						if not (self.higher==tile.highest) and not(self.lower==tile.highest):
							
							break
				elif tile.lowest!=None: #4
					if self.lower == None:
						if not(self.higher == tile.highest) and not(self.higher==tile.lowest):
							
							break
					elif self.lower!=None:
						if not(self.higher == tile.highest)  and not(self.higher == tile.lowest) and not(self.lower == tile.lowest) and not(self.lower==tile.highest):
							
							break
				
				self.set_elevation(tile) #updates the elevation of the rover each time it moves
				
				if tile.is_shaded(): #if the tile is shaded, then the rover loses charge
					self.charge -= 1
				if tile.is_explored==False: #5
					self.number_of_tiles+=1
				tile.set_occupant(self)
				tile.del_occupant()
				self.y+=1
				if self.y == planet.get_height(): #2
					self.y = 0
				
				counter+=1
		elif direction == 'W': #1
			while counter < cycles: #3
				
				tile = planet.tiles[self.y*planet.width+((self.x-1)%planet.width)]
				if self.charge==0 and (tile.is_shaded()):
					break
				if tile.lowest == None: #4
					"""checks if the rover can do the movement elevation wise"""
					if self.lower == None:
						if self.higher!=tile.highest:
							
							break
					elif self.lower!=None:
						if not (self.higher==tile.highest) and not(self.lower==tile.highest):
							
							break
				elif tile.lowest!=None: #4
					if self.lower == None:
						if not(self.higher == tile.highest) and not(self.higher==tile.lowest):
							
							break
					elif self.lower!=None:
						if not(self.higher == tile.highest)  and not(self.higher == tile.lowest) and not(self.lower == tile.lowest) and not(self.lower==tile.highest):
							
							break
				
				self.set_elevation(tile) #updates the elevation of the rover each time it moves
				
				
				if tile.is_explored==False: #5
					self.number_of_tiles+=1
				
				if tile.is_shaded(): #if the tile is shaded, then the rover loses charge
					self.charge -= 1
				tile.set_occupant(self)
				tile.del_occupant()
				self.x-=1
				if self.x < 0: #2
					self.x = planet.get_width()-1
				
				counter+=1
		elif direction == 'E': #1
			while counter < cycles: #3
				
				tile = planet.tiles[self.y*planet.width+((self.x+1)%planet.width)]
				if self.charge==0 and (tile.is_shaded()):
					break
				if tile.lowest == None: #4
					"""checks if the rover can do the movement elevation wise"""
					if self.lower == None:
						if self.higher!=tile.highest:

							break
					elif self.lower!=None:
						if not (self.higher==tile.highest) and not(self.lower==tile.highest):
							
							break
				elif tile.lowest!=None: #4
					if self.lower == None:
						if not(self.higher == tile.highest) and not(self.higher==tile.lowest):
							
							break
					elif self.lower!=None:
						if not(self.higher == tile.highest)  and not(self.higher == tile.lowest) and not(self.lower == tile.lowest) and not(self.lower==tile.highest):
							
							break
				self.set_elevation(tile) #updates the elevation of the rover each time it moves
				
				
				if tile.is_shaded(): #if the tile is shaded, then the rover loses charge
					self.charge -= 1
				if tile.is_explored==False: #5
					self.number_of_tiles+=1
				tile.set_occupant(self)
				tile.del_occupant()
			
				self.x+=1
				if self.x == planet.get_width(): #2
					self.x = 0
				
				counter+=1
		else: #if the movement direction is not valid
			print ("Cannot perform this command")
		
		return tile,self
			
	
	def wait(self, cycles,tile):
		"""
		The rover will wait for the specified cycles
		"""
		if not (tile.is_shaded()) and self.charge<100: #the charge will increase if it is waiting on the plains
			self.charge+=cycles
		else:
			pass
	def finish(self,planet): #if the user enters finish, the program will be calculating the percentage of the planet explored
		"""the percentage of the plaet explored will be returned"""
		percentage = 100*(self.number_of_tiles/(planet.width*planet.height))
		return percentage
	
