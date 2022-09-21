import time
from AutomationSetup import *

time.sleep(1.5)

hasHit = False

#shadHit = 'SoundOfMusicology'
shadHit ='GlowbugSquall'

while True:
    time.sleep(1)

    if inCardSelect():

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