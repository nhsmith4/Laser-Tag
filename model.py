import globe

import globe.debug as debug
from globe.debug import printDebug


## cy - Sets the IP address
def set_ip() -> None:
    printDebug(globe.view.set_new_ip.get())
    globe.essentials.ip_addr = globe.view.set_new_ip.get()

## cy - Sets up virtual world
def start(args:list=None) -> None:
    for arg in args:
        if arg == "debug":
            debug.flag = debug.flag | debug.DEBUG
            continue
        elif arg == "advanced":
            debug.flag = debug.flag | debug.ADVANCED
            continue
        elif arg == "view":
            debug.flag = debug.flag | debug.VIEW
            continue
        elif arg == "model":
            debug.flag = debug.flag | debug.MODEL
            continue
        elif arg == "controller":
            debug.flag = debug.flag | debug.CONTROLLER
            continue
        elif arg == "FULL":
            debug.flag = debug.flag | debug.FULL
            continue
        else:
            print("Unknown argument \"{}\". Please consult documentation.".format(arg))
        
