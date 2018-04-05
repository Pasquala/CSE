# CLASSES START HERE!!!

# ROOM CLASSES


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


# ITEM CLASSES


class Item(object):
    def __init__(self, name, desc, location):
        self.name = name
        self.desc = desc
        self.location = location

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            player_inv.append(self)
            self.location = ''
        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)

    def get_dropped(self):
        print('You set down the %s and give it a little pat.' % self.name)
        player_inv.remove(self)
        self.location = current_node

    def get_looked_at(self):
        print(self.desc)


class KeyItem(Item):
    def __init__(self, name, desc, location):
        super(KeyItem, self).__init__(name, desc, location)

    def get_pick_upped(self):
        print('You grab the %s.' % self.name)
        key_inv.append(self)
        self.location = ''


class Food(Item):
    def __init__(self, name, desc, location, tasty):
        super(Food, self).__init__(name, desc, location)
        self.tasty = tasty

    def consume(self):
        if self in player_inv:
            if self.tasty:
                print('You eat the %s.\nIt was really tasty!' % self.name)
                self.location = ''
                player_inv.remove(self)
            elif not self.tasty:
                print('You eat the %s.\nIT WAS GROSS OH GOD IT WAS NASTY BLEHHHH! WHY DID YOU EAT THAT?!'
                      % (self.name,))
                player_inv.remove(self)
            else:
                print('You cannot eat what you don\'t have!')


class Drink(Food):
    def __init__(self, name, desc, location, tasty):
        super(Drink, self).__init__(name, desc, location, tasty)

    def consume(self):
        if self in player_inv:
            if self.tasty:
                print('You drink the %s.\nIt was really tasty!' % self.name)
                self.location = ''
                player_inv.remove(self)
            elif not self.tasty:
                print('You drink the %s.\nIT WAS GROSS OH GOD IT WAS NASTY BLEHHHH! WHY DID YOU DRINK THAT?!'
                      % (self.name,))
                player_inv.remove(self)
            else:
                print('You cannot drink what you don\'t have!')


class Toaster(KeyItem):
    def __init__(self, name, desc, location):
        super(Toaster, self).__init__(name, desc, location)

    def make_toast(self):
        if current_node == 'KITCHEN':
            print('You plug in the %s and you make some toast! It comes out and your look at the toast...\n'
                  'You see there are messages on the toast.\nYou try to make it out and it looks like a conversation '
                  'between two men and one of them is asking about a toaster' % self.name)
            toast = Food('Toast', 'It be some good toast', '', True)
            if len(player_inv) > 10:
                toast.get_pick_upped()
            else:
                print('Ack! You don\'t have any space to put the toast in your pocket... so you eat it...')
                toast.consume()
        elif current_node != 'KITCHEN':
            print('You look around but you don\nt see anywhere to make toast... only if there was a kitchen somewhere.')


class Wearables(KeyItem):
    def __init__(self, name, desc, location, fab):
        super(Wearables, self).__init__(name, desc, location)
        self.fab = fab

    def wear(self):
        if self.fab:
            print('You put on the %s... OOO GUURRLLL U BE LUUKIN FAB THO' % self.name)
        elif not self.fab:
            print('You put on the %s... Eh... Could be better')


class Map(KeyItem):
    def __init__(self, name, desc, location):
        super(Map, self).__init__(name, desc, location)

    def fast_travel(self):
        print('You open the %s and look at it. The map is filled in with the rooms you have been in before' % self.name)
        print('Where would you like to travel?')
        room_dictionary = {
            'Quiet Meadow Valley': QUIETMEADOW,
            'Meadow Entrance': MEADOWENTRANCE,
            'Mirror Lake': LAKE,
            'Strange Rock Island': LAKEROCK,
            'Crystal Cave': LAKECAVE,
            'Fields of Exploration, South': SOUTHFIELDS,
            'Fields of Exploration, West': WESTFIELDS,
            'Fields of Exploration, East': EASTFIELDS,
            'Mansion Entrance': MANSIONENTRANCE,
            'Behind The House': BEHINDHOUSE,
            'Mansion Courtyard': COURTYARD,
            'Great Atrium': MAINROOM,
            'Dining Room': DININGROOM,
            'Kitchen': KITCHEN,
            'Common Room': LIVINGROOM,
            'Pretty Garden': GARDEN,
            'Trophy Room': TROPHYROOM,
            'Duck Room': DUCKROOM
        }
        teleport = input('>_')



class ShrinkRay(KeyItem):
    def __init__(self, name, desc, location):
        super(ShrinkRay, self).__init__(name, desc, location)

    def shrink_stuff(self):
        print('you look over the %s and realize it looks like it functions like a gun. you point at a nearby piece of '
              'junk and fire\nPOW!\nThe piece of junk shrinks? Oh welp now it\'s too small to find...' % self.name)


class Figurine(KeyItem):
    def __init__(self, name, desc, location):
        super(Figurine, self).__init__(name, desc, location)

    def get_pick_upped(self):
        print('You see the glint of a figurine, you pick it up and look at it. It\'s a limited edition %s Figurine!' %
              self.name + '\n' + self.desc)


# CHARACTER CLASSES


class Character(object):
    def __init__(self, name, description, dialogue, item, affinity):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item = item
        self.affinity = affinity
        if self.item != '':
            self.holding = True
        else:
            self.holding = False

    def look(self):
        if self.holding:
            print(self.description + '\nYou ask the person about the item they have, '
                                     'they hold it up in response. ' + self.item)
        else:
            print(self.description)

    def speak(self):
        current_dia = self.dialogue['GREET']
        print(current_dia['START'] + '\n' + current_dia['START_P'])


# INSTANCES START HERE

# ROOMS INSTANCES


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
courtyard = 'Looking around, the courtyard is somewhat empty, '
mainroom = ''
diningroom = ''
kitchen = ''
livingroom = ''
garden = ''
trophyroom = ''
duckroom = 'You go inside the room and through the tunnel you see... one duck... a very large duck at that. ' \
           '\nGreat, James is at it again. Why does he always do this. Oh great, there\'s the toaster.'

# MANSION F1 OBJECTS START HERE
COURTYARD = Room('Mansion Courtyard', courtyard, 'MAINROOM', '', 'MANSIONENTRANCE', '', '', '')
MAINROOM = Room('Great Atrium', mainroom, '', 'DININGROOM', 'COURTYARD', 'LIVINGROOM', 'F2HALLWAY', '')
DININGROOM = Room('Dining Room', diningroom, '', '', 'KITCHEN', 'MAINROOM', '', '')
KITCHEN = Room('Kitchen', kitchen, 'DININGROOM', '', '', '', '', '')
LIVINGROOM = Room('Common Room', livingroom, 'TROPHYROOM', 'MAINROOM', 'GARDEN', '', '', '')
GARDEN = Room('Pretty Garden', garden, 'LIVINGROOM', '', '', '', '', '')
TROPHYROOM = Room('Trophy Room', trophyroom, '', '', 'LIVINGROOM', '', '', '')
DUCKROOM = Room('Duck Room', duckroom, '', '', 'TROPHYROOM', '', '', '')

# MANSION F2 DESCRIPTIONS START HERE!!!

# MANSION F2 OBJECTS START HERE!!!

# MANSION B1 DESCRIPTIONS START HERE!!!

# MANSION B1 OBJECTS START HERE!!!
