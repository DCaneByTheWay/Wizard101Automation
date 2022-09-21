from pynput.keyboard import Controller, Key
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
    
    # if spell name contains enchanted
    if imageName.find('Enchanted') != -1:
        isEnchanted = True

    if isEnchanted:
        confidenceLvl = 0.7

    res = pyautogui.locateOnScreen(getImagePath(imageName), grayscale=False, confidence=confidenceLvl)
    exists = False if res == None else True

    return res, exists

# random x, y, and duration functions so i dont get banned :)
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
    return random.randint(20, 35) / 100

# given image name, move mouse to the image on screen, returns boolean of success
def moveToImage(imageName):
    res, exists = locateImage(imageName)

    if exists:
        spellLocation = pyautogui.center(res)
        pyautogui.moveTo(spellLocation, duration = getRandomDuration())
        time.sleep(0.2)
        print(f'Clicked {imageName}!')
        return True
    else:
        print(f'Failed to find {imageName}')
        return False

# finds and clicks spell from name
# overloaded valye target, if there is a target for spell, click target after
def clickSpell(spellName, target=None):
    imageFound = moveToImage(spellName)
    success = False

    if imageFound:
        mouse.click()
        # if we click an enemy icon, dont move (not on a card)
        if spellName.find('Enemy') == -1:
            mouse.move(getRandomX(), getRandomY(), absolute = False, duration = getRandomDuration())
        time.sleep(0.5)
        success = True

    # recursive calling to click on target if there is one
    if target != None:
        clickSpell(target)

    return success

# returns true if spell (image representing) is on screen, false otherwise
def spellIsAvailable(spellName):
    res, exists = locateImage(spellName)

    if exists:
        return True
    return False

# returns true if enemy (image representing) is on screen, false otherwise
def enemyAlive(enemyName):
    return spellIsAvailable(enemyName)

def getAllEnemiesLifeStatus():
    return enemyAlive('EnemyOne'), enemyAlive('EnemyTwo'), enemyAlive('EnemyThree'), enemyAlive('EnemyFour')

def getEnemyCount():
    count = 0

    enemyOneAlive, enemyTwoAlive, enemyThreeAlive, enemyFourAlive = getAllEnemiesLifeStatus()

    if enemyOneAlive:
        count = count + 1
    if enemyTwoAlive:
        count = count + 1
    if enemyThreeAlive:
        count = count + 1
    if enemyFourAlive:
        count = count + 1
    
    return count

# returns final enemy alive (if enemiesAlive > 1 then return first alive from left to right)
def getLastSurvivingEnemy():

    enemyOneAlive, enemyTwoAlive, enemyThreeAlive, enemyFourAlive = getAllEnemiesLifeStatus()

    if enemyOneAlive:
        return 'EnemyOne'
    if enemyTwoAlive:
        return 'EnemyTwo'
    if enemyThreeAlive:
        return 'EnemyThree'
    if enemyFourAlive:
        return 'EnemyFour'
    
# returns whether or not we are in card select, based on pass button existance
def inCardSelect():
    if spellIsAvailable('PassButton'):
        #moveToImage('QuickChatIcon')
        return True
    return False

# passes round
def passRound():
    clickSpell('PassButton')

# returns whether or not we are out of battle, based on pet icon button existance
def outOfBattle():
    return True if spellIsAvailable('PetIcon') else False

# does everything required to cast the given spell, returns success as boolean
def trySpell(spellName, target=None, isItemCard=False, noEnchant=False):

    success = False
    spellAvailable = spellIsAvailable(spellName)

    if isItemCard or noEnchant:
        if spellAvailable:
            success = clickSpell(spellName)

    else:
        enchantedSpellName = 'Enchanted{}'.format(spellName)
        enchantAvailable = spellIsAvailable(enchantedSpellName)

        if spellAvailable or enchantAvailable:
        
            if enchantAvailable:
                success = clickSpell(enchantedSpellName)

            elif spellAvailable:
                clickSpell('Epic')
                clickSpell(spellName)
                success = clickSpell(enchantedSpellName)
    
    if target != None and success == True:
        clickSpell(target)

    return success

def tryAura(spellName):
    return trySpell(spellName, noEnchant=True)


# presses key for duration
def pressReleaseKey(key, duration):
    time.sleep(0.2)
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)

def afkRun(direction='left'):
    
    if direction == 'right':
        direction = 'd'
    else:
        direction = 'a'

    time.sleep(0.2)
    myKeyboard.press(direction)
    myKeyboard.press('w')
    time.sleep(0.1)
    myKeyboard.press(Key.alt_l)
    time.sleep(0.2)
    myKeyboard.release(direction)
    myKeyboard.release('w')
    time.sleep(0.1)
    myKeyboard.release(Key.alt_l)
    