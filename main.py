import sys
import tkinter

import view
import model
import controller

#import udp

import globe.essentials
import globe.debug as debug
from globe.debug import printDebug


if __name__ == "__main__":

    globe.essentials.gameState = globe.essentials.SPLASH
    view.start()
    controller.start()
    model.start(sys.argv[1:len(sys.argv)])
    

    printDebug("Debug Mode Activated")

    while(globe.essentials.gameState > 0):
        view.update()
        controller.update()
        model.update()
        