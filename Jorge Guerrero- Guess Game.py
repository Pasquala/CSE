import random
import sys

winning_number = random.randint(1, 50)
guesses = 5


def compare(player_number, guesses):
    if guesses <= 0:

    player_number = input('Choose a number between 1 and 50')
    if player_number == winning_number:
        print('You win! the number was %d and you had %d guesses left.' % (winning_number, guesses))
        sys.exit(0)
    elif player_number > winning_number:
        guesses -= 1
        print('Your number is too high! You now have %d guesses left.' % guesses)
        compare(player_number, guesses)
    elif player_number < winning_number:
        guesses -=1
        print('Your number is too low! You now have %d guesses left.' % guesses)
        compare(player_number,guesses)