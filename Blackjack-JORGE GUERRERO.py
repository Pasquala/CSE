import random

player_val = 0
dealer_val = 0
deck = {'h_ace': 1, 'h_2': 2, 'h_3': 3, 'h_4': 4, 'h_5': 5, 'h_6': 6, 'h_7': 7, 'h_8': 8, 'h_9': 9, 'h_10': 10,
        'h_j': 10, 'h_q': 10, 'h_k': 10,
        'd_ace': 1, 'd_2': 2, 'd_3': 3, 'd_4': 4, 'd_5': 5, 'd_6': 6, 'd_7': 7, 'd_8': 8, 'd_9': 9, 'd_10': 10,
        'd_j': 10, 'd_q': 10, 'd_k': 10,
        'c_ace': 1, 'c_2': 2, 'c_3': 3, 'c_4': 4, 'c_5': 5, 'c_6': 6, 'c_7': 7, 'c_8': 8, 'c_9': 9, 'c_10': 10,
        'c_j': 10, 'c_q': 10, 'c_k': 10,
        's_ace': 1, 's_2': 2, 's_3': 3, 's_4': 4, 's_5': 5, 's_6': 6, 's_7': 7, 's_8': 8, 's_9': 9, 's_10': 10,
        's_j': 10, 's_q': 10, 's_k': 10}
card = ''
card_val = 0


def hit():
    global player_val, dealer_val, deck, card, card_val
    card, card_val = random.choice(list(d.keys()))


def stay():
    global player_val, dealer_val, deck, card, card_val


def bust():
    global player_val, dealer_val, deck, card, card_val


def check():
    global player_val, dealer_val, deck, card, card_val


def game_start():
    global player_val, dealer_val, deck, card, card_val
    while player_val < 22 and dealer_val < 22:
        if player_val == 21 or dealer_val == 21:
            check()
        elif player_val < 22 and dealer_val < 22:


game_start()