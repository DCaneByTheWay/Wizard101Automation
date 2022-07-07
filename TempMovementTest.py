from AutomationSetup import *

def moveAndUndo(key, duration):
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)

    if key == 'a':
        key = 'd'
    elif key == 'd':
        key = 'a'
    elif key == 'w':
        key = 's'
    elif key == 's':
        key = 'w'

    time.sleep(1.5)
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)

def move(key, duration):
    time.sleep(0.2)
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)
