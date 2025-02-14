import globe.view

import model

import globe.debug as debug
from globe.debug import printDebug

settings_command:str = ""

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