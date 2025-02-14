## cy - Debug Flags
DEBUG =         2 ** 0
ADVANCED =      2 ** 1
VIEW =          2 ** 2
MODEL =         2 ** 3
CONTROLLER =    2 ** 4
UDP =           2 ** 5
FULL = -1


## cy - Global Flag
flag:int = 0



## cy - Debug Print func : OR Flags together for multiple flag requirements
def printDebug(msg:str, opCode=0) -> None:
    if (getDebug(opCode)):
            print(msg)
    return

## cy - 
def getDebug(opCode:int = 0) -> bool:
    return bool((flag & (DEBUG | opCode)) == (DEBUG | opCode))