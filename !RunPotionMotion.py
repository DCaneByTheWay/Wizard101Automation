import time
from AutomationSetup import *

'''PLACE WIZARD ON SIGIL, DO NOT PRESS X'''

'''*****CHANGE THIS TO HOW MANY POTS U NEED*****'''
potsToFill = 4

for i in range(potsToFill):

    time.sleep(4)

    # enter potion motion
    pressReleaseKey('x', 0.2)
    time.sleep(1.5)

    clickImage('PotionMotionButton')
    time.sleep(10)

    clickImage('MinigamePlayButton')
    time.sleep(1.5)

    playPotionMotion()
    exitPotionMotion()

print('Finished!')