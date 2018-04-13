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
        self.visited = False

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self,direction)]


# MEADOW AREA STARTS HERE!!!

# MEADOW AREA DESCRIPTIONS
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
       'You might be able to swim to the strange rock to the south. To the west you can go back to the meadow\'s edge'
lakerock = 'You make your way to the top of the rock island. At the top you can see the area around you after ' \
           'catching your breath.\nYou get up and ' \
           'look around the rock, feeling its smooth yet rough texture before spotting a hole. ' \
           'Inside you can see something shining and see the bottom.\n' \
           'To the north you can swim back to shore.'
lakecave = 'You look into the hole as you slide into it, ending up into a medium-sized cave with beautiful crystals ' \
           'lining the walls and glistening in the light.\n' \
           'In the center you see a bag of gold. Above you is the hole you came from.'

# MEADOW AREA OBJECTS START HERE
QUIETMEADOW = Room('Quiet Meadow Valley', quietmeadow, 'MEADOWENTRANCE', '', '', '', '', '')
MEADOWENTRANCE = Room('Meadow Entrance', meadowentrance, 'SOUTHFIELDS', 'LAKE', 'QUIETMEADOW', '', '', '')
LAKE = Room('Mirror Lake', lake, '', '', 'LAKEROCK', 'MEADOWENTRANCE', '', '')
LAKEROCK = Room('Strange Rock Island', lakerock, 'LAKE', '', '', '', '', 'LAKECAVE')
LAKECAVE = Room('Crystal Cave', lakecave, '', '', '', '', 'LAKEROCK', '')


# FIELDS AREA STARTS HERE!!!

# FIELDS DESCRIPTIONS START HERE
southfields = 'You stumbled into a massive field! all around are little shiny objects such as rocks, ' \
              'you look north to see a mansion and more field to the west, leading into a dense forest.\n' \
              'To the east you can see the field leading into another forest but, this forest seems dead and desolate'
westfields = 'You stand at the edge of a really green forest, you notice a considerably sturdy stick. ' \
             'You look deeper into the forest and very easily hear the sound of a river rushing.\n' \
             'To the north, you can go behind the house. ' \
             'To the south you can return to the south of the fields or, you can go venture into the forest.'
eastfields = 'You stand at the edge of a thin forest, most the trees are dead and rotting. Though, parts of the ' \
             'forest are growing back and you can go east to venture in.\n' \
             'To the north you can go behind the mansion. To the south, you can travel back to the fields in the south.'
mansionentrance = 'Walking up the the mansion you see its intricate designs but see something more peculiar, ' \
                  'the door is open enough that you can walk in.\n' \
                  'By peeping through the open door you see a courtyard leading to the actual house which is a ' \
                  'little farther north.\n' \
                  'To the west you see the dense forest and can hear some sound coming from that area albeit faint. ' \
                  'To the east you can see more of the desolate forest.'
behindhouse = 'You stumble upon the back of the house. It looks relatively blank other than a few plants there to ' \
              'decorate.\nThere are steep hills to the north, to the south there is obviously a giant mansion in ' \
              'the way, to the east and west there are the east fields and west fields respectively.'

# FIELDS OBJECTS START HERE
SOUTHFIELDS = Room('Fields of Exploration, South', southfields, 'MANSIONENTRANCE', 'EASTFIELDS', 'MEADOWENTRANCE',
                   'WESTFIELDS', '', '')
WESTFIELDS = Room('Fields of Exploration, West', westfields, 'BEHINDHOUSE', '', 'SOUTHFIELDS', 'LUSHENTRANCE', '', '')
EASTFIELDS = Room('Fields of Exploration, East', eastfields, 'BEHINDHOUSE', 'DESOLATEENTRANCE', 'SOUTHFIELDS', '', '',
                  '')
MANSIONENTRANCE = Room('Mansion Entrance', mansionentrance, 'COURTYARD', '', 'SOUTHFIELDS', '', '', '')
BEHINDHOUSE = Room('Behind The House', behindhouse, '', 'EASTFIELDS', '', 'WESTFIELDS', '', '')


# MANSION AREA STARTS HERE!!!

# MANSION F1 DESCRIPTIONS START HERE
courtyard = 'You step into the courtyard and looking around, the courtyard is somewhat empty.' \
            'There are elegant decorations all around the courtyard.\nThere are a few antique benches, chairs, ' \
            'tables, and other decorations to make the courtyard seem a bit more cozy.\nIn the center there is an ' \
            'open area perfect to stand in and be engulfed in a warm blanket of sunlight!'
mainroom = 'Stepping inside the actual mansion, the air is cool and still, with very little sound... It brings you ' \
           'peace and tranquility, you feel relaxed.\nThe room is furnished with some beautiful antique furniture ' \
           'and the floor is covered in an elegant carpet with intricate designs near the edges.'
diningroom = ''
kitchen = ''
livingroom = ''
garden = 'You step into a garden just outside of the mansion, but fenced into its own secluded area.\n The air is ' \
         'filled with the sweet smell of nectar and despite the apparent age of the garden, the flowers are thriving ' \
         'with splashes of magnificent, vibrant, glorious colors.\nTo the north is the door back into the common room.'
trophyroom = 'You step the trophy room. The west wall has a glass case with dust except for 15 small circles that are' \
             'clear of any dust.\nOn the glass case there is a box that reads "Speak the name of the one lost to the ' \
             'ducks" To the '
duckroom = 'You go inside the room and through the tunnel you see... one duck... a very large duck at that. ' \
           '\nGreat, James is at it again. Why does he always do this. Oh great, there\'s the toaster.\n' \
           'To the south you can go to back to the trophy room...'

# MANSION F1 OBJECTS START HERE
COURTYARD = Room('Mansion Courtyard', courtyard, 'MAINROOM', '', 'MANSIONENTRANCE', '', '', '')
MAINROOM = Room('Great Atrium', mainroom, '', 'DININGROOM', 'COURTYARD', 'LIVINGROOM', 'F2HALLWAY', '')
DININGROOM = Room('Dining Room', diningroom, '', '', 'KITCHEN', 'MAINROOM', '', '')
KITCHEN = Room('Kitchen', kitchen, 'DININGROOM', '', '', '', '', '')
LIVINGROOM = Room('Common Room', livingroom, 'TROPHYROOM', 'MAINROOM', 'GARDEN', '', '', '')
GARDEN = Room('Pretty Garden', garden, 'LIVINGROOM', '', '', '', '', '')
TROPHYROOM = Room('Trophy Room', trophyroom, '', '', 'LIVINGROOM', '', '', '')
DUCKROOM = Room('Duck Room', duckroom, '', '', 'TROPHYROOM', '', '', '')

# CONTROLLER CODE IS HERE!!!

current_node = QUIETMEADOW
directions = ['north', 'east', 'south', 'west', 'up', 'down']
short_directions = ['n', 'e', 's', 'w', 'u', 'd']


while True:
    print(current_node.name)
    if not current_node.visited:
        print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command == 'cheeseburger':
        if current_node == TROPHYROOM:
            print('The wall crumbles and breaks down. A doorway is revealed and there is a dark tunnel.\n'
                  'In the tunnel you hear a strange squeak')
            TROPHYROOM.north = 'DUCKROOM'
        print('DON\'T TRUST THE DUCKS!!!')
    elif command == 'fly':
        print('You cannot fly seeing as you are not a bird!')
    elif command == 'look':
        print(current_node.description)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    elif command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
        except KeyError:
            print('You cannot go this way!')
    else:
        print('Command not recognized')