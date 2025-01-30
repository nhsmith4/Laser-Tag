## cy - Debug Flags
DEBUG = 1
VIEW = 2
MODEL = 4
CONTROLLER = 8


## cy - Global Flag
flag = 0



## cy - Debug Print func : OR Flags together for multiple flag requirements
def printDebug(msg:str, opCode=0):
    if (flag == DEBUG | opCode):
            print(msg)