import sys
#import pygame

#import view
#import model
#import controller

import globe.debug as debug
from globe.debug import printDebug

try:
    if (sys.argv[1] == "debug"):
        debug.flag = 1
except:
    None

printDebug("Secret Message")

while(input(">>" != "0")):
    print("hi")