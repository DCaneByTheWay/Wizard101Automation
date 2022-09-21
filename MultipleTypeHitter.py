import time
from AutomationSetup import *

time.sleep(1.5)

def roundOneHitter(roundOneShad):

    print('Round 1 Hitter')
    
    enteredBattle = False

    while True:
        time.sleep(1)

        if inCardSelect():
            enteredBattle = True

            if trySpell(roundOneShad): continue
            # uncomment line below if and only if you want to sacrifice time for damage
            #if trySpell('SquallWyvern', isItemCard=True): continue
            if trySpell('Tempest'): continue
            passRound()
        
        if outOfBattle() and enteredBattle:
            break

def roundTwoHitter(roundTwoShad):

    print('Round 2 Hitter')

    enteredBattle = False
    hasHit = False

    while True:
        time.sleep(1)

        if inCardSelect():

            enteredBattle = True

            if tryAura('Frenzy'): continue

            if trySpell(roundTwoShad):
                hasHit = True 
                continue
            if trySpell('StormLord'):
                hasHit = True 
                continue

            if hasHit:
                trySpell('Tempest')
                continue

            passRound()       

        if outOfBattle() and enteredBattle:
            break    


roundOneShad = 'GlowbugSquall'
roundTwoShad = 'GlowbugSquall'
#roundTwoShad = 'SoundOfMusicology'

roundOneHitter(roundOneShad)
roundOneHitter(roundOneShad)
roundTwoHitter(roundTwoShad)