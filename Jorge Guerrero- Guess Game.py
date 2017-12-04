import random
import sys

winning_number = random.randint(1, 50)
chances = 5
# print(winning_number)
player_number = input('Choose a number between 1 and 50 ')


def compare(guess, lives):
    global winning_number, chances
    if lives <= 0:
        print('yer\' out of lives buddy ol\' pal friendo person human')
        sys.exit(0)
    if int(guess) == winning_number:
        print('You win! the number was %d and you had %d guess(es) left.' % (winning_number, lives))
        sys.exit(0)
    elif int(guess) > winning_number:
        lives -= 1
        chances = lives
        print('Your number is too high! You now have %d guesses left.' % lives)
        player_number = input('New number. Remember you are too high. ')
        compare(player_number, chances)
    elif int(guess) < winning_number:
        lives -=1
        chances = lives
        print('Your number is too low! You now have %d guesses left.' % lives)
        player_number = input('New number. Remember you are too low. ')
        compare(player_number,chances)


compare(player_number, chances)

