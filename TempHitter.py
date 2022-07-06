import time
from AutomationSetup import *

time.sleep(1.5)

# note that if enchant is already clicked, then no attack spells will be in grayscale
# therefore we must see if spell is available before enchant is clicked
while True:
    clickSpell('EnemyOne')
    time.sleep(0.3)
    clickSpell('EnemyTwo')
    time.sleep(0.3)
    clickSpell('EnemyThree')
    time.sleep(0.3)
    clickSpell('EnemyFour')
    time.sleep(2)