''' VERY SPECIFIC AUTOMATION, THIS ASSUMES A FEW THINGS
1) monitor is 1920x1080, all windows are 800x600
2) top left point of top left window is Point(x=267, y=0) (ish)
3) topr right point of top right window is in top right corner of screen
4) window order:

    [hitter(no hit code)]   [tc feint]
    [tc prism]              [item card feint]

5) code runs hitter into crystal and respawns boss
6) code also runs [tc prism] into the boss, starting the fight
'''

import time
import pyautogui
from pynput.keyboard import Controller
import keyboard
import mouse

myKeyboard = Controller()

# key that runs code
fullTrigger = '+'
clicksTrigger = '-'

# presses key for duration
def pressReleaseKey(key, duration):
    time.sleep(0.1)
    myKeyboard.press(key)
    time.sleep(duration)
    myKeyboard.release(key)
    time.sleep(0.1)

def doClicks(delay):
    time.sleep(delay)
    pyautogui.moveTo(x=1520, y=402, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=1541, y=325, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=1250, y=60, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=661, y=811, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=687, y=735, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=395, y=465, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=1538, y=752, duration=0.1)
    mouse.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=1244, y=480, duration=0.1)
    time.sleep(0.5)
    mouse.click()

while True:
    time.sleep(0.25)
    if keyboard.is_pressed(fullTrigger):
        time.sleep(0.5)

        # cassandra
        pyautogui.click(x=1536, y=182)
        pressReleaseKey('w', 0.1)
        pressReleaseKey('s', 0.1)

        # katherine
        pyautogui.click(x=1536, y=774)
        pressReleaseKey('w', 0.1)
        pressReleaseKey('s', 0.1)

        # brecken
        pyautogui.click(x=661, y=774)
        pressReleaseKey('d', 0.1)
        pressReleaseKey('w', 1)

        # mark
        pyautogui.click(x=661, y=182)
        pressReleaseKey('d', 0.65)
        pressReleaseKey('w', 0.8)
        time.sleep(4)
        pressReleaseKey('x', 0.2)
        time.sleep(1)
        pressReleaseKey('s', 1.5)

        doClicks(10)

    
    elif keyboard.is_pressed(clicksTrigger):
        doClicks(1)