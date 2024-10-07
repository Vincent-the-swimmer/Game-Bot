from pyautogui import *
import pyautogui
import time
import keyboard
import random
from win32 import win32api
import win32.lib.win32con as win32con
import pydirectinput

#Play Button X: 840 Y:  923
#Expert Button X: 1336 Y:  977 (click twice)
#Map Button X: 1256 Y:  371
#Easy Difficulty X:  630 Y:  414
#Deflation X: 1280 Y:  442
#Ok Button X:  954 Y:  743
#Check if game end, X:  950 Y:  900 RGB: (255, 255, 255)
#Home X:  702 Y:  839
#Level Up Idle: X:  859 Y:  186
#Hotkeys:
#SM = S, NJ = D, VL = K, SF = J, BH = I, EG = L, GL = Y
#Top Path = ","; Middle Path = "."; Bottom Path = "/"
#SM: X:  964 Y:  432 2-0-3
#VL: X:  892 Y:  312 0-0-2
#NJ: X:  869 Y:  437 4-0-2
#SF: X: 1523 Y:  567 0-0-3
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.5)

def keyClick(x, num):
    for i in range(num):
        time.sleep(0.01)
        pydirectinput.press(x)
        time.sleep(0.01)
        num+=1

while keyboard.is_pressed('5') == False:
    #Getting into Game
    time.sleep(5)
    click(840, 923)
    click(1336, 977)
    click(1336, 977)
    click(1256, 371)
    click(630, 414)
    click(1280, 442)
    time.sleep(3)
    click(954, 743)
    if keyboard.is_pressed('5') == True:
        break
    time.sleep(1)
    #Placing Village
    keyClick('k', 1)
    click(892, 312)
    click(892, 312)
    keyClick('/', 2)
    #Placing Super Monkey
    keyClick('s', 1)
    click(964, 432)
    click(964, 432)
    keyClick(',', 2)
    keyClick('/', 3)
    #Placing Ninja Monkey
    keyClick('d', 1)
    click(869, 437)
    click(869, 437)
    keyClick(',', 4)
    keyClick('/', 2)
    click(892, 312)
    keyClick('backspace', 1) #selling the village
    #Placing Spike Factory
    keyClick('j', 1)
    click(1523, 567)
    click(1523, 567)
    keyClick('/', 3)
    #Placing Monkeys to Farm XP
    keyClick('l', 1)
    click(920,665)
    keyClick('i', 1)
    click(830,963)
    keyClick('y', 1)
    click(825,660)
    keyClick('space', 2)
    #Idle Clicking for level up
    for i in range(345):
        if keyboard.is_pressed('5') == True:
            break                   
        click(859, 186)
        time.sleep(0.4)
    if keyboard.is_pressed('5') == True:
        break
    #Rewards Screen 
    click(950,900)
    click(702, 839)
