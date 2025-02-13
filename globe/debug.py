## cy - Debug Flags
DEBUG =         2 ** 0
VIEW =          2 ** 1
MODEL =         2 ** 2
CONTROLLER =    2 ** 3
UDP =           2 ** 4


## cy - Global Flag
flag:int = 0



## cy - Debug Print func : OR Flags together for multiple flag requirements
def printDebug(msg:str, opCode=0) -> None:
    if (getDebug(opCode)):
            print(msg)
    return

## cy - 
def getDebug(opCode:int = 0) -> bool:
    return flag == (DEBUG | opCode)