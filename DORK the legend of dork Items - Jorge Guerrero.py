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


class Keyitem(Item):
    def __init__(self, name, location):
        super(Keyitem, self).__init__(name, location)

    def get_pick_upped(self):
        print('You grab the %s.' % self.name)
        key_inv.append(self)
        self.location = ''


class Food(Item):
    def __init__(self, name, location, tasty):
        super(Food, self).__init__(name, location)
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
                print('You cannot eat what you dont have!')


class Drink(Food):
    def __init__(self, name, location, tasty):
        super(Drink, self).__init__(name, location, tasty)

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


class Toaster(Keyitem):
    def __init__(self):


jeffjeff = Item('Jeff Jeff', 'JEFFJEFFLAAANNNNDDDD')
spaghet = Food('Spaghet', 'SOMEWHERERRERERER OVAH DA RAINBAUW', True)
player_inv = [spaghet, jeffjeff]
key_inv = []
for item in player_inv:
    print(item.name)
spaghet.consume()
for item in player_inv:
    print(item.name)