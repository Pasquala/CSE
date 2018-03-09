world_map = {
    'WESTHOUSE': {
        'NAME': 'West of house',
        'DESCRIPTION': 'You are west of a white house',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },

    'SOUTHHOUSE': {
        'NAME': 'South of house',
        'DESCRIPTION': 'You are south of a white house',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },

    'NORTHHOUSE': {
        'NAME': 'North of house',
        'DESCRIPTION': 'North of a white house',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}

world_map = {
        # MEADOW AREA STARTS HERE!!!
        'QUIETMEADOW': {
            'NAME': 'Quiet Meadow Valley',
            'DESCRIPTION': 'A beautiful serene meadow with a large rock in the middle. There is a sign in front of the '
                           'rock stating "Today is the day! Go explore!" \nNorth of the rock you see the meadow '
                           'continues, everywhere else has cliffs too harsh to climb even with proper tools',
            'PATHS': {
                'NORTH': 'MEADOWENTRANCE'
            }
        },
        'MEADOWENTRANCE': {
            'NAME': 'Meadow Entrance',
            'DESCRIPTION': 'The meadow starts fading into an open field. In the far north you see a building? To the '
                           'west you see nothing but an impassable forest, south there is the meadow you woke up at, '
                           '\nand to the east you see a what might be a lake. ',
            'PATHS': {
                'NORTH': 'SOUTHFIELDS',
                'EAST': 'LAKE',
                'SOUTH': 'QUIETMEADOW'
            }
        },
        'LAKE': {
            'NAME': 'Mirror Lake',
            'DESCRIPTION': 'You look around and see a massive lake with a strange rock in the south part of the pond. '
                           'The lake is crystal clear and you can clearly look at your reflection.\n'
                           'You might be able to swim to the strange rock',
            'PATHS': {
                'SOUTH': 'LAKEROCK',
                'WEST': 'MEADOWENTRANCE'
            }
        },
        'LAKEROCK': {
            'NAME': 'Strange Rock Island',
            'DESCRIPTION': 'You hop into the lake with a big splash and swim to the rock in the lake, when you reach '
                           'it, you drag yourself onto a smaller one nearby and catch your breath.\nYou get up and '
                           'look around the rock, feeling its smooth yet rough texture before spotting a hole. inside '
                           'you can see something shining and see the bottom.',
            'PATHS': {
                'NORTH': 'LAKE',
                'DOWN': 'LAKECAVE'
            }
        },
        'LAKECAVE': {
            'NAME': 'Crystal Cave',
            'DESCRIPTION': 'You look into the hole as you slide into it, ending up into a '
                           'medium-sized cave with beautiful crystals lining the walls and glistening in the light.\n'
                           'in the center you see a bag of gold. Above you is the hole you came from.',
            'PATHS': {
                'UP': 'LAKEROCK'
            }
        },
        # FIELDS AREA STARTS HERE!!!
        'SOUTHFIELDS': {
            'NAME': 'Fields of Exploration, South',
            'DESCRIPTION': 'You stumbled into a massive field! all around are little shiny objects such as rocks, you '
                           'look north to see a mansion and more field to the west, leading into a dense forest. '
                           '\nTo the east you can see the field leading into another forest but, '
                           'there are a lot of dead trees and other dead plant matter',
            'PATHS': {
                'NORTH': 'MANSIONENTRANCE',
                'EAST': 'EASTFIELDS',
                'WEST': 'WESTFIELDS',
                'SOUTH': 'MEADOWENTRANCE'
            }
        },
        'WESTFIELDS': {
            'NAME': 'Fields of Exploration, West',
            'DESCRIPTION': 'You stand at the edge of a really green forest, you notice a considerably sturdy stick. '
                           'You look deeper into the forest and very easily hear the sound of a river rushing. To the '
                           'north, you can go behind the house. To the south you can return to the south of the fields '
            'or, you can go venture into the forest',
            'PATHS': {
                'NORTH': 'BEHINDHOUSE',
                'SOUTH': 'SOUTHFIELDS',
                'WEST': 'LUSHENTRANCE'
            }
        },
        'MANSIONENTRANCE': {
            'NAME': 'Entrance to the Mansion',
            'DESCRIPTION': 'Walking up the the mansion you see its intricate designs but see something more peculiar, '
                           'the door is open enough that you can walk in.\nBy peeping through the open door you see a '
                           'courtyard leading to the actual house which is a little farther north.\nTo the west you '
                           'see the dense forest and can hear some sound coming from that area albeit faint. To the '
                           'east you can see more of the desolate forest.',
            'PATHS': {
                'NORTH': 'COURTYARD',
                'WEST': 'WESTFIELDS'
            }
        },
        # FOREST AREA STARTS HERE!!!
        'LUSHENTRANCE': {
            'NAME': 'Lush Forest Edge',
            'DESCRIPTION': 'You step into the forest. You look around and notice all the lush, soft, slightly damp '
                           'plant life.\nA ray of light shines through to the south and you can see a large boulder '
                           'next to a bench. To the north you can hear the sounds of water rushing louder as the '
                           'forest gets thicker.'
        },
        # MANSION AREA STARTS HERE!!!
}

TESTMOVE = input('>_')
current_node = world_map[TESTMOVE]
# current_node = world_map['QUIETMEADOW']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

# print('%s, \n %s' % (current_node['NAME'], current_node['DESCRIPTION']))
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
            name_of_node = current_node['PATHS'][command.upper()]
            current_node = world_map[name_of_node]
            print(current_node['NAME'] + ',' + '\n' + current_node['DESCRIPTION'])
        except KeyError:
            print('You cannot go this way!')
    else:
        print('Command not recognized')


# {
#     'START' : {
#     'Oh! Um... Hello There sir? W-Why did a giant portal appear and why did you come through it?',
#         '1': 'W-well my name is Harvey, I\'m a blue recruit in this base',
#         '2': 'This base is uh... Somewhere in La-La-Lamanthia? Lamantha? Lemanthia??',
#             '3': 'Eeaarrtthh? Eaarth? what\'s an Eaarrrthhh? This is Sirca!',
#                 '4': 'Sirca is a ring world, it is ruled by the house of Omega.',
#             '5': 'Am I alone here? No of course not! There is Chedder and Hartman and Dad and Pas and Re... Um...',
#                 '6': 'R-Rei...? Well he was our old CO but... he had to leave...',
#         'END': 'Goodbye sir.'
#     }
# }