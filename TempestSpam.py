import time
from AutomationSetup import *

time.sleep(1.5)

while True:
    time.sleep(1)

    if inCardSelect():

        if trySpell('Tempest'): continue
        passRound()