class Item(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            
        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)


player_inv = []