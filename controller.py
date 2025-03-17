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

def on_f12_click() -> None:
    model.clear_players()
        

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

    if (key == "TAB"):
        model.set_players()

    if (key == "F11"):
        globe.view.win_fullscreen = ~globe.view.win_fullscreen

    if (globe.essentials.gameState == globe.essentials.PLAYER_ENTRY):
        if (key == "F5"):
            on_f5_click()
            pass

    if (globe.essentials.gameState == globe.essentials.COUNTDOWN):
        if (getDebug(debug.CONTROLLER) and key == "F5"):
            on_f5_click(3)
            pass
    if (key == "F7"):
        i = 7
        globe.model.red_nick[0].set("charles")
        globe.model.red_nick[1].set("Joseph")
        globe.model.red_nick[2].set("Caleb")
        globe.model.red_nick[3].set("Nick")
        globe.model.red_nick[i].set("germany")
        globe.model.green_nick[0].set("selrach")
        globe.model.green_nick[1].set("hpesoj")
        globe.model.green_nick[2].set("balec")
        globe.model.green_nick[3].set("kcin")
        
    if (key == "F12"):
        model.clear_players()
        pass