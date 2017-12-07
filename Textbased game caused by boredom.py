import random
import sys


print("You wake up in the middle of a small forest clearing, on top of a large tree stump with a soft bed of grass."
      " The soft glow of the moon illuminates your surroundings by a minute silver light.")
print('TAKE_NAP LOOK_AROUND CALL_FOR_HELP')
choice_1 = input('>_ ')


if choice_1 == 'TAKE_NAP':
    print("You shuffle around and flop over onto a soft bed of grass. You lie down to sleep until day, maybe lady luck"
          "will let you sleep peacefully?")
    input('CONTINUE:(PRESS ENTER)')
    survive_1 = random.randint(1,2)
    if survive_1 == 1:
        print("A harsh gust of wind hits against your body and sends shivers down your spine. A low growl in the middle"
              " of the night jolts you awake. You look around to see yourself surrounded by a pack of wolves!")
        print('RUN FIGHT ACCEPT_FATE')
        wolf_fight = input('>_')
        if wolf_fight == 'RUN':
            print("With a quick twist of your foot, you turn your whole body to where the biggest opening between the "
                  "wolves. You run and run as far as you can hearing the barks of the wolves and the sound of their "
                  "paws hitting the ground. You hear them gaining and you see up ahead something")
        elif wolf_fight == 'FIGHT':
            print("")
        elif wolf_fight == 'ACCEPT_FATE':
            print("")
    elif survive_1 == 2:
        print("A gentle cool breeze blows across the clearing and the moon slowly moves down the horizon. By luck you"
              "survive!")


if choice_1 == 'LOOK_AROUND':
    print("Looking around the clearing you search for a path, a sign, a signal, ANYTHING that could help you in your"
          "current situation")
    found_1 = random.randint(1,5)
    if found_1 == 1:
        print("You found a sturdy stick! Maybe you can use it for something.")
        inv_stick = True
    elif found_1 == 3:
        print("You found a sharp chipped stone! This may be useful for bashing and cutting something.")
        inv_stone = True
    elif found_1 == 5:
        print("You found a ")
