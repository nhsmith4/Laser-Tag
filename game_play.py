import tkinter as tk


import globe
import globe.view
from globe.view import BLACK, WHITE, RED, GREEN, BLUE
import globe.model
import globe.debug as debug
from globe.debug import printDebug


def create_frame(root):
    frame_height = globe.view.HEIGHT
    frame_width = globe.view.WIDTH // 9

    ## master frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # Left Area (Red Team)
    left_frame = tk.Frame(main_frame, bg="red")
    left_frame.grid(row=0, column=0, sticky="nsew")
    red_team_label = tk.Label(left_frame, text="Red Team", font=("Arial", 16), bg="red", fg="white")
    red_team_label.pack(pady=20)
    for id in range(20):
        player_frame = tk.Frame(left_frame, bg="red")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        player_label = tk.Label(player_frame, text="ligma", font=("Arial", 14), bg="red", fg="white", anchor="w")
        player_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
        score_label = tk.Label(player_frame, text=str(0), font=("Arial", 14), bg="red", fg="white", anchor="e")
        score_label.pack(side=tk.RIGHT)
    
    # Right Area (Green Team)
    right_frame = tk.Frame(main_frame, bg="green")
    right_frame.grid(row=0, column=2, sticky="nsew")
    green_team_label = tk.Label(right_frame, text="Green Team", font=("Arial", 16), bg="green", fg="white")
    green_team_label.pack(pady=20)
    for id in range(len(globe.model.green_team)):
        player_frame = tk.Frame(right_frame, bg="green")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        player_label = tk.Label(player_frame, text=globe.model.green_team[id], font=("Arial", 14), bg="green", fg="white", anchor="w")
        player_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
        score_label = tk.Label(player_frame, text=str(globe.model.green_team_scores[id]), font=("Arial", 14), bg="green", fg="white", anchor="e")
        score_label.pack(side=tk.RIGHT)

    # Middle Area (Message Area)
    middle_frame = tk.Frame(main_frame, bg="black")
    middle_frame.grid(row=0, column=1, sticky="nsew")
    message_label = tk.Label(middle_frame, text="Live Messages", font=("Arial", 16), bg="black", fg="white")
    message_label.pack(pady=20)
    for i in range(20-len(globe.model.message_board_team)):
        message_frame = tk.Frame(middle_frame, bg="black")
        message_frame.pack(fill=tk.X, padx=20, pady=2)
        message_label = tk.Label(message_frame, text=i, font=("Arial", 8), bg="black", fg="white", anchor="w")
        message_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
    for message in range(len(globe.model.message_board_team)):
        message_frame = tk.Frame(middle_frame, bg="black")
        message_frame.pack(fill=tk.X, padx=20, pady=2)
        message_label = tk.Label(message_frame, text=globe.model.message_board_team[message], font=("Arial", 8), bg="black", fg="white", anchor="w")
        message_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
    timer_frame = tk.Frame(middle_frame, bg="#111111")
    timer_frame.pack(fill=tk.X, padx=20, pady=10)
    tk.Label(timer_frame, text="Time Remaining:", font=("Arial", 16), bg="#111111", fg="white", anchor="w").pack(side=tk.LEFT, expand=True, fill=tk.X)
    tk.Label(timer_frame, text=globe.model.game_time_remaining, font=("Arial",16), bg="#111111", fg="white", anchor="w").pack(side=tk.LEFT, expand=True, fill=tk.X)

        
    return main_frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Play Screen")
    root.geometry(globe.view.RESOLUTION)
    frame = create_frame(root)
    frame.pack()
    root.mainloop()
