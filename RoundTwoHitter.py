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

shadHit = 'SoundOfMusicology'
#shadHit ='GlowbugSquall'

while True:
    #time.sleep(1)

    if inCardSelect():
        if not isBattleOccuring:
            isBattleOccuring = True

        if tryAura('Frenzy'): continue

        if trySpell(shadHit):
            hasHit = True 
            continue

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
            # print health mana
            printHealthManaInfo()
            # update battles completed
            battlesCompleted += 1
            print('Battles Completed:', battlesCompleted)
            # get time
            currentTime = time.time_ns()
            totalNano = totalSeconds * 1000000000
            runTime = (currentTime - start - totalNano) / 1000000000 
            totalSeconds += runTime
            avg = totalSeconds / battlesCompleted
            # format time to print
            formattedTime = str(datetime.timedelta(seconds=totalSeconds))
            formattedTime = formattedTime[0:len(formattedTime)-3]
            # print time
            print(f'Total Time Running: {formattedTime}')
            print(f'Average Run Time: {avg:.3f}')
            print(f'This Run: {runTime:.3f}')
            print()