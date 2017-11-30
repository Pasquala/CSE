# print('Hello world')

# Jorge Guerrero

# b = 3
# a = 4
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print('Try to figure out how this works')
# print(13 % 5)

# the "%" sign is a modulus. It finds the remainder.

# car_name = 'Weibe Mobile'
# car_type = 'BMW'
# car_cylinders = 8
# car_mpg = 5000.0

# print("I have a car called %s. It's pretty nice" % car_name)
# print("I have a car called %s. It's a %s" % (car_name, car_type))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# print("What is your name?")
# name = input(">_ ")
# print("Hello %s" % name)

# age = input("How old are you?")
# print("%s?! That's really old. You belong in a retirement home." % age)

# print('cheeseburgers or hamburgers?')
# answer = input('>_')
# if answer == 'cheeseburgers':
#     then: print('Correct')

# elif answer == 'hamburgers':
#     then: print '>_> what is wrong with you'

# else: print('I said cheeseburgers or hamburgers >:C')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def print_hw():
#     print('Hello World.')
#     print('Enjoy the day.')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print_hw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def say_hi(name): # Name is a "parameter"
#     print('Hello %s' % name)
#     print('Coding is great!')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# say_hi('Pasquala')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def print_age(name, age):
#     print('%s is %d years old' % (name, age))
#     age += 1
#     print('Next year, %s will be %d years old' % (name, age))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print_age('Pasquala', 14)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def algebra_hw(x):
#     return x**3 + 4*x**2 +7 * x - 4


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def grade_calc(percentage):
#     if percentage >= 90:
#         return 'A'
#     elif percentage >= 80:
#         return 'B'
#     elif percentage >= 70:
#         return 'C'
#     elif percentage >= 60:
#         return 'D'
#     else:
#         return 'F'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print (grade_calc(100))

# print('HERE AM UR TURTLESSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def happy_birthday(name):
#     if name == 'name':
#         name = input('name ')
#     print('Happy birthday to you!')
#     print('Happy birthday to you!')
#     print('Happy birthday dear %s,' % name)
#     print('Happy birthday to you!')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# happy_birthday('name')
# happy_birthday('Pas')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Loops

# for num in range(10):
#     print(num + 1)

# a = 1
# while a < 10:
#     print(a)
#     a += a


import random
print(random.randint(0, 10))