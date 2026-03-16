import time
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

while True:

    time.sleep(1)

    if inCardSelect():
        if not isBattleOccuring:
            isBattleOccuring = True

        if tryShadowSpell('GlowbugSquall'): 
            hasHit = True
            continue
        
        if getEnemyCount() == 1:
            if trySpell('TreeOfStrife', getLastSurvivingEnemy()): 
                hasHit = True
                continue

        if hasHit:
            if getEnemyCount() == 1:
                if trySpell('MaxLightningBats', getLastSurvivingEnemy()): continue

        if trySpell('BunyipsRage'):
            hasHit = True
            continue
        
        if trySpell('Tempest'): 
            hasHit = True
            continue
        
        passRound()
        
    # end of battle logic
    if outOfBattle() and isBattleOccuring:
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