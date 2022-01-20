from cgitb import text
from PIL import ImageGrab
import webbrowser
import pyautogui
import time
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
getRegion = (1275, 813, 1686, 888)
ageRegion = (832, 674, 1088, 742)
## regions = (X_Start , Y_Start, X_End, Y_End)

## Opens the epic games free games website
webbrowser.open('https://www.epicgames.com/store/en-US/free-games', new=1, autoraise=True)

## Sleeps for 10 seconds to let the webpage load
time.sleep(7)

## Only works if there is one game. Will click the first free game
pyautogui.moveTo(584, 767, duration=0.98, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()

## Sleeps for 10 seconds to let the webpage load
time.sleep(7)

## Check if there is an age verification process
ss_img = ImageGrab.grab(ageRegion)
ss_img.save("screenshot.jpg")
imgToRead = cv2.imread('screenshot.jpg')
textFromImage = pytesseract.image_to_string(imgToRead)
if textFromImage == "CONTINUE\n":
    pyautogui.moveTo(882, 696, duration=0.276, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

ss_img = ImageGrab.grab(getRegion)
ss_img.save("screenshot.jpg")
imgToRead = cv2.imread('screenshot.jpg')
textFromImage = pytesseract.image_to_string(imgToRead)

if textFromImage == "GET\n":
    ## Will click the GET button
    pyautogui.moveTo(1458, 838, duration=0.47, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    pyautogui.click() # Click the mouse at the x, y coordinates 1458, 838.

    ## Will click the PLACE ORDER button
    time.sleep(5)
    pyautogui.moveTo(1494, 1009, duration=0.73, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

    ## Will click the I AGREE button
    time.sleep(3)
    pyautogui.moveTo(1247, 826, duration=0.254, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

    ## This will delete screenshot.jpg
    time.sleep(7)
    os.remove("screenshot.jpg")


else:
    pyautogui.alert("I GOT " + textFromImage)
    exit()