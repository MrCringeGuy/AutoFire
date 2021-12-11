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

print(pixel1, pixel2)

while True:
    if keyboard.is_pressed('t'):
        if pyautogui.pixel(pixel1, pixel2) != (111, 111, 111):
            mouse.position = (pixel1, pixel2)
            mouse.click(Button.left, 1)
            pixel2 = random.choice([530, 550, 535, 545])
            pixel1 = random.choice([950, 970, 955, 965])
            
        
