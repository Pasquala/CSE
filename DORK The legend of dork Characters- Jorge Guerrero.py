class Chupadore(object):
    def __init__(self, name, description, dialogue, item, affinity):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item = item
        self.affinity = affinity


haavee = 'You look at one of the aliens, a "Chupadore", and what you see is short fluffy fur colored a light teal. He' \
         'has the regular blue recruit armor and he fiddles with a paper in his paws.\n' \
         'He looks very young compared to everyone else, about 12-13 human years.'
haavee_dia = {'0': 'Oh! Um... Hello There sir? W-Why did a giant portal appear and why did you come through it?',
              '1': 'W-well my name is Harvey, I\'m a blue recruit in this base',
              '2': 'This base is uh... Somewhere in La-La-Lamanthia? Lamantha, Lemanthia?',
              '3': 'Eeaarrtthh? Eaarth? what\'s an Eaarrrthhh? This is Sirca!',
              '4': 'Sirca is a ring world, it is ruled by the house of Omega.',
              '5': 'Am I alone here? No of course not! There is Chedder and Hartman and Dad and Pas and Re... Um...',
              }

drawing = 'The drawing is a somewhat crude drawing of Harvey and another being that looks drastically different. ' \
          'On the back there is a heart and in the heart it says \'For Harv!\''

HAAVEE = Chupadore('Harvey', haavee, haavee_dia, drawing, 'Blue')

