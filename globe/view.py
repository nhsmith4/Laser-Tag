from sys import platform
## cy - global window
win = None
win_frames = {}


## cy - settings variables
set_new_ip:str = None

## cy - GLOBAL CONSTANTS
TITLE:str = "Photon Laser Tag"
RESOLUTION:str = "1280x720"
WIDTH:int = 1280
HEIGHT:int = 720

## Colors
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "0000ff"

## Function that creates directory based upon OS
def omni_dir(img:str) -> str:
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return f"./media/{img}"
    else:
        return f".\media\{img}"