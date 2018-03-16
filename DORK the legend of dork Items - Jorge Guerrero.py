class Item(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            player_inv.append()

        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)


player_inv = []
item = Item('Jeff Jeff', 'RAINBOW')
item.get_pick_upped()
print(player_inv)