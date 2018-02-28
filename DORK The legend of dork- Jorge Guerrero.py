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
lake = 'You look around and see a massive lake with a strange rock in the south part of the pond. ' \
       'The lake is crystal clear and you can clearly look at your reflection.\n' \
       'You might be able to swim to the strange rock'
lakerock = 'You hop into the lake with a big splash and swim to the rock in the lake. ' \
           'When you reach it, you drag yourself onto a smaller one nearby and catch your breath.\nYou get up and ' \
           'look around the rock, feeling its smooth yet rough texture before spotting a hole. ' \
           'Inside you can see something shining and see the bottom.'
lakecave = 'You look into the hole as you slide into it, ending up into a medium-sized cave with beautiful crystals ' \
           'lining the walls and glistening in the light.\n' \
           'In the center you see a bag of gold. Above you is the hole you came from.'

# MEADOW AREA OBJECTS START HERE!!!
QUIETMEADOW = Room('Quiet Meadow Valley', quietmeadow, 'MEADOWENTRANCE', '', '', '', '', '')
MEADOWENTRANCE = Room('Meadow Entrance', meadowentrance, 'SOUTHFIELDS', 'LAKE', 'QUIETMEADOW', '', '', '')
LAKE = Room('Mirror lake', lake, '', '', 'LAKEROCK', 'MEADOWENTRANCE', '', '')
LAKEROCK = Room('Strange Rock Island', lakerock, 'LAKE', '', '', '', '', 'LAKECAVE')
LAKECAVE = Room('Crystal Cave', lakecave, '', '', '', '', 'LAKEROCK', '')

# FIELDS AREA STARTS HERE!!!

# FIELDS DESCRIPTIONS START HERE!!!
southfields = 'You stumbled into a massive field! all around are little shiny objects such as rocks, ' \
              'you look north to see a mansion and more field to the west, leading into a dense forest.\n' \
              'To the east you can see the field leading into another forest but, this forest seems dead and desolate'
westfields = 'You stand at the edge of a really green forest, you notice a considerably sturdy stick. ' \
             'You look deeper into the forest and very easily hear the sound of a river rushing.\n' \
             'To the north, you can go behind the house. ' \
             'To the south you can return to the south of the fields or, you can go venture into the forest.'
# FIELDS OBJECTS START HERE!!!
SOUTHFIELDS = Room('Fields of Exploration, South', southfields, 'MANSIONENTRANCE', 'EASTFIELDS', 'MEADOWENTRANCE',
                   'WESTFIELDS', '', '')
WESTFIELDS = Room('Fields of Exploration, West', westfields, 'BEHINDHOUSE', '', 'SOUTHFIELDS', 'LUSHENTRANCE', '', '')

current_node = QUIETMEADOW
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node.name)
    print(current_node.description)
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