import globe
from globe.view import win

import model
import view

import globe.debug as debug
from globe.debug import printDebug, getDebug


settings_command:str = ""

def on_f5_click() -> None:
    globe.essentials.gameState=globe.essentials.COUNTDOWN
    if (getDebug(debug.CONTROLLER)):
        model.set_timer(3)
    else:
        model.set_timer(30)

## cy - sets up the keybinds for the view
def start() -> None:
    return

## cy - Uses updates to perform actions
def update() -> None:
    printDebug("Controller update", debug.CONTROLLER | debug.ADVANCED)
    global settings_command

    ## check for setting commands
    if settings_command == "ip change":
        model.set_ip()
    settings_command=""


## cy - Setting command to set ip address
def set_ip_change() -> None:
    global settings_command
    settings_command = "ip change"


def on_key_press(event) -> None:
    key = event.keysym
    printDebug("Key pressed: " + key, debug.CONTROLLER)

    if (key == "F11"):
        globe.view.win_fullscreen = ~globe.view.win_fullscreen
    if (key == "7"):
        player_entry.set_nick(7, "turtle")

    if (globe.essentials.gameState == globe.essentials.PLAYER_ENTRY):
        if (key == "F5"):
            on_f5_click()
            pass
        if (key == "F12"):
            model.clear_table()
    if (globe.essentials.gameState == globe.essentials.COUNTDOWN):
        if (getDebug(debug.CONTROLLER) and key == "F5"):
            on_f5_click(3)
            pass