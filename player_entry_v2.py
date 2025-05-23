import tkinter as tk

import globe
import databaseConn
import globe.view
from globe.view import BLACK, WHITE, RED, GREEN, BLUE
import globe.model
import globe.debug as debug
from globe.debug import printDebug
import controller
import model

def create_header(root, color):
    header_frame = tk.Frame(root, bg=color)
    header_frame.pack(fill=tk.X, padx=10, pady=2)
    hardware_label = tk.Label(header_frame, text="Hardware ID", font=("Arial", 14), width=2, bg=color, fg="white", anchor="w")
    hardware_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
    id_label = tk.Label(header_frame, text="Player ID", font=("Arial", 14), width=2, bg=color, fg="white", anchor="w")
    id_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
    nick_label = tk.Label(header_frame, text="Player Nickname", font=("Arial", 14), bg=color, fg="white", anchor="w")
    nick_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

def submit_player(entry_id, entry_nickname):
    player_id = entry_id.get()
    player_nickname = entry_nickname.get()

    if player_id:
        existing_name = entry_nickname.get()
        if databaseConn.player_exists(player_id): 
            entry_nickname.set(databaseConn.player_exists(player_id))
        elif player_id and player_nickname:     
            databaseConn.insert_player(player_id, player_nickname)
        else:
            printDebug("Player ID and nickname required")
    else:
        printDebug("Player id")



def create_frame(root):
    ## master frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    validation = root.register(globe.view.is_digit)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)

    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=3)

    # Left Area (Red Team)
    left_frame = tk.Frame(main_frame, bg="red")
    left_frame.grid(row=0, column=0, sticky="nsew")
    red_team_label = tk.Label(left_frame, text="Red Team", font=("Arial", 16), bg="red", fg="white")
    red_team_label.pack(pady=20)
    create_header(left_frame, "red")
    for id in range(15):
        player_frame = tk.Frame(left_frame, bg="red")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        player_hardware = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", validate='key', validatecommand=(validation, '%S'), width=2, relief=tk.SUNKEN, textvariable=globe.model.red_hardware[id])
        player_hardware.pack(side=tk.LEFT, expand=True, fill=tk.X)
        player_id = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", validate='key', validatecommand=(validation, '%S'), width=2, relief=tk.SUNKEN, textvariable=globe.model.red_id[id])
        player_id.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
        player_nickname = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", relief=tk.SUNKEN, textvariable=globe.model.red_nick[id])
        player_nickname.pack(side=tk.LEFT, expand=True, fill=tk.X)
        submit_button = tk.Button(player_frame, text="submit", font=("Arial", 10), command=model.set_players)
        submit_button.pack(side=tk.LEFT, padx=5)

    # Right Area (Green Team)
    right_frame = tk.Frame(main_frame, bg="green")
    right_frame.grid(row=0, column=1, sticky="nsew")
    green_team_label = tk.Label(right_frame, text="Green Team", font=("Arial", 16), bg="green", fg="white")
    green_team_label.pack(pady=20)
    create_header(right_frame, "green")
    for id in range(15):
        player_frame = tk.Frame(right_frame, bg="green")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        player_hardware = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", validate='key', validatecommand=(validation, '%S'), width=2, relief=tk.SUNKEN, textvariable=globe.model.green_hardware[id])
        player_hardware.pack(side=tk.LEFT, expand=True, fill=tk.X)
        player_id = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", validate='key', validatecommand=(validation, '%S'), width=2, relief=tk.SUNKEN, textvariable=globe.model.green_id[id])
        player_id.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
        player_nickname = tk.Entry(player_frame, font=("Arial", 12), bg="white", fg="black", relief=tk.SUNKEN, textvariable=globe.model.green_nick[id])
        player_nickname.pack(side=tk.LEFT, expand=True, fill=tk.X)
        submit_button = tk.Button(player_frame, text="submit", font=("Arial", 10), command=model.set_players)
        submit_button.pack(side=tk.LEFT, padx=5)

    ## Button Frame (Bottom Frame)
    bottom_frame = tk.Frame(main_frame, bg="black")
    bottom_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
    f5_butt = tk.Button(bottom_frame, fg="white", bg="black", height=20, width=11, borderwidth=5, relief="raised", font=("Arial", 12), text="<f5>\nStart\nGame", command=controller.on_f5_click).pack(side=tk.LEFT, padx=1)
    f12_butt = tk.Button(bottom_frame, fg="white", bg="black", height=20, width=11, borderwidth=5, relief="raised", font=("Arial", 12), text="<f12>\nClear\nTeams", command=controller.on_f12_click).pack(side=tk.LEFT, padx=1)

    return main_frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Play Screen")
    root.geometry(globe.view.RESOLUTION)
    frame = create_frame(root)
    root.attributes("-fullscreen", True) 
    frame.pack()
    root.mainloop()
