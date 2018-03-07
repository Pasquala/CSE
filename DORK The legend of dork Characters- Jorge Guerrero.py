class Chupadore(object):
    def __init__(self, name, description, dialogue, item, happiness):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item = item
        self.happiness = happiness


haavee = 'You look at one of the aliens, a "Chupadore", and what you see is short fluffy fur colored a light teal. He' \
         'has the regular blue recruit armor and he fiddles with a paper in his paws.\n' \
         'He looks very young compared to everyone else, about 12-13 human years.'
haavee_dia = []

HAAVEE = Chupadore('Harvey', haavee, haavee_dia, 'drawing', 85)
