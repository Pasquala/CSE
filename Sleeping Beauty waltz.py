import winsound
import time
import pygame


# winsound.Beep(466, 200)  # bB
# winsound.Beep(587, 100)  # D
# winsound.Beep(587, 100)  # D
# winsound.Beep(440, 200)  # A
# winsound.Beep(587, 100)  # D
# winsound.Beep(587, 100)  # D
# winsound.Beep(466, 200)  # bB
# winsound.Beep(390, 50)  # G
# winsound.Beep(440, 50)  # A
# winsound.Beep(466, 50)  # bB
# winsound.Beep(390, 50)  # G

pygame.mixer.init()
pygame.mixer.music.load("file.mp3")
pygame.mixer.play()


'''
Try to use a sound player instead of making beeps.
'''