class Room(object):
    def __init__(self, name, description, north, east, south, west, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self,direction)]


# MEADOW AREA STARTS HERE!!!

# MEADOW AREA DESCRIPTIONS START HERE!!!
quietmeadow = 'A beautiful serene meadow with a large rock in the middle. ' \
                   'There is a sign in front of the rock stating "Today is the day! Go explore!"' \
                   ' \nNorth of the rock you see the meadow continues,' \
                   ' everywhere else has cliffs too harsh to climb even with proper tools'
meadowentrance = 'The meadow starts fading into an open field. ' \
                 'In the far north you see a building? ' \
                 'To the west you see nothing but an impassable forest, ' \
                 'south there is the meadow you woke up at, \nand to the east you see a what might be a lake.'

# MEADOW AREA OBJECTS START HERE!!!
QUIETMEADOW = Room('Quiet Meadow Valley', quietmeadow, 'MEADOWENTRANCE', '', '', '', '', '')
MEADOWENTRANCE = Room('Meadow Entrance', meadowentrance, 'SOUTHFIELDS', 'LAKE', 'QUIETMEADOW', '', '', '')

current_node = QUIETMEADOW
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node.name)
    command = input('>_')
    if command == 'quit':
        quit(0)
    elif command == 'cheeseburger':
        print('DON\'T TRUST THE DUCKS!!!')
    elif command == 'fly':
        print('You cannot fly seeing as you are not a bird!')
    elif command.upper() in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You cannot go this way!')
    else:
        print('Command not recognized')