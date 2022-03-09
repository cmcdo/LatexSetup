import psutil
import os
from os import walk
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
key = "f5"
if not ("chrome.exe" in (i.name() for i in psutil.process_iter())):
    for file in [f for f in os.listdir('.') if os.path.isfile(f)]:
        if ".pdf" in file:
            os.startfile(file)
            time.sleep(0.1)
            os.startfile("refresh.vbs")
else:
    os.startfile("refresh.vbs")
    time.sleep(0.1)
    
    keyboard.press(Key.ctrl)
    keyboard.press("1")
    
    keyboard.release(Key.ctrl)
    keyboard.release("1")

    time.sleep(0.1)
    keyboard.press(Key.f5)

    keyboard.release(Key.f5)
    time.sleep(0.1)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
