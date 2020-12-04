import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = 2
while(True):
    x=0
    while(x<numMin):
        time.sleep(30)
        pyautogui.click()
        print("Vaya trabajo... I last clicked at {}".format(datetime.now().time()))