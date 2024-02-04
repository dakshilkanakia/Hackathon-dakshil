import pygame
import os
import random
import sys
import time

# Max window width
WIN_WIDTH = 1280

# Max window height
WIN_HEIGHT = 720

# Configure screen width and height
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Total distance traveled
TOTAL_DISTANCE = 0

# Required Distance
#REQ_DISTANCE = 100

#open variable.txt to access the value
file = open("variable.txt", "r")
temp = int(file.read())
file.close()

if temp == 1:
    REQ_DISTANCE = 1000
elif temp == 2:
    REQ_DISTANCE = 800
elif temp == 3:
    REQ_DISTANCE = 750
elif temp == 4:
    REQ_DISTANCE = 800
elif temp == 5:
    REQ_DISTANCE = 500
elif temp == 6:
    REQ_DISTANCE = 480
elif temp == 7:
    REQ_DISTANCE = 600
elif temp == 8:
    REQ_DISTANCE = 900


