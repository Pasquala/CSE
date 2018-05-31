
# CLASSES START HERE!!!

# ROOM CLASSES


class CustomError(Exception):
    def __init__(self, message=None):
        self.message = message


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
        current_node = globals()[getattr(self, direction)]


# ITEM CLASSES


class Item(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            player_inv.append(self)
        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)

    def get_dropped(self):
        print('You set down the %s and give it a little pat.' % self.name)
        player_inv.remove(item)

    def get_looked_at(self):
        print(self.desc)


class KeyItem(Item):
    def __init__(self, name, desc):
        super(KeyItem, self).__init__(name, desc)

    def get_pick_upped(self):
        print('You grab the %s.' % self.name)
        key_inv.append(self)

    def get_dropped(self):
        print('You try to drop the %s... nawh its too valuable' % self.name)


class Food(Item):
    def __init__(self, name, desc, tasty):
        super(Food, self).__init__(name, desc)
        self.tasty = tasty

    def consume(self):
        if self in player_inv:
            if self.tasty:
                print('You eat the %s.\nIt was really tasty!' % self.name)
                player_inv.remove(self)
            elif not self.tasty:
                print('You eat the %s.\nIT WAS GROSS OH GOD IT WAS NASTY BLEHHHH! WHY DID YOU EAT THAT?!'
                      % (self.name,))
                player_inv.remove(self)
            else:
                print('You cannot eat what you don\'t have!')


class Drink(Food):
    def __init__(self, name, desc, tasty):
        super(Drink, self).__init__(name, desc, tasty)

    def consume(self):
        if self in player_inv:
            if self.tasty:
                print('You drink the %s.\nIt was really tasty!' % self.name)
                player_inv.remove(self)
            elif not self.tasty:
                print('You drink the %s.\nIT WAS GROSS OH GOD IT WAS NASTY BLEHHHH! WHY DID YOU DRINK THAT?!'
                      % (self.name,))
                player_inv.remove(self)
            else:
                print('You cannot drink what you don\'t have!')


class Toaster(KeyItem):
    def __init__(self, name, desc):
        super(Toaster, self).__init__(name, desc)

    def make_toast(self):
        if current_node == 'KITCHEN':
            print('You plug in the %s and you make some toast! It comes out and your look at the toast...\n'
                  'You see there are messages on the toast.\nYou try to make it out and it looks like a conversation '
                  'between two men and one of them is asking about a toaster' % self.name)
            if len(player_inv) > 10:
                toast.get_pick_upped()
            else:
                print('Ack! You don\'t have any space to put the toast in your pocket... so you eat it...')
                toast.consume()
        elif current_node != 'KITCHEN':
            print('You look around but you don\nt see anywhere to make toast... only if there was a kitchen somewhere.')


class Wearables(KeyItem):
    def __init__(self, name, desc, fab):
        super(Wearables, self).__init__(name, desc)
        self.fab = fab

    def wear(self):
        if self.fab:
            print('You put on the %s... OOO GUURRLLL U BE LUUKIN FAB THO' % self.name)
        elif not self.fab:
            print('You put on the %s... Eh... Could be better')


class Map(KeyItem):
    def __init__(self, name, desc):
        super(Map, self).__init__(name, desc)

    def fast_travel(self):
        print('You open the %s and look at it. The map is filled in with the rooms you have been in before and rooms'
              'you know the name of' % self.name)
        print('You hear a voice in your head.\nWhere would you like to travel?')
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
            'Second Floor Hallway': F2HALLWAY,
            'Dining Room': DININGROOM,
            'Kitchen': KITCHEN,
            'Common Room': LIVINGROOM,
            'Pretty Garden': GARDEN,
            'Trophy Room': TROPHYROOM,
            'Duck Room': DUCKROOM
        }
        teleport = input('>_')
        if teleport in room_dictionary:
            print('You close the map and shiny transparent golden wings wrap around you and teleport you to %s!'
                  % teleport)
            global current_node
            current_node = room_dictionary[teleport]
            current_node.visited = True
        else:
            print('You look over the map... it seems %s is not there.' % teleport)


class ShrinkRay(KeyItem):
    def __init__(self, name, desc):
        super(ShrinkRay, self).__init__(name, desc)

    def shrink_stuff(self):
        print('you look over the %s and realize it looks like it functions like a gun. you point at a nearby piece of '
              'junk and fire\nPOW!\nThe piece of junk shrinks? Oh welp now it\'s too small to find...' % self.name)


class Figurine(KeyItem):
    def __init__(self, name, desc):
        super(Figurine, self).__init__(name, desc)

    def get_pick_upped(self):
        print('You see the glint of a figurine, you pick it up and look at it. It\'s a limited edition %s Figurine!' %
              self.name + '\n' + self.desc)


# CHARACTER CLASSES


class Character(object):
    def __init__(self, name, description, dialogue, held_item, affinity):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item = held_item
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
                 'In the far north you see a building ' \
                 'To the west you see nothing but an impassable forest, ' \
                 'south there is the meadow you woke up at, \nand to the east you see a what might be a lake.'
lake = 'You look around and see a massive lake with a strange rock in the south part of the pond. ' \
       'The lake is crystal clear and you can clearly look at your reflection.\n' \
       'You might be able to swim to the strange rock to the south. To the west you can go back to the meadow\'s edge'
lakerock = 'You are on top of the rock island, farr off you can see a mansion in the distance along with a' \
           'green house inside the woods.\nAt the you take a quick breather and enjoy the refresing air with ' \
           'the majestic view look around the rock, feeling its smooth yet rough texture before spotting a hole. ' \
           'Inside you can see shining objects at the bottom along with a cool updraft.\n' \
           'To the north you can swim back to shore.'
lakecave = 'You are inside a medium-sized cave with beautiful crystals lining the walls and glistening in the light.' \
           '\nThe air is cold and slightly damp; below your feet there are small puddles of cold refresing water.' \
           ' Above you is the hole you came from.'

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
westfields = 'You stand at the edge of a really green forest, you look deeper into the forest and very easily hear ' \
             'the sound of a river rushing.\n To the north, you can go behind the house. ' \
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
           'and the floor is covered in an elegant carpet with intricate designs near the edges. \nTo the east there' \
           'is the path to a dining room. To the south there the path to the courtyard.\n' \
           'To the west there is a hallway' \
           'to a common room. Finally, there are stairs leading up to a second floor.'
f2hallway = ''
diningroom = 'The dining room is filled with beautiful furniture, with elegant silverware and place settings on ' \
             'the table. You walk around and look around.\nYou notice a knife stab on the table.\nYou the table ' \
             'cloth has a rip.\nTo the south there us the kitchen. To the west you can go to the grand atrium'
kitchen = ''
livingroom = ''
garden = 'You step into a garden just outside of the mansion, but fenced into its own secluded area.\n The air is ' \
         'filled with the sweet smell of nectar and despite the apparent age of the garden, the flowers are thriving ' \
         'with splashes of magnificent, vibrant, glorious colors.\nTo the north is the door back into the common room'
trophyroom = 'You step the trophy room. The west wall has a glass case with dust except for 15 small circles that are' \
             'clear of any dust.\nOn the glass case there is a box that reads "Speak the name of the one lost to the ' \
             'ducks" To the south there is the doorway to the common room.'
duckroom = 'You go inside the room and through the tunnel you see... one duck... a very large duck at that. ' \
           '\nGreat, James is at it again. Why does he always do this. Oh great, there\'s the toaster. To the south ' \
           'you can go back to the Trophy room.'

# MANSION F1 OBJECTS START HERE
COURTYARD = Room('Mansion Courtyard', courtyard, 'MAINROOM', '', 'MANSIONENTRANCE', '', '', '')
MAINROOM = Room('Great Atrium', mainroom, '', 'DININGROOM', 'COURTYARD', 'LIVINGROOM', 'F2HALLWAY', '')
F2HALLWAY = Room('Second Floor Hallway', f2hallway, '', '', '', '', '', 'MAINROOM')
DININGROOM = Room('Dining Room', diningroom, '', '', 'KITCHEN', 'MAINROOM', '', '')
KITCHEN = Room('Kitchen', kitchen, 'DININGROOM', '', '', '', '', '')
LIVINGROOM = Room('Common Room', livingroom, 'TROPHYROOM', 'MAINROOM', 'GARDEN', '', '', '')
GARDEN = Room('Pretty Garden', garden, 'LIVINGROOM', '', '', '', '', '')
TROPHYROOM = Room('Trophy Room', trophyroom, '', '', 'LIVINGROOM', '', '', '')
DUCKROOM = Room('Duck Room', duckroom, '', '', 'TROPHYROOM', '', '', '')

# GREEN FOREST STARTS HERE!!!


# GREEN FOREST DESCRIPTIONS START HERE
lushentrance = ''
forestbench = ''
entrancestonewall = ''
forestmaze = 'There are trees in all directions, You are on your own inside this forest...'
secondbench = ''
grovestonewall = ''
treeguard = ''
riverbank = ''
quietgrove = ''
sanctuary = ''

# GREEN FOREST OBJECTS START HERE

LUSHENTRANCE = Room('Lush Forest Entrance', lushentrance, 'DENSEFOREST', 'WESTFIELDS', 'FORESTBENCH', '', '', '')
FORESTBENCH = Room('Serene Bench', forestbench, 'LUSHENTRANCE', 'ENTRANCESTONEWALL', '', '', '', '')
ENTRANCESTONEWALL = Room('Strange Stone Wall', entrancestonewall, '', '', '', 'FORESTBENCH', '', '')
DENSEFOREST = Room('Very Dense Woods', forestmaze, 'DENSERFOREST', 'LUSHENTRANCE', 'LUSHENTRANCE', 'LUSHENTRANCE', '',
                   '')
DENSERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERFOREST', 'LUSHENTRANCE', 'DENSEFOREST', 'LUSHENTRANCE', '',
                    '')
DENSERERFOREST = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'DENSERERERFOREST', 'DENSERFOREST',
                      'LUSHENTRANCE', '', '')
DENSERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERERERERFOREST', 'LUSHENTRANCE', 'DENSERERERERFOREST',
                        'DENSERERFOREST', '', '')
DENSERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERFOREST', 'LUSHENTRANCE', 'DENSERERERERERFOREST',
                          'LUSHENTRANCE', '', '')
DENSERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERERFOREST', 'LUSHENTRANCE', 'LUSHENTRANCE',
                            'LUSHENTRANCE', '', '')
DENSERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERERERERERFOREST', 'LUSHENTRANCE',
                              'DENSERERERFOREST', 'LUSHENTRANCE', '', '')
DENSERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSEFORESTFAKE', 'DENSERERERERERERERERFOREST',
                                'DENSERERERERERERFOREST', 'LUSHENTRANCE', '', '')
DENSERERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERERERERERERERFOREST', 'LUSHENTRANCE',
                                  'LUSHENTRANCE', 'DENSERERERERERERERFOREST', '', '')
DENSERERERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'DENSERERERERERERERERERERFOREST',
                                    'DENSERERERERERERERERFOREST', 'LUSHENTRANCE', '', '')
DENSERERERERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE',
                                      'DENSERERERERERERERERERERERFOREST', 'LUSHENTRANCE',
                                      'DENSERERERERERERERERERFOREST', '', '')
DENSERERERERERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'LUSHENTRANCE',
                                        'DENSERERERERERERERERERERERERFOREST', 'DENSERERERERERERERERERERFOREST', '', '')
DENSERERERERERERERERERERERERFOREST = Room('Very Dense Woods', forestmaze, 'DENSERERERERERERERERERERERFOREST',
                                          'SECONDBENCH', 'LUSHENTRANCE', 'DENSEFORESTEXTRAFAKE', '', '')
DENSEFORESTFAKE = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'LUSHENTRANCE',
                       'DENSERERERERERERERFOREST', 'DENSEFORESTFAKEFAKE', '', '')
DENSEFORESTFAKEFAKE = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'LUSHENTRANCE', 'DENSEFORESTFAKEFAKEFAKE',
                           'LUSHENTRANCE', '', '')
DENSEFORESTFAKEFAKEFAKE = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'LUSHENTRANCE', 'LUSHENTRANCE',
                               'LUSHENTRANCE', 'LUSHENTRANCE', 'LUSHENTRANCE')
DENSEFORESTEXTRAFAKE = Room('Very Dense Woods', forestmaze, 'LUSHENTRANCE', 'DENSERERERERERERERERERERERERFOREST',
                            'DENSEFORESTEXTRAFAKEFAKE', 'LUSHENTRANCE', '', '')
DENSEFORESTEXTRAFAKEFAKE = Room('Very dense woods', forestmaze, 'LUSHENTRANCE', 'LUSHENTRANCE', 'LUSHENTRANCE',
                                'LUSHENTRANCE', 'LUSHENTRANCE', 'LUSHENTRANCE')
SECONDBENCH = Room('Calming Stone Bench', secondbench, 'TREEGUARD', '',
                   'GROVESTONEWALL','DENSERERERERERERERERERERERERFOREST', '', '')
GROVESTONEWALL = Room('Strange Stone Wall', grovestonewall, 'SECONDBENCH', '', '', '', '', '')
TREEGUARD = Room('Tree Altar', treeguard, '', 'RIVERBANK', 'SECONDBENCH', '', '', '')
RIVERBANK = Room('', riverbank, '', '', '', 'TREEGUARD', '', '')
QUIETGROVE = Room('', quietgrove, '', 'TREEGUARD', '', 'SANCTUARY', '', '')
SANCTUARY = Room('Sanctuary of Life', sanctuary, '', 'QUIETGROVE', '', '', '', '')

figurine_list = ['Mr. Wiebe', 'Wiebe "the duck" Wybe', 'Cheese God (not other friend???)', 'Gandwiebe the white',
                 'Mister Sir Man', 'Toaster', 'Troll eating smashed egg', 'Messed up bear', 'Great pyrenees', 'Mr. Wybe'
                 'Gas Station Wiebe', 'Teen Wiebe', 'One Duck', 'Crusty Soap', 'Problems (not friend???)']

# KEY ITEMS
magic_map = Map('Old Map', 'A very strange map. The more you walk, the more it fills itself in. on the bottom it reads '
                           '"Speak the word of movement. Focus your mind and say the word teleport. '
                           'The map will heed your call and take you with gilded wings"')
toaster = Toaster('Toaster', 'A very fancy red toaster that for some reason always has bread in it. You look it over...'
                             '\n...\n...\n...\nYou kinda want toast...\n\nYou should get toast\n\n...\n\n Get toast.')

# ITEMS

# MEADOW ITEMS
potato = Food('Delicious potato', 'A very yummy potato', True)
goldbag = Item('Bag of gold', 'A leather bag filled to the brim with gold coins')
rock = Item('Good Rock', 'A rock that is smooth on one side and has a flat and sharp edge on the other side')
waterbottle = Drink('Canteen of water', 'A metal bottle filled with refreshing', True)
stick = Item('Sturdy Stick', 'A very sturdy stick, maybe can be combined with something')

# MANSION ITEMS
toast = Food('Toast', 'It be some good toast', True)
spaghet = Food('Spaghet', 'Spaghet', True)
carrot = Food('Carrots', 'Very sweet smelling carrots', True)
ants_on_a_log = Food('Ants on a log', 'A stick of crisp celery covered in peanut butter and raisins. It good.', True)
shrink_ray = ShrinkRay('Shrink Ray', 'A very strange device that looks like a gun, but lets out a soft whirring noise')
half_eaten_sandwich = Food('Half eaten sandwich', 'A sandwich that is missing half of it... '
                                                  'maybe there the other half?', False)

# LUSH FOREST ITEMS
bomb = Item('Bomb', 'A round object the slowly crumbles if you rub it too hard, it smells like a variety of fruits and '
                    'other sweet smelling things such as honey. You feel like you should put it in a bathtub with '
                    'water...')
gem = Item('Fused Gems', 'A chunk of gems fused together to look what looks like a flower bud, every layer changing to '
                         'a different type and color, ranging from green alexandrite in the center to beautiful jade '
                         'at the bottom.\n You feel energy emanating from it')

# OTHER STUFF
inclined_toast = True
current_node = QUIETMEADOW
directions = ['north', 'east', 'south', 'west', 'up', 'down']
short_directions = ['n', 'e', 's', 'w', 'u', 'd']
player_inv = [toast, potato, stick]
key_inv = [magic_map]
item_dictionary = {
    # MEADOW ITEMS
    'potato': potato,
    'bag of gold': goldbag,
    'rock': rock,
    'canteen of water': waterbottle,
    'sturdy stick': stick,


    # MANSION ITEMS
    'spaghetti': spaghet,
    'toaster': toaster,
    'ants on a log': ants_on_a_log,
    'shrink ray': shrink_ray,

    # LUSH FOREST ITEMS
    'bomb': bomb,
    'gem': gem,
    'old map': magic_map,
}
item_location_dictionary = {
    # MEADOW ITEMS
    'potato': QUIETMEADOW,
    'bag of gold': LAKECAVE,
    'rock': SOUTHFIELDS,
    'canteen of water': LAKE,
    'stick': WESTFIELDS,

    # MANSION ITEMS
    'spaghetti': DININGROOM,
    'toaster': DUCKROOM,
    'ants on a log': GARDEN,

    # LUSH FOREST ITEMS
    'bomb': LUSHENTRANCE,
    'gem': DENSERERERERERFOREST
}
room_item_name_dictionary = {
    # MEADOW ITEMS
    QUIETMEADOW: 'potato',
    LAKECAVE: 'bag of gold',
    SOUTHFIELDS: 'rock',
    LAKE: 'water bottle',
    WESTFIELDS: 'stick',


    # MANSION ITEMS
    DININGROOM: 'spaghetti',
    DUCKROOM: 'toaster',
    GARDEN: 'ants on a log',
    LUSHENTRANCE: 'bomb',
    DENSERERERERERFOREST: 'gem',
}

print('WELCOME TO DORK! DORK: The legend of dork is a text based game created by Jorge G. \n'
      'The basic commands are:\n'
      'north/east/south/west/up/down: Move to the corresponding directions. \n'
      'n/e/s/w/u/d: Move to the corresponding directions. \n'
      'look/room: Look at the room\'s description. \n'
      'check/item: Look at an item\'s description. \n'
      'inventory/inv/i: Displays Player inventory. \n'
      'pickup/take: Take an item. \n'
      'drop/leave: Drop an item. \n'
      'eat/drink/consume: Eat a food/drink item. \n'
      'There are other hidden commands but it is up to you to find them!')

# song here

print('\n' + '\n' + 'The sounds of the night fill the air with quiet gentle noises... You have no idea what happened...'
                    '\nLast you could remember, you were in a fight with someone you care for...\n'
                    'You feel bad for it...'
                    'Then you angrily stepped out, picking a direction and going for a walk. You are now somewhere in a'
                    'valley, the grass looks so beautiful and untouched by humans, you go back to sleep, curling up on '
                    'a rock...\n\n'
                    'You wake up on a rock...'
                    '\n\n')

while True:

    # Room desc stuffs

    print('')
    print(current_node.name)
    if not current_node.visited:
        print(current_node.description)
        print('The following items are here:')
        try:
            if room_item_name_dictionary[current_node]:
                print(room_item_name_dictionary[current_node])
        except KeyError:
            print('There are no items here.')
    command = input('>_').lower().strip()

    if command in ['quit', 'exit']:
        quit(0)

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Ducks

    if command == 'cheeseburger':
        if current_node == TROPHYROOM:
            print('The wall crumbles and breaks down. A doorway is revealed and there is a dark tunnel.\n'
                  'In the tunnel you hear a strange squeak')
            TROPHYROOM.north = 'DUCKROOM'
        print('DON\'T TRUST THE DUCKS!!!')

    elif command == 'one duck':
        print('https://weneedtotalkabouttheducks.com')

    # Fun stuffs

    elif command == 'fly':
        print('FLY YOU FOOLS! FLYYYYYYYYYYYYYYYYY!...You cannot fly seeing as you are not a bird...')
    elif command == 'zork':
        print('Zork?!?! What\'s that? It sounds like a really old and hard text based game...')

    # Gates of Wiebe

    elif command == 'wiebe wybe':
        for wiebe in range(0, 99999):
            print('Mr. Wiebe')
        print('The gates of Wiebe have been opened! within the room of trophies, there lies your reward.')
        TROPHYROOM.name = 'You step the trophy room. The west wall has a glass case with dust except for 15 small ' \
                          'circles that are clear of any dust.\nOn the glass case there is a box that is now opened.' \
                          ' To the south there is the doorway to the common room.'
        maple_syrup = KeyItem('Maple Syrup', 'Very good maple syrup! Super sweet!')
        item_dictionary['maple syrup'] = maple_syrup
        item_location_dictionary['maple syrup'] = TROPHYROOM

    # Needed stuffs

    elif command in ['consume', 'eat', 'drink']:
        item_name = input('What? ').lower()
        food_dictionary = {
            'potato': potato,
            'delicious potato': potato,
            'toast': toast,
            'cooked bread': toast,
            'canteen of water': waterbottle,
            'water bottle': waterbottle,
            'water': waterbottle,
            'spaghetti': spaghet,
            'spaghet': spaghet,
            'carrots': carrot,
            'carrot': carrot,
            'ants on a log': ants_on_a_log,
        }
        try:
            item = food_dictionary[item_name]
            found = False
            if item in player_inv and item_name not in food_dictionary:
                raise KeyError
            if item in player_inv and item_name in food_dictionary:
                found = True
                item.consume()
            if not found:
                raise CustomError()
        except KeyError:
            print('You try to stuff the %s in your mouth... you cannot... stop...\n\n\n\n\n\n\n\n\n\n'
                  'WHAT ARE YOU DOING STAHP\n\n\n\n\nYes officer... this player... this player right here' % item_name)
        except CustomError:
            print("You try to take a bite out of an invisible %s! Mmmmmm! Nothingness tastes amazing!" % item_name)

    elif command in ['look', 'room']:
        print(current_node.description)
        try:
            if room_item_name_dictionary[current_node]:
                print(room_item_name_dictionary[current_node])
        except KeyError:
            print('There are no items here.')

    elif command in ['check', 'item']:
        print('What item do you wanna check?')
        command = input('>_ ')
        try:
            if command in item_dictionary:
                if item_dictionary[command] in player_inv:
                    print(item_dictionary[command].name + '\n' + item_dictionary[command].desc)
                elif item_dictionary[command] not in player_inv:
                    raise KeyError
            elif command in item_dictionary:
                raise KeyError
        except KeyError:
            print('Hmmm... you realize you don\'t have it...')

    elif command in ['teleport', 'warp', 'travel'] and magic_map in key_inv:
        magic_map.fast_travel()

    elif command in ['inventory', 'inv', 'i']:
        inv_len = 10 - len(player_inv)
        print('Inventory(%s)' % inv_len)
        for item in player_inv:
            print(item.name)
        print('')
        print('Key inventory')
        for item in key_inv:
            print(item.name)

    elif command in ['pick up', 'take']:
        found = False
        item_name = input('What? ')
        if item_name in item_dictionary and current_node == item_location_dictionary[item_name]:
            item = item_dictionary[item_name]
            item.get_pick_upped()
            del item_location_dictionary[item_name]
            del room_item_name_dictionary[current_node]
            found = True
        if not found:
            print("Not Found.")

    elif command in ['drop', 'leave']:
        if inclined_toast and current_node == DUCKROOM:
            print('You really wanna drop toast...')
            item_name = input('What? ')
            if item_dictionary[item_name] in player_inv:
                player_inv.remove(item_dictionary[item_name])
        elif not inclined_toast:
            item_name = input('What? ')

        elif item_name in item_dictionary:
            item = item_dictionary[item_name]
            if item in player_inv:
                player_inv.remove(item)
                item_location_dictionary[item_name] = current_node
                room_item_name_dictionary[current_node] = item_name

    elif command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
        except KeyError:
            print('You cannot go this way!')

    else:
        print('It work no')
