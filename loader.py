
def load_level(filepath):
	"""
	Loads the level and returns None if the file is structurally incorrect and planet, rover, and tiles info otherwise
	"""
	correct_structure = True #a boolean checking the structure of the level file
	level_file = open(filepath,'r')
	contents = level_file.readlines()
	level_file.close()
	counter = 0
	for i in range(1,len(contents)):
		#counts the number of elements after the [planet] and before [tile]
		if not (contents[i].startswith('\n') or contents[i].startswith("[")):
			counter+=1
		else:
			break
	if counter!=4:
		#if we don't have exactly 4 fields after the planet it will exit the function printing out the relevant message
		correct_structure = False
		print ()
		
		print ("Unable to load level file")
		print ()
		return None
	width = None #width of the planet
	height = None #planet height
	rover_x=None #rover x position
	rover_y = None #rover y position
	name = None #plant name
	for i in contents:
		if i.startswith('name'): #initialising planet name
			name = i.split(',')[1]
		elif i.startswith('width'): #initialising width
			width = int(i.split(',')[1])
		elif i.startswith('height'): #initialising height
			height = int(i.split(',')[1])
		elif i.startswith('rover'): #initialising rover position
			if len(i.split(","))!=3: #if rover's arguments are missing
				correct_structure = False
				print ()
				
				print ("Unable to load the file")
				print ()
				return None
			rover_x = int(i.split(",")[1])
			rover_y = int(i.split(",")[2])
	if width == None or height == None or rover_x == None or rover_y == None or name==None: 
		"""if any of the above variables are not initialised then the file in structurally incorrect"""
		correct_structure = False
		print ()
		
		print ("Unable to load the file")
		print ()
		return None 
	number_of_tiles = 0 #variable containing the number of tiles
	c=0
	for i in range(1, len(contents)):
		#calculates the number of tiles in the file
		if contents[i].startswith("\n"):
			continue
		if contents[i].startswith("shaded") or contents[i].startswith("plains"):
			number_of_tiles+= 1
			if c==0:
				first_tile_index = i #stores the index of the first tile
			c+=1
	
	if width*height !=number_of_tiles:
		#checks if the number of tiles matches the dimensions of the planet
		correct_structure = False
		print ()
		
		print ("Unable to load level file")
		print ()
		return None
	if rover_x<0 or rover_y<0:
		#checks if the coordinates of rover is less than 0
		correct_structure = False
		print ()
		
		print("Unable to load level file")
		print ()
		return None
	if rover_x>=width or rover_y>=height:
		#checks if the coordinates of rover is whitihn the boundaries of the planet
		correct_structure = False
		print ()
		
		print ("Unable to load level file")
		print ()
		return None
	if width<5 or height<5:
		#checks whether the width and height of the planet is more than 5
		correct_structure = False
		print ()
		
		print("Unable to load level file")
		print ()
		return None
	
	for i in range(first_tile_index,len(contents)):
		#checks if all the tiles start with plain or shaded
		# if not (contents[i].split(",")[0]=='plains') and not(contents[i].split(",")[0]=='shaded'):
		# 	print (contents[i])
		# 	correct_structure = False
		# 	print ()
		# 	print ("not shade or plains")
		# 	print ("Unable to load the file")
		# 	print ()
		# 	return None
		if len(contents[i].split(","))>2:
			if int(contents[i].split(",")[1])<int(contents[i].split(",")[2]): #if highest elevation is lower than the lower elevation, which means structurally incorrect file
				correct_structure = False
				print ()
				
				print ("Unable to load level file")
				print ()
				return None
	if correct_structure:
		#if the file is structurally correct, the function returns planet's info, rover's position and a list of tiles
		tiles = []
		for i in range(first_tile_index,len(contents)):
			tiles.append(contents[i])
		return name, width,height,rover_x,rover_y,tiles
	else:
		print ()
		print ("Unable to load level file")
		print ()
		return None

