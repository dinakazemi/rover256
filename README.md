# rover256
This game involves exploring as much of a planet with a planetary rover without running out of power.

## How to launch the game?
Go to the home directory and run `python3 game.py` in the terminal to start the game.
## Main Menu
The player can enter any of these commands when they launch the program:
- Quit: When the user selects this menu item, your program must exit.
- START ```<level file>```: When the user selects this menu item, your game must load the level file `<level file>` specified
by the user. The input for the level file is a file path that, if exists, will load the level.
If the level file specified does not exist, the program will return back to the menu and display the
error:
`Level file could not be found`  
Sample level files have already been provided in the directory named `level`. 
If the level file can be found but the data is not structured properly (ie level file does not have the correct syntax), then the game should output:
`Unable to load level file`
- HELP: This will show the menu items available.  
```txt
START <level file> - Starts the game with a provided file.
QUIT - Quits the game
HELP - Shows this message
```  
## Level File 
The level file will contain data related to the game such as the planet’s dimensions, name, rover
placement and attributes and tile information.
The format of the file follows:  
```txt
[planet]
name,<name of planet>
width,<width of planet>
height,<height of planet>
rover,<x>,<y>
[tiles]
<terrain_type>,<highest elevation>[,<lowest elevation>]
```
The number of tiles is based on the dimensions of the planet. For example, if the width is 6 and the
height is 5, the number of tiles listed should be strictly 30.  
A level file is considered correctly structured if:
- There is exactly 4 fields specified under the planet section and the number of tiles match the
dimensions of the planet.
- The rover’s coordinates specified are greater than or equal to 0
- The rover’s coordinates must be within the bounds of the planet’s dimensions.
- Both width and height values need to be greater than or equal to 5.
- highest elevation is strictly greater than lowest elevation for a tile.  
The program is able to support loading any level file that uses this format. However, it also detects if level file is incorrectly structured.
## Planet
The planet is defined as a two dimensional grid of terrain tiles. All tiles are square-shaped and of unit length. Each tile will have different data as outlined in the Tile section.  
Planets are spherical and not flat. This means the left-most column of the grid should "meet up" with
the right-most column. Similarly, the top-most row should meet up with the bottom-most.
## Tiles
A planet is made of up many individual terrain tiles and each tile has the following properties:
- Elevation relative from 0 (can be negative or positive).
- Effect: Each tile will have its own effect on the rover. This will be described in the following
section Terrain and slope.
## Terrain & Slope
Terrain is an attribute of a tile. There are two allowed types of terrain:  
#### Terrain types
- " " - Unshaded Plains (exposed to sunlight) `plain`.
- "#" - Shaded Plains, `shaded`.
#### Elevation effect
- "+" - Elevated tile relative to the rover.
- "-" - Descended tile relative to the rover.

Tiles that are described by 2 elevation values are sloped. This will allow the rover to move up or down
elevation between the two given elevation values provided. The slope will only have a difference of 1
between the highest and lowest ( highest − lowest ).
- "\" - Down slope, allows for movement to lower level.
- "/" - Up slope, allows for movement to upper level.

As an example: shaded,0,-1  
If the rover has an elevation of -1, the tile would appear as an up slope. This allows the rover to
access tiles with elevation of 0.  
If the rover has an elevation of 0, the tile would appear as an down slope This allows the rover to
access tiles with elevation of -1.
## Rover
The rover is the object that the player controls during the game. It is represented with the H symbol
when it scans the area around it and must occupy a terrain tile at any given time.
- In the level file, the line rover,<x>,<y> indicates the rover’s starting position. For example,
rover,1,0 means that the rover starts at (x, y) coordinates (1, 0).
- Current coordinates (x, y).
- Battery charge, maximum charge is 100 and always starts with a charge of 100.
- Number of tiles it has explored.

The rover will move around on the planet’s surface, being able to explore different parts of the terrain.
The objective for the rover is to explore the entire surface, once the rover has explored the entire
planet or runs out of power, the player can type the `FINISH` command (specified in the following
section) to finish the game and output how much they explored of the planet.  
`You explored {percentage} % of {planet}`
### Battery
The rover will lose power when moving around shaded areas. Every time it moves to a shaded tile,
it will decrease the battery charge by 1. The battery charge stays the same while the rover moves on unshaded tiles. If the rover waits on an unshaded tile, it will recharge.
## Commands
Once the game has been started your program must be able to handle another set of commands from
the user. The user is able to input commands to their rover.  
The rover is able to see all tiles within a 5x5 box using the `SCAN` function.  
- `SCAN <type>` 

This command will draw the current surroundings of the rover. The type component will allow the
user to display the scannable area for `shade` and `elevation`. The following examples will outline
how it is displayed.  
An example of the player using `SCAN shade`  
``` txt
|#|#| | |#|
|#| | | |#|
|#| |H| |#|
| | | |#|#|
| | |#|#|#|
```
The # tiles are shaded, and the blank tiles are exposed to non-shaded. The display does not indicate
whether the rover is currently in the shade or exposed to sunlight.  
An example of the player using `SCAN elevation`
``` txt
|+| | | |+|
| | | | |+|
| | |H| |/|
|-| | | |+|
|-|\| |+|+|
```
Our rover is able to see the different bits of terrain and the player will be able to make decisions what to do. The + symbol denotes tiles that are above the rover, while - symbol denotes tiles that are below the rover.  
When drawing the scannable environment, your rover is always centred in the box. When a
rover has scanned, all tiles within the scanning view will be explored. 
- `MOVE <direction> <cycles>`

The directions that the user can specify are: N, E, S, W which correspond to North, East, South and
West.  
When you use move, you will specify how many tiles the rover will move for.  
Example: `MOVE N 15`  
Will attempt move the rover north by 15 tiles.  
When the rover has moved to a tile (in the previous example, 15 tiles) the tile will be considered as
explored.   
If the rover is instructed to move N cycles but encouters a tile in K cycles. Where K < N and
the tile’s elevation is different from the rover’s elevation, the rover will stop before the tile and only consume K cycles.  
If the rover is instructed to move N cycles during only shaded tiles but only has P power remaining,
where P < N, the rover will move P tiles.
- `WAIT <cycles>`

In the event that the rover is in shade, the battery cycles will not replenish. When the rover is in
sunlight (non-shaded area) and it is waiting, the battery will recharge. The rover will recharge based
on the number of cycles specified if it is in sunlight, otherwise it will remain at the same state.
- `STATS`

Your rover will have statistics of its current exploration, when this command is executed it will allow the player to see:
- How much they have explored.
- How much battery they have left.

Example output:  
`Explored: 60%`  
`Battery: 56/100`  
- `FINISH`

The rover will shut down and the game will end. The player can enter this if the rover runs out of
power or if they do not wish to keep playing.  
The game should print the message:  
`You explored {percentage} % of {planet}.`  




