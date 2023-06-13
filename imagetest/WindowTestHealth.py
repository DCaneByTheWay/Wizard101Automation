# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
  
import pytesseract
import time
# importing OpenCV
import cv2
  
from PIL import ImageGrab

# returns true if s is valid health in wizard101
# must be in this format: int/int
def isValid(s):
    
    # if s has '/', split on it
    if '/' in s:
        currentHealth, maxHealth = s.split('/')
        # return true if each side is int
        if (currentHealth.isdigit() and maxHealth.isdigit()):
            return True
    return False

  
  
def imToString():
  
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    while(True):
  
        # ImageGrab-To capture the screen image in a loop. 
        # Bbox used to capture a specific area.

        cap = ImageGrab.grab(bbox = (525, 400, 700, 430))
        

        img = nm.array(cap)

        hImg,wImg,_ = img.shape
        boxes = pytesseract.image_to_boxes(img)

        #for b in boxes.splitlines():
        #    print(b)
            #b = b.split(' ')

        cv2.imshow("", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

        if cv2.waitKey(1) == 27:
            break

        
        # Converted the image to monochrome for it to be easily 
        # read by the OCR and obtained the output String.

        tesstr = pytesseract.image_to_string(
                cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 
                lang ='eng',
                config='--psm 6')


        tesstr = tesstr.replace('\n', '').replace(',', '').replace(' ', '')

        if isValid(tesstr):
        
            currentHealth, maxHealth = [int(i) for i in tesstr.split('/')]

            percentHealth = (currentHealth / maxHealth) * 100
            print()
            print('Current HP:', currentHealth)
            print('Max HP:    ', maxHealth)
            print(f'Percent HP: {percentHealth:.2f}%')
        else:
            print('ERROR: Heath not visible')
            print(tesstr)


        time.sleep(3)
# Calling the function
imToString()
cv2.destroyAllWindows()