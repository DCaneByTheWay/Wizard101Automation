from re import L
import time
from AutomationSetup import *

def resetAndJoinOni():
    # battle -> obelisk
    pressReleaseKey('a', 0.80)
    pressReleaseKey('w', 5.5)
    pressReleaseKey('x', 0.1)
    time.sleep(0.5)                 # extra time waiting for x presses and space presses due to game time
    pressReleaseKey('x', 0.1)
    time.sleep(0.5)
    pressReleaseKey(Key.space, 0.1)
    time.sleep(0.5)

    # obelisk -> oni
    pressReleaseKey('a', 0.73)
    pressReleaseKey('w', 6.5)

    # wait and check again to see if we made it to oni
    time.sleep(1)
    if outOfBattle:
        # if we didn't make it, adjust a little
        # I've found 2 or 3 outcomes, and this accounts for them
        pressReleaseKey('a', 0.85)
        pressReleaseKey('w', 2)

time.sleep(1.5)

jadeOniPosition = 'EnemyOne'
# variable to hold value to know whether or not we should be looking for battle end
isBattleOccuring = False

while time.sleep(1) == None:

    if inCardSelect():
        if not isBattleOccuring:
            isBattleOccuring = True

        # glowbug first if possible (it can oneshot oni no buffs)
        if trySpell('GlowbugSquall'): continue
        if trySpell('Feint', jadeOniPosition, noEnchant=True): continue
        if trySpell('Triton', jadeOniPosition): continue
        passRound()

    if outOfBattle() and isBattleOccuring:
        resetAndJoinOni()
        isBattleOccuring = False