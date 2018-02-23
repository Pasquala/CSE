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


QUIETMEADOW_DESC = 'A beautiful serene meadow with a large rock in the middle. ' \
                   'There is a sign in front of the rock stating "Today is the day! Go explore!"' \
                   ' \nNorth of the rock you see the meadow continues,' \
                   ' everywhere else has cliffs too harsh to climb even with proper tools'

QUIETMEADOW = Room('Quiet Meadow Valley', QUIETMEADOW_DESC, 'MEADOWENTRANCE', 'BLNK', 'BLNK', 'BLNK', 'BLNK', 'BLNK')

current_node = QUIETMEADOW()
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

print(current_node['NAME'] + ',' + '\n' + current_node['DESCRIPTION'])

while True:
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command == 'cheeseburger':
        print('DON\'T TRUST THE DUCKS!!!')
    if command == 'fly':
        print('You cannot fly seeing as you are not a bird!')
    if command.upper() in directions:
        try:
            
        except:
            print('You cannot go this way!')
    else:
        print('Command not recognized')