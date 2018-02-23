import random
import sys


doggo_breeds = ['shiba inu', 'belgian shepard', 'german shepard', 'australian shepard', 'shetland sheepdog',
                'pembroke welsh corgi', 'siberian husky', 'lapponian herder', 'great pyrenees', 'border collie']

# EXPANSION PACKS!
doggo_breeds_expansion_1 = ['swedish vallhund', 'czechoslovakian wolfdog', 'golden retriever', 'alaskan malamute',
                            'greenland dog', 'canadian eskimo dog', 'chow chow', 'akita inu',
                            'australian cattle dog', 'beagle']

doggo_breeds += doggo_breeds_expansion_1


word = random.choice(doggo_breeds)
# print(word)
letters_the_player_guessed = []
hidden_word = []
# print(letters_the_player_guessed)
lives = 10

print('You have the basic english alphabet at your disposal; all spaces will be filled in!')

while lives > 0:
    # Prints what the player sees
    output = []
    for letter_in_the_word in word:
        if letter_in_the_word in letters_the_player_guessed:
            output.append(letter_in_the_word)
        elif letter_in_the_word == ' ':
            output.append(' ')
        else:
            output.append("*")
    print("".join(output))

    if "*" not in output:
        print('Ya win! Good job you had %d guesses left' % lives)
        sys.exit()

    player_input = input('Input a letter: ').lower()
    letters_the_player_guessed.append(player_input)
    print(letters_the_player_guessed)

    if player_input not in word:
        lives -= 1
        print('Wrong answer! -1 life, %d lives left!' % lives)


print('MAHN ME GABE YAH 10 CHAHNCES AHN YAH BLE ET! THUS HURE THAR WURD WUSH %s' % word)
