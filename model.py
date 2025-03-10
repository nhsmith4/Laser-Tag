import time
import globe

import globe.debug as debug
import globe.model
from globe.debug import printDebug

timer = 80


## cy - Sets the IP address
def set_ip() -> None:
    printDebug(globe.view.set_new_ip.get())
    globe.essentials.ip_addr = globe.view.set_new_ip.get()

def set_timer(sec:int) -> None:
    global timer
    timer = sec
    globe.model.time = time.time()

def get_timer() -> int:
    global timer
    return timer


## cy - Sets up virtual world
def start(args:list=None) -> None:
    globe.model.time = time.time()
    for arg in args:
        if arg == "debug":
            debug.flag |= debug.DEBUG
            continue
        elif arg == "advanced":
            debug.flag |= debug.ADVANCED
            continue
        elif arg == "view":
            debug.flag |= debug.VIEW
            continue
        elif arg == "model":
            debug.flag |= debug.MODEL
            continue
        elif arg == "controller":
            debug.flag |= debug.CONTROLLER
            continue
        elif arg == "FULL":
            debug.flag |= debug.FULL
            continue
        elif arg == "cake":
            print("The cake is a lie.\n")
            continue
        else:
            continue

    time.sleep(3)
    globe.essentials.gameState = globe.essentials.PLAYER_ENTRY

def update() -> None:
    global timer
    cur_time = time.time()
    printDebug(str(cur_time - globe.model.time) + "| " + str(timer), globe.debug.MODEL)
    if (cur_time - globe.model.time >= 1):
        timer -= 1
        globe.model.time = cur_time

    if (globe.essentials.gameState == globe.essentials.COUNTDOWN):
        if (timer <= 0):
            globe.essentials.gameState = globe.essentials.GAME_PLAY