from infi.systray import SysTrayIcon
from threading import Event
import pyautogui
import keyboard
import time
import sys
import os

quit_event = Event()
script_name = sys.argv[0]
running = True

def qcallback(systray):
    global running
    running = False
    quit_event.set()
    os.system(f'taskkill /f /im {script_name}')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)            

def pressKey(key):
    lastPosition = pyautogui.position()
    pyautogui.moveTo(1886, 748)
    keyboard.press_and_release(key)
    time.sleep(0.035)
    pyautogui.moveTo(lastPosition)


path = resource_path("icon.ico")    
systray = SysTrayIcon(path, "Lulu Client", on_quit=qcallback)
systray.start()  

while running:
    if keyboard.is_pressed("7"):
        pressKey("e")
    if keyboard.is_pressed("8"):
        pressKey("r")   
