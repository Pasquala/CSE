# print('Hello world')

# Jorge Guerrero

# b = 3
# a = 4

# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)

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


# import random
# print(random.randint(0, 10))


# Recasting
# c = '1'
# print(c ==1)  # we have a string and an int
# print(int(c) == 1)
# print(c == str(1))


# Comparisons

# print(1 ==1)  # Use a double equal sign
# print(1 != 2)  # 1 is not equal to 2
# print(not False)


# Lists

# the_count = [1, 2, 3, 4, 5]

# extra_supreme_burger = ['mozzarella cheese', 'beef', 'chips', 'sesame seed buns', 'lettuce', 'crispy bacon',
#                         'mac and cheese', 'swiss cheese', 'american cheese', 'provolone cheese', 'havarti cheese',
#                         'any add ons']

# print(extra_supreme_burger)
# print(extra_supreme_burger[0])
# print(extra_supreme_burger[2])
# print(len(extra_supreme_burger))
# print(len(the_count))


# Going through lists

# for extra_supreme_burger in extra_supreme_burger:
#     print(extra_supreme_burger)

# for num in the_count:
#     print(num * 2)

# length = len(extra_supreme_burger)
# range(5)  # A list of numbers 1 through 4
# range(len(extra_supreme_burger))  # Generates a list of all indices

# for num in range(len(extra_supreme_burger)):
#     item = extra_supreme_burger[num]
#     print('The item at index %d is %s' % (num, item))


# Recasting into a list

# strOne = 'Hello World!'
# listOne = list(strOne)
# print(listOne)
# listOne[11] = '.'
# print(listOne)


# Adding things to a list

# extra_supreme_burger.append('bacon bowl mac and cheese')
# print(extra_supreme_burger)


# Removing things from a list

# extra_supreme_burger.pop(8)
# print(extra_supreme_burger)
# extra_supreme_burger.remove('lettuce')
# print(extra_supreme_burger)

# Getting the alphabet

# import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)

# Making things lowercase

# strTwo = 'hElLo PeopLE hOw aM yOU?'
# lowercase = strTwo.lower()
# print(lowercase)


# Dictionaries - Made up of key: value pair


dictionary = {'name': 'Matthew', 'age': 14, 'height': 5 * 12}

#  Accessing things from a dictionary

# print(dictionary['name'])
# print(dictionary['age'])
# print(dictionary['height'])
# dictionary['profession'] = 'telemarketer'

# large_dictionary = {
#     'CA': 'California',
#     'AZ': 'Arizona',
#     'NY': 'Mississippi',
#     'OR': 'Oregon'
# }

# print(large_dictionary['NY'])

# larger_dictionary = {
#     'CA': [
#         'Fresno',
#         'San Francisco',
#         'San Jose',
#         'Sacramento',
#         'California City',
#         'Salinas'
#     ],
#     'AZ': [
#         'Phoenix',
#         'Tuscon'
#     ],
#     'NY': [
#         'New York City',
#         'Brooklyn'
#     ],
# }
# print(larger_dictionary['NY'])
# print(larger_dictionary['NY'][1])
# print(larger_dictionary['AZ'][1])

# largerer_dictionary = {
#     'CA': {
#         'NAME': 'California',
#         'POPULATION': 39250000,
#         'BORDER ST': [
#             'Oregon',
#             'Nevada',
#             'Arizona'
#         ]
#     },
#     'AZ': {
#         'NAME': 'Arizona',
#         'POPULATION': 6831000,
#         'BORDER ST': [
#             'California',
#             'Utah',
#             'Nevada',
#             'New Mexico'
#         ]
#     },
#     'NY': {
#         'NAME': 'New York',
#         'POPULATION': 19750000,
#         'BORDER ST': [
#             'Vermont',
#             'Massachusetts',
#             'Connecticut',
#             'Pennsylvania',
#             'New Jersey'
#         ]
#     }
# }


# current_node = largerer_dictionary['NY']
# print(current_node['NAME'])
# print(current_node['POPULATION'])

# Defining functions


# def hello_world():
#     print('Hello world')


# hello_world()


# def square(base):
#     return base ** 2


# print(square(3))


# def tip(bill):
#     tax_amt = bill * 0.18
#     total_bill = bill + tax_amt
#     return total_bill


# print(tip(100))


# def distance_formula(x1, x2, y1, y2):
#     inside = (x1 - x2) ** 2 + (y1 - y2) ** 2
#     answer = inside ** 0.5
#     return answer


# print(distance_formula(0, 3, 0, 4))


# def pythagorean_theorem(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c


# print(pythagorean_theorem(5, 12))