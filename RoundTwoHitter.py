import time
from AutomationSetup import *

time.sleep(1.5)

# note that if enchant is already clicked, then no attack spells will be in grayscale
# therefore we must see if spell is available before enchant is clicked
while True:
    # if epic is available, then we are in battle
    if spellIsAvailable('Epic') or spellIsAvailable('EnchantedStormLord') or spellIsAvailable('EnchantedSoundOfMusicology'):

        if spellIsAvailable('Frenzy'):
            clickSpell('Frenzy');
            continue

        if spellIsAvailable('SoundOfMusicology'):
            clickSpell('Epic')
            clickSpell('SoundOfMusicology')
            clickSpell('EnchantedSoundOfMusicology')

        elif spellIsAvailable('EnchantedSoundOfMusicology'):
            clickSpell('EnchantedSoundOfMusicology')

        elif spellIsAvailable('StormLord'):
            clickSpell('Epic')
            clickSpell('StormLord')
            clickSpell('EnchantedStormLord')
            
        else:
            clickSpell('EnchantedStormLord')
    else:
        time.sleep(2)