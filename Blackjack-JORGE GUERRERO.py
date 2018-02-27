import random
import sys

player_val = 0
dealer_val = 0
deck = {'heart': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'diamond': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'club': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
        'spade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]}
card = deck.popitem()
card_val = 0


def hit():
    global player_val, dealer_val, deck, card_val


def stay():
    global player_val, dealer_val, deck, card_val


def check():
    global player_val, dealer_val, deck, card_val


def game_start():
    global player_val, dealer_val, deck, card_val
    for x in range(2):
        player_val += int(card_val)
    print("(You draw two cards. Your cards add up to %d" % player_val)
    while player_val < 22 and dealer_val < 22:
        if player_val == 21 or dealer_val == 21:
            check()
        elif player_val < 22 and dealer_val < 22:
            print("Ya both are bust!")
            sys.exit()



game_start()