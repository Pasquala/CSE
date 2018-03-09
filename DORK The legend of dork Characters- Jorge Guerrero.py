class Chupadore(object):
    def __init__(self, name, description, dialogue, item, affinity):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item = item
        self.affinity = affinity

    def look(self):
        print(self.description + '\nYou ask him about the paper in the paws, he looks awkwardly and holds out the paper'
              + self.item)

    def speak(self):
        print('hi')


haavee_des = 'You look at one of the aliens, a "Chupadore", and what you see is short fluffy fur colored a ' \
             'light teal. He has some blue recruit armor and he fiddles with a paper in his paws.\n' \
         'He looks very young compared to everyone else, about 12-13 human years.'
haavee_dia = {
    'GREET': {
        'START': 'Oh! Um... Hello There sir? W-Why did a giant portal appear and why did you come through it?',
        'START_P':'Hello, I was messing about in and around a canyon next to an old mansion and I got dragged here',
        '1': 'Wait what do you mean you came from a mansion next to a canyon???',
    }
}

drawing = 'The drawing is a somewhat crude drawing of Harvey and another being that looks drastically different.\n' \
          'On the back there is a heart and in the heart it says \'For Harv!\''

haavee = Chupadore('Harvey', haavee_des, haavee_dia, drawing, 'Blue')

character = haavee
while True:
    command = input('>_').lower
    if command == 'quit':
        quit(0)
    elif command == 'look':
        character.look()
    elif command == 'speak':
        character.speak()
    else:
        print('Cammand nawht recongininized')