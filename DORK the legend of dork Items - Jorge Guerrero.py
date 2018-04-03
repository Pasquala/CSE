class Item(object):
    def __init__(self, name, desc, location):
        self.name = name
        self.desc = desc
        self.location = location

    def get_pick_upped(self):
        if len(player_inv) < 10:
            print('You grab the %s.' % self.name)
            player_inv.append(self)
            self.location = ''
        elif len(player_inv) == 10:
            print('You have no space to carry the %s!' % self.name)

    def get_dropped(self):
        print('You set down the %s and give it a little pat.' % self.name)
        player_inv.remove(self)
        self.location = current_node

    def get_looked_at(self):
        print(self.desc)


class KeyItem(Item):
    def __init__(self, name, desc, location):
        super(KeyItem, self).__init__(name, desc, location)

    def get_pick_upped(self):
        print('You grab the %s.' % self.name)
        key_inv.append(self)
        self.location = ''


class Food(Item):
    def __init__(self, name, desc, location, tasty):
        super(Food, self).__init__(name, desc, location)
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
    def __init__(self, name, desc, location, tasty):
        super(Drink, self).__init__(name, desc, location, tasty)

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


class Toaster(KeyItem):
    def __init__(self, name, desc, location):
        super(Toaster, self).__init__(name, desc, location)

    def make_toast(self):
        if current_node == 'KITCHEN':
            print('You plug in the %s and you make some toast! It comes out and your look at the toast...\n'
                  'You see there are messages on the toast.\nYou try to make it out and it looks like a conversation '
                  'between two men and one of them is asking about a toaster' % self.name)
            toast = Food('Toast', 'It be some good toast', '', True)
            if len(player_inv) > 10:
                toast.get_pick_upped()
            else:
                print('Ack! You don\'t have any space to put the toast in your pocket... so you eat it...')
                toast.consume()
        elif current_node != 'KITCHEN':
            print('You look around but you don\nt see anywhere to make toast... only if there was a kitchen somewhere.')


class Wearables(KeyItem):
    def __init__(self, name, desc, location, fab):
        super(Wearables, self).__init__(name, desc, location)
        self.fab = fab

    def wear(self):
        if self.fab:
            print('You put on the %s... OOO GUURRLLL U BE LUUKIN FAB THO' % self.name)
        elif not self.fab:
            print('You put on the %s... Eh... Could be better')


class ShrinkRay(KeyItem):
    def __init__(self, name, desc, location):
        super(ShrinkRay, self).__init__(name, desc, location)

    def shrink_stuff(self):
        print('you look over the %s and realize it looks like it functions like a gun. you point at a nearby piece of '
              'junk and fire\nPOW!\nThe piece of junk shrinks? Oh welp now it\'s too small to find...' % self.name)


class Figurine(KeyItem):
    def __init__(self, name, desc, location):
        super(Figurine, self).__init__(name, desc, location)

    def get_pick_upped(self):
        print('You see the glint of a figurine, you pick it up and look at it. It\'s a limited edition %s Figurine!' %
              self.name + '\n' + self.desc)


current_node = 'RAWK'
jeffjeff = Item('Jeff Jeff', 'It Jeff Jeff', 'JEFFJEFFLAAANNNNDDDD')
spaghet = Food('Spaghet', 'Somebody\'s spaghet', 'SOMEWHERERRERERER OVAH DA RAINBAUW', True)
player_inv = [spaghet, jeffjeff]
figurine_list = ['mr wiebe', 'wiebe "the duck" wybe', 'Giant rubber duck', 'treeguard', 'Weibe 2.0', 'Mister Sir Man',
                 'toaster', 'Troll eating smashed egg', 'Messed up bear', 'Great pyrenees', 'Mr Wybe']
key_inv = []
for item in player_inv:
    print(item.name)
spaghet.consume()
for item in player_inv:
    print(item.name)
high_heels = Wearables('Lucky High Heels', 'You are wearing these lucky high heels... you feel fabulous', 'YES', True)
high_heels.wear()