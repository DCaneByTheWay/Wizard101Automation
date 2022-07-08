import time
from AutomationSetup import *

time.sleep(1.5)

hasHit = False

# note that if enchant is already clicked, then no attack spells will be in grayscale
# therefore we must see if spell is available before enchant is clicked
while True:
    time.sleep(1)

    if inCardSelect():

        if trySpell('Frenzy'): continue
        if trySpell('SoundOfMusicology'):
            hasHit = True 
            continue
        if trySpell('StormLord'):
            hasHit = True 
            continue

        if hasHit:
            trySpell('Tempest')
            continue

        passRound()