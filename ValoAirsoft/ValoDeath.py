# OCR Screen Scanner
# By Dornu Inene
# Libraries that you show have all installed
import cv2
import numpy as np
from pyautogui import Size
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# We only need the ImageGrab class from PIL
from PIL import ImageGrab, ImageOps
import serial
import re

bluetooth = serial.Serial('COM12', 11520) #replace with your com port
bluetooth.flushInput()

#Set last and current health to 100 before starting the loop
lastHealth = 100
currHealth = 100

#array for the points for the image
#topLeft(x1,y1), bottomRight(x2,y2) [x1, y1, x2, y2]
point = [570, 985, 655, 1075]
width = point[2] - point[0]
height = point[3] - point[1]

def writeBluetooth(val):
    bluetooth.write(val)


# Run forever unless you press Esc
while True:
    # This instance will generate an image from
    # the point of (570, 985) and (655, 1080) in format of (x, y), 85x95 WxH
    cap = ImageGrab.grab(bbox=(point))
    cap = ImageOps.grayscale(cap) #grayscale the image
    
    # For us to use cv2.imshow we need to convert the image into a numpy array
    cap_arr = np.array(cap)
    cap = cv2.resize(cap_arr, (int(width*.5), int(height*.5))) #resize the image
    # This isn't really needed for getting the text from a window but
    # It will show the image that it is reading it from

    # cv2.imshow() shows a window display and it is using the image that we got
    # use array as input to image
    cv2.imshow("", cap_arr) #SHOW THE IMAGE || THIS IS NOT 'TECHINCALLY' WHAT THE COMPUTER READS TEXT FROM (2x scale)

    # Read the image that was grabbed from ImageGrab.grab using    pytesseract.image_to_string
    # This is the main thing that will collect the text information from that specific area of the window
    #--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789
    text = pytesseract.image_to_string(cap)
    # This just removes spaces from the beginning and ends of text
    # and makes the the it reads more clean
    text = text.strip()

    if(len(text) == 0): #If text is empty attempt to read it using psm 10 which looks for single characters
        singleText = pytesseract.image_to_string(cap, config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789")
        singleText = text.strip()
        if(len(singleText) > 0 and singleText.isdigit()):
            if(int(singleText) < 10):
                text = singleText

    hitDetected = "0"

    # If any text was translated from the image, and the text is a number, print it
    if (len(text) > 0 and text.isdigit()):
        print(text)
        currHealth = int(text)
        if(currHealth < lastHealth): #If the current health is less than the last health player was shot
            print('you suck shit bag')
            hitDetected = "hit\n"
            writeBluetooth(str.encode(str(hitDetected)))
        lastHealth = currHealth

        

    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()
bluetooth.close()