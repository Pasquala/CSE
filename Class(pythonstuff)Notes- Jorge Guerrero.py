# Defining a class


# class Cheeseburger(object):
#     def __init__(self, patty_type, cheese):  # TWO underscores before and TWO after
#         self.patty = patty_type
#         self.cheese = cheese
#         self.eaten = False

    # def give(self, name):
    #     print(name + 'is thankful')

    # def cut(self):
    #     print('You cut the cheeseburger')

    # def eat(self):
    #     print('You eat the cheeseburger')
    #     self.eaten = True


# Instantiating (The creation of) two cheeseburgers
# burger1 = Cheeseburger('Beef', 'Havarti')
# burger2 = Cheeseburger('Bacon', 'Swiss')

# print(burger1.eaten)
# print(burger2.cheese)

# burger1.eat()
# print(burger1.eaten)
# print(burger2.eaten)


class Car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.moving = False

    def explode(self):
        print('3...2...1...KABOOM! The car blew up')

    def turn_on(self):
        if self.running:
            print('Nothing happens.')
        else:
            print('You turn on the car!')
            self.running = True

    def turn_off(self):
        if self.running:
            self.running = False
            print('You turn off the car.')
        else:
            print('The car is already off')

    def move_forward(self):
        if self.moving:
            print('You move faster. Whoa speeding up again? Wait You are double the speed limit o~o maybe slow down?'
                  'No, okay stop please your at 100mph. You slam down onto the gas pedal and lurch forward whoa stop!'
                  'OH GOD YOU BROKE THE SOUND BARRIER! WELP THERE GOES THE SPEED OF LIGHT, GOTTA GO FAST AMIRITE?!?')
        else:
            print('You start driving forward')
            self.moving = True

    def crash(self):
        print('For absolutely no reason you slam down on the gas and crash into a wall')

    def eat(self):
        print('You eat a cheeseburger from Mac n\' Bacon. It is really really good, you should go get more')

    def go_for_drive(self):
        if self.running:
            print('%d passengers get into the car' % self.passengers)
            self.move_forward()
            print('You casually violently break, doing a deus ex machina and stopping perfectly at your destination')
        else:
            print('The car is off')


Car('Fabmobile', 'Rainbow', 2, 123456789)

Car.turn_on()