from pynput.keyboard import Controller, Key
import pyautogui
import mouse
import random
import time
import numpy as nm  
import pytesseract
import cv2
from PIL import ImageGrab

myKeyboard = Controller()

# monitor size: I dont intend on using this a lot, just in some cases
MONITOR_DIMENSIONS = (1920, 1080)

# gets image path given name
def getImagePath(imageName):
    imageFolderPath = '.\\SpellImages\\{name}.png'
    return imageFolderPath.format(name = imageName)

# returns tuple, the image on screen, and a boolean representing whether or not it exists
def locateImage(imageName, isEnchanted = False):

    '''
    it looks random, but after extensive testing i've found
    that 91% confidence for regular spells and 76% confidence 
    for enchanted spells seems to be the most fitting, but there 
    may still be mistakes that are made
    '''

    # high confidence by default
    confidenceLvl = 0.91
    
    # if spell name contains enchanted
    if 'Enchanted' in imageName:
        isEnchanted = True

    # lower confidence level if enchanted due to shiny card making it harder to find
    if isEnchanted:
        confidenceLvl = 0.76

    # get and return location of image, and boolean of success    
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
def moveToImage(imageName, xOff=0, yOff=0):
    res, exists = locateImage(imageName)

    # if it exists, then move to img and print success in terminal, print failure otherwise
    if exists:
        imageLocation = pyautogui.center(res)

        # add offset 
        # (cannot update tuple, so tuple>list>tuple)
        temp = list(imageLocation)
        temp[0] += xOff
        temp[1] += yOff
        imageLocation = tuple(temp)


        # there are some issues with two monitors, we'll move the 
        # cursor back to the main monitor first, if it is beyond the boundaries

        # current position of cursor
        cursorX, cursorY = pyautogui.position()

        # move back to main monitor bounds if outside
        if (cursorX > MONITOR_DIMENSIONS[0] or cursorY > MONITOR_DIMENSIONS[1]):
        
            # move to top middle of monitor
            pyautogui.moveTo((MONITOR_DIMENSIONS[0] / 2, 50), duration = getRandomDuration())

        # move to the image
        pyautogui.moveTo(imageLocation, duration = getRandomDuration())
        time.sleep(0.2)
        print(f'Clicked {imageName}!')
        return True
    else:
        print(f'Failed to find {imageName}')
        return False

# finds and clicks spell from name
def clickSpell(spellName):
    imageFound = moveToImage(spellName)
    success = False

    if imageFound:
        mouse.click()

        # after each click, move to a random spot over a random duration
        # UNLESS we clicked an enemy, in which case we dont move
        if 'Enemy' not in spellName:
            mouse.move(getRandomX(), getRandomY(), absolute = False, duration = getRandomDuration())

        time.sleep(0.5)
        success = True

    return success

# given image name, moves to and clicks it
def clickImage(imageName):
    moveToImage(imageName)
    mouse.click()

# returns true if image is on screen, false otherwise
def imageIsAvailable(imageName):
    res, exists = locateImage(imageName)

    if exists:
        #print('found', imageName)
        return True
    #print('could not find', imageName)
    return False 

# returns true if spell (image representing) is on screen, false otherwise
def spellIsAvailable(spellName):
    return imageIsAvailable(spellName)

# returns true if enemy (image representing) is on screen, false otherwise
def enemyAlive(enemyName):
    return spellIsAvailable(enemyName)

# returns boolean for each enemy, alive -> true, dead -> false
def getAllEnemiesLifeStatus():
    return enemyAlive('EnemyOne'), enemyAlive('EnemyTwo'), enemyAlive('EnemyThree'), enemyAlive('EnemyFour')

# returns number of enemies in battle
def getEnemyCount():

    enemyOneAlive, enemyTwoAlive, enemyThreeAlive, enemyFourAlive = getAllEnemiesLifeStatus()

    return enemyOneAlive + enemyTwoAlive + enemyThreeAlive + enemyFourAlive

# returns final enemy alive (if enemiesAlive > 1, then return first alive from left to right)
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
    if imageIsAvailable('PassButton') or imageIsAvailable('PassButtonDark') or imageIsAvailable('PassButtonLit'):
        return True
    return False

# passes round
def passRound():
    clickSpell('PassButton')

# returns whether or not we are out of battle, based on pet icon button existance
def outOfBattle():
    return True if imageIsAvailable('PetIcon') else False

# does everything required to cast the given spell, returns success as boolean
# default enchant is epic, but you can overload with other enchants
def trySpell(spellName, target=None, isItemCard=False, noEnchant=False, enchant='Epic'):
    
    # default success is false
    success = False
    spellAvailable = spellIsAvailable(spellName)

    # if item card or specifically no enchant requested, click spell without enchant
    if isItemCard or noEnchant:
        if spellAvailable:
            success = clickSpell(spellName)

    # else enchant before hit
    else:
        enchantedSpellName = 'Enchanted{}'.format(spellName)
        enchantAvailable = spellIsAvailable(enchantedSpellName)

        # click enchant then click spell
        if spellAvailable or enchantAvailable:
        
            if enchantAvailable:
                success = clickSpell(enchantedSpellName)

            elif spellAvailable:
                clickSpell(enchant)
                clickSpell(spellName)
                success = clickSpell(enchantedSpellName)
    
    # if there is a target and we clicked the spell, click target
    if target != None and success == True:
        clickSpell(target)

    return success

# click aura if it exists
def tryAura(spellName):
    return trySpell(spellName, noEnchant=True)

# presses key for duration
def pressReleaseKey(key, duration):
    time.sleep(0.2)
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)

# afk run forwards and in direction, default direction is left
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
    
# setup for playing potion motion
def potionMotionSetup():

    # open friends list
    pressReleaseKey('f', 0.2)

    # tp to friend with this icon 
    moveToImage('TopFriendIcon', xOff=random.randint(50,175))
    mouse.click()
    time.sleep(0.5)

    clickImage('GoToLocationIcon')
    time.sleep(0.5)

    clickImage('YesButton')
    time.sleep(0.5)

    # move mouse out of the way
    moveToImage('QuickChatIcon')
    time.sleep(10)

    # enter potion motion
    pressX()
    time.sleep(1.5)

    clickImage('PotionMotionButton')
    time.sleep(10)

    clickImage('MinigamePlayButton')
    time.sleep(1.5)

# find tile given tile x and y
def getTileLocation(tileX, tileY):
    # tile (1,1) is upper left and tile (7,6) is lower right

    # upper left corner of upper left tile - 650 285
    # bottom right corner of lower right tile - 1270 815

    initialX = 650
    initialY = 285
    tileWidth = 88.571
    tileHeight = 88.333

    x = initialX + tileWidth * tileX - (tileWidth / 2)
    y = initialY + tileHeight * tileY - (tileHeight / 2)

    return x, y

# play potion motion by moving tiles
def playPotionMotion():

    time.sleep(1.5)

    print('Playing Potion Motion...')

    # verticle movement
    for x in range(1, 8):
        startX, startY = getTileLocation(x, 1)
        for y in range(1, 7):
            endX, endY = getTileLocation(x, y)
            mouse.drag(startX, startY, endX, endY, duration=0.05)
            time.sleep(0.05)

    # horizontal movement
    for y in range(1, 7):
        startX, startY = getTileLocation(1, y)
        for x in range(1, 8):
            endX, endY = getTileLocation(x, y)
            mouse.drag(startX, startY, endX, endY, duration=0.05)
            time.sleep(0.05)

# exit potion motion by clicking menu options
def exitPotionMotion():

    clickImage('MinigameXButton')
    time.sleep(1.5)

    clickImage('MinigameContinueButton')
    time.sleep(1.5)

    clickImage('MinigameXButton')
    time.sleep(10)

# use a potion if available
def usePotion():
    res, isPot = locateImage('FullPotionBottle')
    if isPot:
        clickImage('FullPotionBottle')
        printHealthManaInfo()
    else:
        print('Out of Potions!')
        #refillPotions()

# take mark, allow for area loading time
def takeMark():
    clickImage('TakeMarkButton')
    time.sleep(10)

def placeMark():
    clickImage('PlaceMarkButton')
    time.sleep(1)
    
def refillPotions():

    potionMotionSetup()

    totalBottles = 4

    for i in range(totalBottles):
        playPotionMotion()
        exitPotionMotion()

    takeMark()
    placeMark()
    afkRun()

# returns true if s is valid mana in wizard101
# must be in this format: int/int
def isValidHealthManaStr(s):
    
    # if s has '/', split on it
    if '/' in s:
        currentMana, maxMana = s.split('/')
        # return true if each side is int
        if (currentMana.isdigit() and maxMana.isdigit()):
            return True
    return False

# gets health info, assumes stat page is open (player push c)
def getHealthInfo():
    
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area.

    cap = ImageGrab.grab(bbox = (525, 400, 700, 430))

    img = nm.array(cap)

    # comment/uncomment to hide/show window
    #cv2.imshow("", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 
        lang ='eng',
        config='--psm 6')


    # removing specific chars to clean up output
    replaceChars = ' ,\n'
    tesstr = tesstr.translate({ord(i): None for i in replaceChars})

    # if valid string, get health values
    if isValidHealthManaStr(tesstr):
        
        currentHealth, maxHealth = [int(i) for i in tesstr.split('/')]
        percentHealth = (currentHealth / maxHealth) * 100
        return currentHealth, maxHealth, percentHealth
    else:
        return -1, -1, -1

# gets mana info, assumes stat page is open (player push c)
def getManaInfo():
    
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area.

    cap = ImageGrab.grab(bbox = (755, 400, 880, 430))

    img = nm.array(cap)

    # comment/uncomment to hide/show window
    #cv2.imshow("", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 
        lang ='eng',
        config='--psm 6')


    # removing specific chars to clean up output
    replaceChars = ' ,\n'
    tesstr = tesstr.translate({ord(i): None for i in replaceChars})

    # if valid string, get mana values
    if isValidHealthManaStr(tesstr):
        
        currentMana, maxMana = [int(i) for i in tesstr.split('/')]
        percentMana = (currentMana / maxMana) * 100
        return currentMana, maxMana, percentMana
    else:
        return -1, -1, -1

def printHealthManaInfo():

    # opening character stat page
    pressReleaseKey('c', getRandomDuration())
    time.sleep(1)
  
    # getting health and mana info
    currentHealth, maxHealth, percentHealth = getHealthInfo()
    currentMana, maxMana, percentMana = getManaInfo()

    # closing character stat page
    pressReleaseKey('c', getRandomDuration())

    # printing health info
    if currentHealth == -1: # error case
        print('ERROR: Health not visible')
    else:
        print(f'Current Health: {currentHealth}/{maxHealth} ({percentHealth:.2f}%)')
    
    # printing mana info
    if currentMana == -1: # error case
        print('ERROR: Mana not visible')
    else:
        print(f'Current Mana: {currentMana}/{maxMana} ({percentMana:.2f}%)')

    # using potion if needed
    # edit these numbers directly for now
    if (currentHealth < 2000 and currentHealth != -1):
        print('\nHealth too low! Using Potion!')
        usePotion()
    elif (currentMana < 10 and currentMana != -1):
        print('\nMana too low! Using Potion!')
        usePotion()

def pressX():
    pressReleaseKey('x', 0.2)
    print('Pressed X!')

# look for x icon and click x, but only on reagents, chests, and mounts
def lookForX():

    # if X icon is there at all
    if imageIsAvailable('PressXKey'):

        # press X on reagents
        if imageIsAvailable('PressXCollectReagent'):
            pressX()

        # press X on wooden chests only
        if imageIsAvailable('PressXCollectChest'):
            if not imageIsAvailable('SilverChest'):
                pressX()

        # press X on mounts
        if imageIsAvailable('PressXRideMount'):
            pressX()


# look for tp request and tp to that person
def lookForTpRequest():

    if imageIsAvailable('TeaCupEmoji'):

        if not imageIsAvailable('FriendIconDM'):
            pressReleaseKey('o', 0.2)

        moveToImage('FriendIconDM', xOff=50)
        mouse.click()
        time.sleep(1)

        clickImage('GoToLocationIcon')
        time.sleep(0.5)

        clickImage('YesButton')
        time.sleep(0.5)

        pressReleaseKey('o', 0.2)
        pressReleaseKey('f', 0.2)

        time.sleep(5)
