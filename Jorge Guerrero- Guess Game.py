import random
import sys

winning_number = random.randint(1, 50)
guesses = 5
test_numerooooooo = winning_number
print(test_numerooooooo)
player_number = input('Choose a number between 1 and 50')


def compare(guess, lives):
    if lives <= 0:
        sys.exit(0)
    if guess == winning_number:
        print('You win! the number was %d and you had %d guesses left.' % (winning_number, guesses))
        sys.exit(0)
    elif guess > winning_number:
        lives -= 1
        print('Your number is too high! You now have %d guesses left.' % lives)
        compare(player_number, guesses)
    elif guess < winning_number:
        lives -=1
        print('Your number is too low! You now have %d guesses left.' % lives)
        compare(player_number,guesses)


compare(player_number, guesses)

