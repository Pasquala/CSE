import random

dice = 0
money = 15
rounds = 0


def gamble():
    global money, rounds, dice
    if money > 0:
        rounds += 1
        money -= 1
        dice = random.randint(1,12)
        if dice == 7:
            money += 5
            print('The number is %d. Ya won. You have played %d rounds and have %d$' % (dice, rounds, money))
            gamble()
        elif dice != 7:
            print('The number is %d. Ya lost. You have played %d rounds and have %d$.' % (dice, rounds, money))
            gamble()
    else: print('Ya lost now git lost! It only took you %d games to be broke.' % rounds)


gamble()