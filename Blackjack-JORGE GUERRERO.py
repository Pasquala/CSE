import random

player_val = 0
dealer_val = 0
deck = {'h_ace': '1', 'h_2': '2', 'h_3': '3'}

def hit():
    global player_val, dealer_val, deck


def stay():
    global player_val, dealer_val, deck


while player_val < 22 and dealer_val < 22:
    if player_val == 21 or dealer_val == 21:
        input("will you HIT or STAY ?")
