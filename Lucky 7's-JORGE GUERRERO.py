import random

dice1 = 0
dice2 = 0
money = 15
rounds = 0
max_round = 0
max_money = 0


def gamble():
    global money, rounds, dice1, dice2, max_money, max_round
    if money > 0:
        if max_money < money:
            max_money = money
            max_round = rounds
        rounds += 1
        money -= 1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 + dice2 == 7:
            money += 5
            print('The number is %d. Ya won. You have played %d rounds and have $%d' % (dice1 + dice2, rounds, money))
            gamble()
        elif dice1 + dice2 != 7:
            print('The number is %d. Ya lost. You have played %d rounds and have $%d.' % (dice1 + dice2, rounds, money))
            gamble()
    else: print('Ya lost now git lost! It only took you %d games to be broke. '
                'Yer highest amount of money was $%d at round %d' % (rounds, max_money, max_round))


gamble()