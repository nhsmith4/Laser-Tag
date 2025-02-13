import sys
import pygame
import tkinter

import view
import model
#import controller

#import udp

import globe.debug as debug
from globe.debug import printDebug


if __name__ == "__main__":
    try:
        if (sys.argv[1] == "debug"):
            debug.flag = 1
    except:
        None

    globe.essentials.gameState = globe.essentials.GAME_START
    model.start()
    view.start()

    while(globe.essentials.gameState > 0):
        None
