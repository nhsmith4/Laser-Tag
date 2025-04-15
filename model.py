import time
import globe
import tkinter
import music
import game_play
import asyncio

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

def send_hardware(id:int) -> None:
    if not globe.model.hardware_used[id]:
        printDebug("sending ID")
        udp.udp_send(id)
        globe.model.hardware_used[id] = True

def set_players():
    id_base = {}
    for i in range(20):
        ## red team
        player_id:int = globe.model.red_id[i].get()
        try:
            player_id = int(player_id)
        except:
            continue
        if player_id in id_base.keys():
            clear_red(i)
            tkinter.messagebox.showwarning("Duplicate entry",f"ID {player_id} is already used!!!")
            continue
        id_base[player_id] = 'r'
        inDatabase:str = databaseConn.player_exists(player_id)
        if inDatabase:
            globe.model.red_nick[i].set(inDatabase)
        else:
            player_nick:str = globe.model.red_nick[i].get()
            if player_nick.replace(" ", "") != "":
                databaseConn.insert_player(player_id, player_nick)
            else:
                tkinter.messagebox.showwarning("Insufficient Data", f"ID {player_id} requires a nickname!!!")
        udp.udp_send(globe.model.red_hardware[i].get())
        
    

    for i in range(20):
        ## green team
        player_id:int = globe.model.green_id[i].get()
        try:
            player_id = int(player_id)
        except:
            continue
        if player_id in id_base.keys():
            clear_green(i)
            tkinter.messagebox.showwarning("Duplicate entry",f"ID {player_id} is already used!!!")
            continue
        id_base[player_id] = 'g'
        inDatabase:str = databaseConn.player_exists(player_id)
        if inDatabase:
            globe.model.green_nick[i].set(inDatabase)
        else:
            player_nick:str = globe.model.green_nick[i].get()
            if player_nick.replace(" ", "") != "":
                databaseConn.insert_player(player_id, player_nick)
            else:
                tkinter.messagebox.showwarning("Insufficient Data", f"ID {player_id} requires a nickname!!!")
        udp.udp_send(globe.model.green_hardware[i].get())


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
            clear_red(i)
            clear_green(i)
    printDebug("Cleared Players")


## cy - Sets up virtual world
def start(args:list=None) -> None:
    globe.model.time = time.time()
    udp.establish_client()
    globe.model.hardware_used = {}
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
        # Sync track with timer
        if (timer == 15):
            music.play_random_music()
        if (timer <= 0):
            globe.essentials.gameState = globe.essentials.GAME_PLAY
            udp.udp_send(202)
        globe.model.timer = timer
        return

    if(globe.essentials.gameState == globe.essentials.GAME_PLAY):
        ## udp_receive
        udp_str = udp.udp_receive()
        if udp_str != "":
            udp_str = udp_str.split(":")
            ##printDebug(udp_str)
            tagger = udp_str[0]
            target = udp_str[1]
            udp.udp_send(target)

            red_hard = [i.get() for i in globe.model.red_hardware]
            green_hard = [j.get() for j in globe.model.green_hardware]
            printDebug(red_hard, debug.MODEL)
            printDebug(green_hard, debug.MODEL)

            ## Opposing Team
            if (tagger in red_hard and target in green_hard) or (tagger in green_hard and target in red_hard):
                if tagger in red_hard:
                    globe.model.red_team_scores[red_hard.index(tagger)].set(globe.model.red_team_scores[red_hard.index(tagger)].get()+10)
                if tagger in green_hard:
                    globe.model.green_team_scores[green_hard.index(tagger)].set(globe.model.green_team_scores[green_hard.index(tagger)].get()+10)

            ## Same Team
            if (tagger in red_hard and target in red_hard) or (tagger in green_hard and target in green_hard):
                if tagger in red_hard:
                    globe.model.red_team_scores[red_hard.index(tagger)].set(globe.model.red_team_scores[red_hard.index(tagger)].get()-10)
                if tagger in green_hard:
                    globe.model.green_team_scores[green_hard.index(tagger)].set(globe.model.green_team_scores[green_hard.index(tagger)].get()-10)

            ## Red Base
            if (target == '53'):
                if tagger in green_hard and (True not in globe.model.red_base_hit):
                    globe.model.green_team_scores[green_hard.index(tagger)].set(globe.model.green_team_scores[green_hard.index(tagger)].get()+100)
                    game_play.mark_base_hit('g', green_hard.index(tagger))
                else:
                    return
            ## Green Base
            if (target == '43'):
                if tagger in red_hard and (True not in globe.model.green_base_hit):
                    globe.model.red_team_scores[red_hard.index(tagger)].set(globe.model.red_team_scores[red_hard.index(tagger)].get()+100)
                    game_play.mark_base_hit('r', red_hard.index(tagger))
                else:
                    return


        return
