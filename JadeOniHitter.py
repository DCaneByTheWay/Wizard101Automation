import time
from AutomationSetup import *

time.sleep(1.5)

jadeOniPosition = 'EnemyOne'

while time.sleep(1) == None:

    if inCardSelect():
        # glowbug first if possible (it can oneshot oni no buffs)
    
        if trySpell('GlowbugSquall'): continue
        if trySpell('Feint', jadeOniPosition, noEnchant=True): continue
        if trySpell('Triton', jadeOniPosition): continue
        passRound()



    #myKeyboard.press('w')
    #time.sleep(0.1)
    #myKeyboard.release('w')

'''
while True:
    time.sleep(3)
    mouse.move(screenLength / 2, screenHeight / 2)
    mouse.click('left')
   ''' 



'''
ctrlPressed = False
altPressed = False
comboPressed = False




def writeToFile(key):
    
    keydata = str(key)
    with open("log.txt", 'a') as f:
        f.write(keydata)

    if keydata == "'p'":
        exit()
        
def on_press(key):

    global ctrlPressed
    global altPressed
    global comboPressed

    keydata = str(key)

    if keydata == 'Key.ctrl_l':
        ctrlPressed = True

    if keydata == 'Key.alt_l':
        altPressed = True

    if ctrlPressed and altPressed:
        comboPressed = True

    if comboPressed:
        time.sleep(0.75)
        myKeyboard.press(Key.ctrl)

        myKeyboard.tap('a')
        time.sleep(0.125)
        myKeyboard.tap('c')

        myKeyboard.release(Key.ctrl)

        time.sleep(0.125)
        clipboardContents = pyperclip.paste()

        binaryStr = getBinary(clipboardContents);

        print(binaryStr)

        myKeyboard.type(binaryStr)
        #myKeyboard.tap(Key.enter)


        comboPressed = False
        altPressed = False
        ctrlPressed = False

def on_release(key):
    keydata = str(key)


    global ctrlPressed
    global altPressed
    if keydata == 'Key.ctrl_l':
        ctrlPressed = False

    if keydata == 'Key.alt_l':
        altPressed = False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



time.sleep(2)

myKeyboard
myKeyboard.type("amogus")
myKeyboard.press(Key.enter)

print('finished')
'''