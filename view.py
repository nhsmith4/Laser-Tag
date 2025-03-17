import tkinter

import globe.essentials
import globe.view
from globe.view import win
import globe.model

import controller

import globe.debug as debug
from globe.debug import printDebug

import splash
import player_entry_v2
import countdown
import game_play

global red_team

g_local_state = None


## cy - Settings Menu
def add_settings(window):
    menu = tkinter.Menu(window)
    window.config(menu=menu)
    filemenu = tkinter.Menu(menu)
    menu.add_cascade(label='Settings', menu=filemenu)
    filemenu.add_command(label='Change IP Address', command=change_ip_window)


## cy - change ip window
def change_ip_window():
    globe.view.set_new_ip = tkinter.StringVar()

    window = tkinter.Toplevel()
    window.title("Change IP Address")
    tkinter.Label(window, text="Current IP Address: " + globe.essentials.ip_addr).grid(row=0, column=0)
    tkinter.Label(window, text="Enter New IP").grid(row=1)
    new_ip = tkinter.Entry(window, textvariable=globe.view.set_new_ip)
    new_ip.grid(row=1, column=1)
    chck_ip = tkinter.Button(window, text="Check Compatability", width=25, command=controller.set_ip_change)
    chck_ip.grid(row=1, column=2)

## cy - View start module / Establish main window
def start() -> None:
    global win
    win = tkinter.Tk()
    win.title(globe.view.TITLE)
    win.geometry(globe.view.RESOLUTION)

    add_settings(win)

    globe.model.red_hardware = [tkinter.StringVar(win) for i in range(20)]
    globe.model.red_id = [tkinter.StringVar(win) for i in range(20)]
    globe.model.red_nick = [tkinter.StringVar(win) for i in range(20)]
    globe.model.red_team_scores = [tkinter.IntVar(win) for i in range(20)]
    globe.model.green_nick = [tkinter.StringVar(win) for i in range(20)]
    globe.model.green_team_scores = [tkinter.IntVar(win) for i in range(20)]

    globe.view.win_frames[globe.essentials.SPLASH] = splash.create_splash_screen(win)
    globe.view.win_frames[globe.essentials.PLAYER_ENTRY] = player_entry_v2.create_frame(win)
    globe.view.win_frames[globe.essentials.COUNTDOWN] = countdown.create_countdown_screen(win)
    globe.view.win_frames[globe.essentials.GAME_PLAY] = game_play.create_frame(win)

    


        


    win.bind_all("<Key>", controller.on_key_press)
    win.bind("WM_DELETE_WINDOW", win.destroy)

    win.update()

    




## cy - View update command / updates windows
def update() -> None:
    global g_local_state
    printDebug("View update", debug.VIEW | debug.ADVANCED)
    
    try:
        if(g_local_state != globe.essentials.gameState):
            for frame in globe.view.win_frames:
                globe.view.win_frames[frame].pack_forget()
            g_local_state = globe.essentials.gameState
            globe.view.win_frames[g_local_state].pack(fill=tkinter.BOTH, expand=True)
        
        ##win.update_idletasks()
        countdown.gCountdown.set(globe.model.timer)
        win.attributes("-fullscreen", globe.view.win_fullscreen)
        win.update()
    except Exception as e:
        print(e)
        globe.essentials.gameState = -1
