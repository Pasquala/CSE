class Chupadore(object):
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
            print(self.description + '\nYou ask the chupa about the item in their paws, '
                                     'they look at you and hold it up. ' + self.item)
        else:
            print(self.description)

    def speak(self):
        current_dia = self.dialogue['GREET']
        print(current_dia['START'] + '\n' + current_dia['START_P'])


harvey_des = 'You look at one of the aliens, a "Chupadore", and what you see is short fluffy fur colored a ' \
             'light teal. He has some blue recruit armor and he fiddles with a paper in his paws.\n' \
         'He looks very young compared to everyone else, about 12-13 human years.'
harvey_dia = {
    'GREET': {
        'START': 'Oh! Um... Hello There sir? W-Why did a giant portal appear and why did you come through it?',
        'START_P':'Hello, I was messing about in and around a canyon next to an old mansion and I got dragged here',
        '1': 'Wait what do you mean you came from a mansion next to a canyon???',
    }
}

drawing = 'The drawing is a somewhat crude drawing of Harvey and another being that looks drastically different.\n' \
          'On the back there is a heart and in the heart it says \'For Harv!\''

harvey = Chupadore('Harvey', harvey_des, harvey_dia, drawing, 'Blue')

character = harvey

while True:
    command = input('>_').lower().strip()
    if command == 'quit':
        exit(0)
    elif command == 'look':
        character.look()
    elif command == 'speak':
        character.speak()
    else:
        print('Cammand nawht recongininized')