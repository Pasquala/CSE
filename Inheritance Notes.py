class Vehicle(object):
    def __init__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat = seat
        self.max_speed = speed
        self.passengers = passengers

    def move(self):
        print('You move forward')

    def change_direction(self):
        print('You change directions')


class Car(Vehicle):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Car, self). __init__('engine', material, seat, speed, passengers)
        self.windows = windows

    def roll_down_windows(self):
        print('You roll the windows down')

    def turn_on(self):
        print('You turn the key and the engine starts')


test_car = Car('Aluminum', 'Driver side', 140, 2, True)
test_car.change_direction()


class KeylessCar(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(KeylessCar, self).__init__(material, seat, speed, passengers, windows)

    def turn_on(self):
        print('You push the button and the car turns on')


class Tesla(KeylessCar):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Tesla, self).__init__(material, seat, speed, passengers, windows)

    def crash(self):
        print('You violently jerk the steering wheel and crash into a pole. No one is hurt except for the car')


test_car.turn_on()
cool_car = KeylessCar('Aluminum', 'Driver side', 140, 2, True)
cool_car.turn_on()