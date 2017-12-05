import random
import sys

print("You wake up in the middle of a small forest clearing, on top of a large tree stump with a soft bed of grass."
      " The soft glow of the moon illuminates your surroundings by a minute silver light.")
print('TAKE_NAP LOOK_AROUND CALL_FOR_HELP')
choice_1 = input('>_ ')
if choice_1 == 'TAKE_NAP':
    print("You shuffle around and flop over onto a soft bed of grass. You lie down to sleep until day, maybe lady luck"
          "will let you sleep peacefully?")
    input('CONTINUE ')
    survive_1 = random.randint(1,2)
    if survive_1 == 1:
        print("A harsh gust of wind hits against your body and sends shivers down your spine. A low growl in the middle"
              " of the night jolts you awake. You look around to see yourself surrounded by a pack of wolves!")
        print('RUN FIGHT ACCEPT_FATE')
    elif survive_1 == 2:
        print("A gentle cool breeze blows across the clearing and the moon slowly moves down the horizon. By luck you"
              "survive!")
if choice_1 == 'LOOK_AROUND':
    print("Looking around the clearing you search for a path, a sign, a signal, ANYTHING that could help you in your"
          "current situation")