import random
import pyautogui
import time
import pynput
import keyboard

from pynput.mouse import *

mouse = Controller()
pixel2 = random.choice([540, 539, 541])
pixel1 = random.choice([960, 959, 961])

print(" ▄▄▄▄    ▒█████   ██▓ ███▄    █  ██ ▄█▀ ▄▄▄▄    ▒█████  ▄▄▄█████▓")
print("▓█████▄ ▒██▒  ██▒▓██▒ ██ ▀█   █  ██▄█▒ ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒")
print("▒██▒ ▄██▒██░  ██▒▒██▒▓██  ▀█ ██▒▓███▄░ ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░")
print("▒██░█▀  ▒██   ██░░██░▓██▒  ▐▌██▒▓██ █▄ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ ")
print("░▓█  ▀█▓░ ████▓▒░░██░▒██░   ▓██░▒██▒ █▄░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ")
print("░▒▓███▀▒░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ")
print("▒░▒   ░   ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░▒░▒   ░   ░ ▒ ▒░     ░    ")
print(" ░    ░ ░ ░ ░ ▒   ▒ ░   ░   ░ ░ ░ ░░ ░  ░    ░ ░ ░ ░ ▒    ░      ")
print(" ░          ░ ░   ░           ░ ░  ░    ░          ░ ░           ")
print("      ░                                      ░                   ")

time.sleep(0.5)

print("For isses, go to <ISSUE PAGE MADE LATER>")

time.sleep(0.5)

input("Press ENTER to start the trigger bot... ")

print("Trigger key = T")

print(pixel1, pixel2)       #Don't change the pixels, it's made to go around your crosshair instead of always seeing it.

while True:
    if keyboard.is_pressed('t'):        #Change the ('t') to any other letter e.g: ('r'). This will change the start key.
        if pyautogui.pixel(pixel1, pixel2) != (111, 111, 111):      #For anyone trying to use this, the (111,111,111) is basically jsut (r, g, b).
            mouse.click(Button.left, 1)
            pixel2 = random.choice([530, 550, 535, 545])
            pixel1 = random.choice([950, 970, 955, 965])
            
        
