import time
import datetime
from AutomationSetup import *

time.sleep(1.5)

# variable to hold value of battles completed
battlesCompleted = 0
# variable to hold value to know whether or not main aoe has been used
hasHit = False
# variable to hold value to know whether or not we should be looking for battle end
isBattleOccuring = False

start = time.time_ns()
totalSeconds = 0

# uncomment shadhit you want to use
shadHit = 'SoundOfMusicology'
#shadHit ='GlowbugSquall'

while True:
    time.sleep(1)

    if inCardSelect():
        if not isBattleOccuring:
            isBattleOccuring = True

        if tryShadowSpell(shadHit):
            hasHit = True 
            continue

        if tryAura('Frenzy'): continue

        if trySpell('StormLord'):
            hasHit = True 
            continue

        if hasHit:
            trySpell('Tempest')
            continue

        passRound()

    # outside of battle logic
    if outOfBattle():

        #lookForX()
        #lookForTpRequest()

        # end of battle logic
        if isBattleOccuring:
            # reset vars
            hasHit = False
            isBattleOccuring = False
            # run to leave iframes faster
            afkRun()
            # update battles completed
            battlesCompleted += 1
            # print health mana info
            printHealthManaInfo()
            # print additional info
            printAutomationInfo(start, totalSeconds, battlesCompleted)