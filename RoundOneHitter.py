import time
from AutomationSetup import *

time.sleep(1.5)

# note that if enchant is already clicked, then no attack spells will be in grayscale
# therefore we must see if spell is available before enchant is clicked
while True:
    # if epic is available, then we are in battle
    if spellIsAvailable('Epic') or spellIsAvailable('EnchantedTempest') or spellIsAvailable('EnchantedGlowbugSquall'):
        if spellIsAvailable('GlowbugSquall'):
            clickSpell('Epic')
            clickSpell('GlowbugSquall')
            clickSpell('EnchantedGlowbugSquall')

        elif spellIsAvailable('EnchantedGlowbugSquall'):
            clickSpell('EnchantedGlowbugSquall')

        elif spellIsAvailable('Tempest'):
            clickSpell('Epic')
            clickSpell('Tempest')
            clickSpell('EnchantedTempest')
            
        else:
            clickSpell('EnchantedTempest')
    else:
        time.sleep(2)
