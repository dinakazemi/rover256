
class Planet:
	def __init__(self, name, width, height):
		"""
		Initialise the planet object
		"""
		self.name = name
		self.width = width
		self.height = height
		self.tiles = []
		self.grid_shaded = [] #a grid of the planet showing shaded tiles
		self.grid_elevation = [] #a grid of the planet showing elevations
	def get_name(self):
		"""returns the name of the planet"""
		return self.name
	def get_width(self):
		"""returns the width of the planet"""
		return self.width
	def get_height(self):
		return self.height
	def tile_setter(self,tiles):
		"""sets the tiles on the surface of a planet"""
		self.tiles = tiles
		
		return self.tiles
	def planet_shaded_grid(self):
		self.grid_shaded = []
		"""returns a map of the planet with shaded areas marked with #"""
		for i in range(0, self.height):
			self.grid_shaded.append([])
			
			for j in range(0,self.width):
				# print (i,j)
				# print (self.tiles[i*self.width+j].terrain_type,self.tiles[i*self.width+j].highest,self.tiles[i*self.width+j].lowest)
				if self.tiles[i*self.width+j].is_shaded():
					self.grid_shaded[i].append("#") #if the tile is shaded
				else:
					self.grid_shaded[i].append(" ")
		
		return self.grid_shaded
	def planet_elevation_grid(self,rover):
		self.grid_elevation = []
		
		"""returns an elevation map of the whole planet according to the rover's elevation"""
		for i in range (self.height):
			self.grid_elevation.append([])
			for j in range(self.width):
		
				highest,lowest = self.tiles[i*self.width+j].elevation()
				if lowest ==None: #if the tile does not have lower elevation
					if rover.lower == None: #the tile does not have lower height
						if highest == rover.higher:
							self.grid_elevation[i].append(" ") #the tile and the rover has the same elevation
						elif highest<rover.higher:
							self.grid_elevation[i].append("-") #tile is lower
						elif highest>rover.higher:
							self.grid_elevation[i].append("+")#tile is higher
					elif rover.lower!=None: #the rover has lower elevation
						if highest == rover.higher or highest == rover.lower:
							self.grid_elevation[i].append(" ")#the tile and the rover has the same elevation
						elif highest>rover.higher:
							self.grid_elevation[i].append("+") #tile is higher
						elif highest<rover.lower:
							self.grid_elevation[i].append("-") #tile is lower
				elif lowest!=None: #the tile has lower elevation
					if rover.lower==None: #rover does not have lower elevation
						if highest == rover.higher:
							self.grid_elevation[i].append("\\") #the tile is sloping down
						elif lowest == rover.higher:
							self.grid_elevation[i].append("/") #tile is sloping up
						elif highest<rover.higher:
							self.grid_elevation[i].append("-") #tile is lower
						elif lowest>rover.higher:
							self.grid_elevation[i].append("+") #tile is higher
					elif rover.lower!=None: #the rover has lower elevation
						if highest == rover.higher:
							
							self.grid_elevation[i].append(" ")#the tile and the rover has the same elevation
						elif highest==rover.lower:
							
							self.grid_elevation[i].append("\\") #tile is slopign down
						elif lowest == rover.higher:
							self.grid_elevation[i].append("/") #tile is sloping up
						elif highest>rover.higher:
							self.grid_elevation[i].append ("+") #tile is higher
						elif lowest<rover.lower:
							self.grid_elevation[i].append("-") #tile is lower
		
		return self.grid_elevation
	def rover_position_setter(self,rover):
		"""sets the position of the rover after each movement"""
		index = 0
		rover_tile = None
		for i in range(len(self.tiles)):
			if self.tiles[i].get_occupant()!=None: #when one of the tiles has an occupant, this is where the rover is standing on
				rover_tile = self.tiles[i]
				index = i
				break
		rover.x = index%self.width
		rover.y =  int(index/(self.width))
		return rover.x,rover.y
			
	def scan(self,type,rover):
		"""prints out a shade/elevation 5*5 map of the planet grid"""
		output = []
		counter = 0
		
		if type=='shade': #if the user wants shade grid
			for i in range(rover.y-2,rover.y+3): #traversing thruogh the rows
				output.append([])
				if i<0: #reaching the edges of the planet
					row= self.height+i
				elif i>self.height-1:#reaching the edges of the planet
					row = i%self.height
				else:
					row = i
				
				for j in range(rover.x-2,rover.x+3): #traversing through the columns
					if j<0:#reaching the edges of the planet
						column = self.width+j
					elif j>self.width-1:
						column = j%self.width#reaching the edges of the planet
					else:
						column = j
					if not (self.tiles[row*self.width+column].is_explored): #increasing the number of tiles explored for each tile that is scanned but not previuosly explored
						rover.number_of_tiles+=1
						self.tiles[row*self.width+column].is_explored = True
					output[counter].append(self.grid_shaded[row][column]) #takes the output from the planet's shaded grid
				counter+=1
			output[2][2] = 'H' #the center point is the rover itself with H
			print () 
			for i in output: #printing out the output
				print("|",end = '')
				for j in i:
					print(j+"|",end = '')
				print ()
			print ()
					
		elif type == 'elevation': #user selects elevation
			for i in range(rover.y-2,rover.y+3): #for loop for 5*5 square (rows)
				output.append([])
				if i<0: #if the scanning reaches the edges of the planet
					row= self.height+i
				elif i>self.height-1: #if the scanning reaches the edges of the planet
					row = i%self.height
				else:
					row = i
				
				for j in range(rover.x-2,rover.x+3):  #for loop for 5*5 square (columns)
					if j<0:  #if the scanning reaches the edges of the planet
						column = self.width+j
					elif j>self.width-1: #if the scanning reaches the edges of the planet
						column = j%self.width
					else:
						column = j
					
					if not (self.tiles[row*self.width+column].is_explored): #incrementing the number of tiles explored each for each tile that is scanned and not explored before
						rover.number_of_tiles+=1
						self.tiles[row*self.width+column].is_explored = True
					output[counter].append(self.grid_elevation[row][column]) #we produce the output based on the planet's elevation grid
				counter+=1
			output[2][2] = 'H' #center point which is the rover indicated by H
			print () #printing out the result
			for i in output:
				print("|",end = '')
				for j in i:
					print(j+"|",end = '')
				print ()
			print ()
					
		else: #if the inputted format is invalid.
			print ("Cannot perform this command")
			
	
	
	
	
