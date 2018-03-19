class Item(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            player_inv.append(self)
            self.location = ''

        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)


class Food(Item):
    def __init__(self, name, location, tasty):
        super(Food, self).__init__(name, location)
        self.tasty = tasty

    def eat(self):
        if self.tasty:
            print('You eat the %s.\nIt was really tasty!' % self.name)
            self.location = ''
        elif not self.tasty:
            print('You eat the %s.\nIT WAS GROSS OH GOD IT WAS NASTY BLEHHHH! WHY DID YOU EAT THAT?!'
                  % (self.name,))


player_inv = []
item = Item('Jeff Jeff', 'RAINBOW')
item.get_pick_upped()
for item in player_inv:
    print(item.name)
spaghet = Food('Spaghet', 'SOMEWHERERRERERER OVAH DA RAINBAUW', False)
spaghet.eat()
