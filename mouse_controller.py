import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(20)
    for i in range(10,50):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 2):
        pyautogui.press('down')
