import psutil
import os
from os import walk
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
key = "f5"
#Finding out what file
FileType = ""
FileName = ''
for file in [f for f in os.listdir('.') if os.path.isfile(f)]:
    if '.tex' in file:
        FileType = 'Latex'
        FileName = file
        break
    elif '.py' in file and file != 'run.py':
        FileType = 'Python'
        FileName = file
        break
        

if FileType == 'Latex':
    os.system('cmd /c "pdflatex "'+FileName)
    if not ("chrome.exe" in (i.name() for i in psutil.process_iter())):
        os.startfile(FileName)
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
