import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed("7"):
        lastPosition = pyautogui.position()
        pyautogui.moveTo(1886, 748)
        keyboard.press_and_release("e")
        time.sleep(0.035)
        pyautogui.moveTo(lastPosition)
    if keyboard.is_pressed("8"):
        lastPosition = pyautogui.position()
        pyautogui.moveTo(1886, 748)
        keyboard.press_and_release("r")
        time.sleep(0.035)
        pyautogui.moveTo(lastPosition)    
