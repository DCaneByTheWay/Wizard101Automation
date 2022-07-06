from pynput.keyboard import Key, Controller, Listener
import pyautogui
import mouse
import random
import time

myKeyboard = Controller()

# gets image path given name
def getImagePath(imageName):
    imageFolderPath = '.\\SpellImages\\{name}.png'
    return imageFolderPath.format(name = imageName)

# returns tuple, the image on screen, and a boolean representing whether or not it exists
def locateImage(imageName, isEnchanted = False):

    confidenceLvl = 0.9

    '''# if 'Enemy' exists in the string
    if imageName.find('Enemy') != -1:
        print('searching', imageName)
        confidenceLvl = 0.8'''

    # THIS MAY BE REMOVED LATER
    # we need higher confidence if enchanted since it is similar to another card and can also be shiny
    if isEnchanted:
        confidenceLvl = 0.9

    res = pyautogui.locateOnScreen(getImagePath(imageName), grayscale=False, confidence=confidenceLvl)
    exists = False if res == None else True

    return res, exists

def getRandomX():

    x = random.randint(150,400)
    
    if random.randint(0,1) == 0:
        x = x * -1
    return x

def getRandomY():
    
    y = random.randint(200,600)
    
    if random.randint(0,1) == 0:
        y = y * -1
    return y

def getRandomDuration():
    return random.randint(15, 50) / 100

# given image name, move mouse to the image on screen, returns boolean of success
def moveToImage(imageName):
    res, exists = locateImage(imageName)

    if exists:
        print(f'Clicked {imageName}!')
        spellLocation = pyautogui.center(res)
        pyautogui.moveTo(spellLocation, duration = getRandomDuration())
        return True
    else:
        print(f'Failed to find {imageName}')
        return False

# finds and clicks spell from name
# overloaded valye target, if there is a target for spell, click target after
def clickSpell(spellName, target=None):
    imageFound = moveToImage(spellName)

    if imageFound:
        mouse.click()
        mouse.move(getRandomX(), getRandomY(), absolute = False, duration = getRandomDuration())
        time.sleep(0.5)

    # recursive calling to click on target if there is one
    if target != None:
        clickSpell(target)


def spellIsAvailable(spellName):
    res, exists = locateImage(spellName)

    if exists:
        return True
    return False
