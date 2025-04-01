import time
import globe
import tkinter
import tkinter.messagebox

import globe.debug as debug
import globe.model
from globe.debug import printDebug

import udp
import databaseConn

timer = 80

global red_hardware
global red_id
global red_nick


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

def set_players():
    id_base = {}

    for i in range(20):
        ## red team
        player_id = globe.model.red_id[i].get()

        ## check if player is already used
        if id_base.get(player_id) is not None:
            tkinter.messagebox.showwarning("Duplicate User", f"ID {player_id} has already been inserted!!!")
            clear_red(i)
        else:
            id_base[player_id] = 'r'
            player_nick = globe.model.red_nick[i].get()
            inDatabase = databaseConn.player_exists(player_id)
            if inDatabase:
                globe.model.red_nick[i].set(inDatabase)
            elif player_id and player_nick:
                databaseConn.insert_player(player_id, player_nick)
            else:
                printDebug("Player ID and nickname required!!!")
                tkinter.messagebox.showwarning("ERROR","Player ID and nickname required!!!")

            udp.udp_send(globe.model.red_hardware[i])
        player_id = globe.model.green_id[i].get()
        if id_base.get(player_id) is not None:
            tkinter.messagebox.showwarning("Duplicate User", f"ID {player_id} has already been inserted!!!")
            clear_green(i)
        else:
            player_nick = globe.model.green_nick[i].get()
            inDatabase = databaseConn.player_exists(player_id)
            if inDatabase:
                globe.model.green_nick[i].set(inDatabase)
            elif player_id and player_nick:
                databaseConn.insert_player(player_id, player_nick)
            else:
                printDebug("Player ID and nickname required!!!")
                tkinter.messagebox.showwarning("ERROR","Player ID and nickname required!!!")
            udp.udp_send(globe.model.green_hardware[i])

        

    '''
    for i in range(20):
        player_id = globe.model.red_id[i].get()
        if player_id in id_base:
            clear_player(i)
            continue
        id_base[player_id] = True
        player_nick = globe.model.red_nick[i].get()
        inDatabase = databaseConn.player_exists(player_id)
        if inDatabase:
            globe.model.red_nick[i].set(inDatabase)
        elif player_id and player_nick:
            databaseConn.insert_player(player_id, player_nick)
        else:
            printDebug("Player ID and nickname required!!!")
            tkinter.messagebox.showwarning("ERROR","Player ID and nickname required!!!")
        udp.udp_send(globe.model.red_hardware[i])
        player_id = globe.model.green_id[i].get()
        player_nick = globe.model.green_nick[i].get()
        inDatabase = databaseConn.player_exists(player_id)
        if inDatabase:
            globe.model.green_nick[i].set(inDatabase)
        elif player_id and player_nick:
            databaseConn.insert_player(player_id, player_nick)
        else:
            printDebug("Player ID and nickname required!!!")
            tkinter.messagebox.showwarning("ERROR","Player ID and nickname required!!!")
        udp.udp_send(globe.model.green_hardware[i])'''


def clear_red(id) -> None:
    globe.model.red_hardware[id].set('')
    globe.model.red_id[id].set('')
    globe.model.red_nick[id].set("")

def clear_green(id) -> None:
    globe.model.green_hardware[id].set('')
    globe.model.green_id[id].set('')
    globe.model.green_nick[id].set("")

def clear_players():
    printDebug("Clearing Players")
    for i in range(20):
            clear_red(id)
            clear_green(id)
    printDebug("Cleared Players")


## cy - Sets up virtual world
def start(args:list=None) -> None:
    globe.model.time = time.time()
    udp.establish_client()
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
        elif arg == "udp":
            debug.flag |= debug.UDP
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
            udp.udp_send(202)
    globe.model.timer = timer
    if (globe.model.red_team_scores[0].get()):
        globe.model.red_team_scores[0].set(globe.model.red_team_scores[0].get() + 1)
    else:
        globe.model.red_team_scores[0].set(1)
    