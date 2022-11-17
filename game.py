import sys
import os
from loader import load_level
from planet import Planet
from terrain import Tile
from rover import Rover
def quit():
	"""
	Will quit the program
	"""
	sys.exit()
	
def menu_help():
	"""
	Displays the help menu of the game
	"""
	print ()
	print("START <level file> - Starts the game with a provided file.")
	print("QUIT - Quits the game")
	print ("HELP - Shows this message")
	print ()

def menu_start_game(filepath):
	"""
	Will start the game with the given file path. We need to check if the level file has the correct structure
	"""
	if load_level(filepath) == None:
		return None
	name,width,height,rover_x,rover_y,result = load_level(filepath)#extracting the info from the level file
	planet = Planet(name, width, height) #initialising the planet object
	rover = Rover(rover_x,rover_y) #initialising the rover
	tiles = []
	
	for i in result:
		"""creating a list of the whole tile objects in the planet"""
		i = i.strip()
		li = []
		for j in i.split(","):
			li.append(j)
		if len(li)==2: #if the tile only has a max elevation
			tiles.append(Tile(li[0],int(li[1])))
		elif len(li)==3: #if the tile has a min and max elevation
			tiles.append(Tile(li[0],int(li[1],),int(li[2])))
	return planet,rover,tiles #returning the planet, rover, and tiles for the use in the program #passes on the filepath to the loader file
def menu():
	"""
	Start the menu component of the game
	"""
	while True:
		user_menu_selection = input() #waits for the user to choose a menu option
		if user_menu_selection.split(" ")[0] == 'QUIT': #if the user wants to quit
			quit()
		elif user_menu_selection.split(" ")[0] == 'HELP':#in case user chooses HELP
			menu_help()
		elif user_menu_selection.split(" ")[0] == 'START':
			if len(user_menu_selection.split(" "))<2: #no filepath entered
				print ()
				print("Level file could not be found")
				print ()
			elif os.path.exists(user_menu_selection.split(" ")[1]): #the file path exists
				if menu_start_game(user_menu_selection.split(" ")[1])==None:
					continue
				else:
					planet,rover,tiles = menu_start_game(user_menu_selection.split(" ")[1])
					return planet,rover,tiles
			elif not os.path.exists(user_menu_selection.split(" ")[1]):# the filepath provided does not exist
				print ()
				print ("Level file could not be found")
				print ()
		else: #if the user selection is not valid.
			print()
			print ("No menu item")
			print ()
while True:
	planet,rover,tiles = menu()
	new_tile = tiles[rover.y*planet.width+rover.x] #initialising the first tile our rover is standing on
	planet.tile_setter(tiles) #setting the tiles on the planet
	new_tile.set_occupant(rover) #setting occupant on the first tile
	planet.rover_position_setter(rover) #initialising the position of the rover
	planet.planet_shaded_grid() #initialising the shaded grid of the planet
	planet.planet_elevation_grid(rover) #initialising the elevation grid of the planet
	is_finished = False
	while not is_finished:
		command = input()
		if command.startswith("SCAN"): #the user enters scan
			if len(command.split(" "))<2:
				print ("Cannot perform this command")
			else:

				planet.scan(command.split(" ")[1],rover)
		elif command.startswith("MOVE"): #the user enters move
			"""each time the rover is moved, we need to adjust set_occupant, rover_position setter, planet_shaded_grid, and planet_elevation_grid
			, for this reason, the move method has to return the last tile our rover finishes its movement on
			"""
			if len(command.split(" "))<3:
				print ("Cannot perform this command")
			else:
				try:
					command.split(" ")[2] = int(command.split(" ")[2])
					new_tile,rover = rover.move(command.split(" ")[1],int (command.split(" ")[2]),planet)

					planet.planet_shaded_grid()
					planet.planet_elevation_grid(rover)
				except ValueError: #if the cycle provided cannot be converted to int
					print ("Cannot perform this command")
					continue

		elif command.startswith("STATS"): #the user enters stats
			percentage = rover.finish(planet)
			print ()
			print("Explored: {:.0f}%".format(percentage))
			print ("Battery: {}/100".format(rover.charge))
			print()
		elif command.startswith("WAIT"): #user enters wait
			if len(command.split(" "))<2:
				print("Cannot perform this command")
			else:
				try:
					rover.wait(int(command.split(" ")[1]),new_tile)

				except ValueError: #cycles cannot be turned into int
					print ("Cannot perform this command")
					continue
		elif command.startswith("FINISH"): #user enters finish
			percentage = rover.finish(planet)
			print()
			print ("You explored {}% of {}".format(int(percentage), planet.get_name()))
			
			is_finished = True
		else:
			print ("Cannot perform this command")
