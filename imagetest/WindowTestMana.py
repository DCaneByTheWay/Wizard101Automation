import numpy as nm  
import pytesseract
import cv2
import time
from PIL import ImageGrab
  

# returns true if s is valid mana in wizard101
# must be in this format: int/int
def isValid(s):
    
    # if s has '/', split on it
    if '/' in s:
        currentMana, maxMana = s.split('/')
        # return true if each side is int
        if (currentMana.isdigit() and maxMana.isdigit()):
            return True
    return False

  
  
def imToString():
  
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:
  
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
        if isValid(tesstr):
        
            currentMana, maxMana = [int(i) for i in tesstr.split('/')]

            percentMana = (currentMana / maxMana) * 100
            print()
            print('Current HP:', currentMana)
            print('Max HP:    ', maxMana)
            print(f'Percent HP: {percentMana:.2f}%')
        else:
            print('ERROR: Mana not visible')
            print(tesstr)


        time.sleep(3)
# Calling the function
imToString()