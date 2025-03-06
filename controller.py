from globe.view import win

import model

import globe.debug as debug
from globe.debug import printDebug

settings_command:str = ""


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

    
    if event.keysym == "F1":
        print("F1 pressed")
    elif event == "k":
        print("asfkjfjhdfsfkjfjhd")