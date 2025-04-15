import tkinter as tk


import globe
import globe.view
import music
from globe.view import BLACK, WHITE, RED, GREEN, BLUE
import globe.model
import globe.debug as debug
from globe.debug import printDebug, getDebug

from tkinter import messagebox
import time
import globe.debug as debug
globe.model.red_team = None
import udp

# Game timer variables
game_duration = 60 * 6 # 6 minutes in seconds
game_start_time = None
gameplay_timer_running = False
current_screen_active = False
FLASH_INTERVAL = 500  # milliseconds between flashes
flash_state = False  
flash_active = True   # Should flashing continue

green_base_hit = False
red_base_hit = False

red_player_labels = []  
green_player_labels = []  

def create_frame(root):
    global game_start_time, timer_running, current_screen_active, game_duration, red_total_frame, green_total_frame
    
    if (getDebug(debug.CONTROLLER)):
        game_duration = 25 

    frame_height = globe.view.HEIGHT
    frame_width = globe.view.WIDTH // 9

    # Reset timer completely each time frame is created
    game_start_time = None
    gameplay_timer_running = False
    
    # Create the StringVar for the local timer
    if not hasattr(globe.model, 'gameplay_time_remaining'):
        globe.model.gameplay_time_remaining = tk.StringVar(root)
    globe.model.gameplay_time_remaining.set("6:00")
    
    # Create variables for team totals
    if not hasattr(globe.model, 'red_team_total'):
        globe.model.red_team_total = tk.IntVar(root)
        globe.model.red_team_total.set(0)
    if not hasattr(globe.model, 'green_team_total'):
        globe.model.green_team_total = tk.IntVar(root)
        globe.model.green_team_total.set(0)

    # master frame
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
    
    # Create a frame to hold all red player frames (for easy sorting)
    red_players_frame = tk.Frame(left_frame, bg="red")
    red_players_frame.pack(fill=tk.X)
    
    # Store player frames and data for sorting
    red_player_data = []
    for id in range(20):
        player_frame = tk.Frame(red_players_frame, bg="red")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        
        nickname = globe.model.red_nick[id].get()
        if (globe.model.red_base_hit[id]) & (red_base_hit == False):
            label_text = f"𝓑 {nickname}"
            red_base_hit = True
        else: nickname
        player_label = tk.Label(player_frame, text=label_text, font=("Arial", 14), bg="red", fg="white", anchor="w")
        player_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        score_label = tk.Label(player_frame, textvariable=globe.model.red_team_scores[id], font=("Arial", 14), bg="red", fg="white", anchor="e")
        score_label.pack(side=tk.RIGHT)
        
        red_player_labels.append(player_label)
        red_player_data.append({
            'frame': player_frame,
            'label': player_label,
            'score_var': globe.model.red_team_scores[id],
            'id': id
        })
    
    # Add Red Team Total section (store frame for flashing)
    red_total_frame = tk.Frame(left_frame, bg="red")
    red_total_frame.pack(fill=tk.X, padx=10, pady=10)
    tk.Label(red_total_frame, text="Total Score:", font=("Arial", 14, "bold"), bg="red", fg="white").pack(side=tk.LEFT)
    red_total_label = tk.Label(red_total_frame, textvariable=globe.model.red_team_total, font=("Arial", 14, "bold"), bg="red", fg="white")
    red_total_label.pack(side=tk.RIGHT)

    # Right Area (Green Team)
    right_frame = tk.Frame(main_frame, bg="green")
    right_frame.grid(row=0, column=2, sticky="nsew")
    green_team_label = tk.Label(right_frame, text="Green Team", font=("Arial", 16), bg="green", fg="white")
    green_team_label.pack(pady=20)
    
    # Create a frame to hold all green player frames (for easy sorting)
    green_players_frame = tk.Frame(right_frame, bg="green")
    green_players_frame.pack(fill=tk.X)
    
    # Store player frames and data for sorting
    green_player_data = []
    for id in range(20):
        player_frame = tk.Frame(green_players_frame, bg="green")
        player_frame.pack(fill=tk.X, padx=10, pady=2)
        
        nickname = globe.model.green_nick[id].get()
        if (globe.model.green_base_hit[id]) & (green_base_hit == False):
            label_text = f"𝓑 {nickname}"
            green_base_hit = True
        else: nickname
        player_label = tk.Label(player_frame, text=label_text, font=("Arial", 14), bg="green", fg="white", anchor="w")
        player_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        score_label = tk.Label(player_frame, textvariable=globe.model.green_team_scores[id], font=("Arial", 14), bg="green", fg="white", anchor="e")
        score_label.pack(side=tk.RIGHT)
        
        green_player_labels.append(player_label)
        green_player_data.append({
            'frame': player_frame,
            'label': player_label,
            'score_var': globe.model.green_team_scores[id],
            'id': id
        })
    
    # Add Green Team Total section (store frame for flashing)
    green_total_frame = tk.Frame(right_frame, bg="green")
    green_total_frame.pack(fill=tk.X, padx=10, pady=10)
    tk.Label(green_total_frame, text="Total Score:", font=("Arial", 14, "bold"), bg="green", fg="white").pack(side=tk.LEFT)
    green_total_label = tk.Label(green_total_frame, textvariable=globe.model.green_team_total, font=("Arial", 14, "bold"), bg="green", fg="white")
    green_total_label.pack(side=tk.RIGHT)

    # Use the sort python function
    def update_player_order():
        # Sort red team by descending score
        red_player_data.sort(key=lambda x: -x['score_var'].get())
        for i, player in enumerate(red_player_data):
            player['frame'].pack_forget()
            player['frame'].pack(fill=tk.X, padx=10, pady=2)
        
        # Sort green team 
        green_player_data.sort(key=lambda x: -x['score_var'].get())
        for i, player in enumerate(green_player_data):
            player['frame'].pack_forget()
            player['frame'].pack(fill=tk.X, padx=10, pady=2)
        
        # Schedule next update
        root.after(400, update_player_order)

    # Function to update totals and flashing
    def update_totals_and_flash():
        """Update team totals and manage flashing state"""
        global flash_active
        
        # Calculate totals
        red_total = sum(score.get() for score in globe.model.red_team_scores)
        green_total = sum(score.get() for score in globe.model.green_team_scores)
        
        globe.model.red_team_total.set(red_total)
        globe.model.green_team_total.set(green_total)
        
        # Determine which team is leading
        if red_total > green_total:
            # Stop any existing flashing
            flash_active = False
            # Reset both frames to their base colors
            reset_frame_colors(red_total_frame, "red")
            reset_frame_colors(green_total_frame, "green")
            # Start flashing for red team
            flash_active = True
            flash_frame(red_total_frame, "red")
        elif green_total > red_total:
            # Stop any existing flashing
            flash_active = False
            # Reset both frames to their base colors
            reset_frame_colors(red_total_frame, "red")
            reset_frame_colors(green_total_frame, "green")
            # Start flashing for green team
            flash_active = True
            flash_frame(green_total_frame, "green")
        else:
            # Scores are equal - stop flashing and reset colors
            flash_active = False
            reset_frame_colors(red_total_frame, "red")
            reset_frame_colors(green_total_frame, "green")
        
        # Schedule next total update
        root.after(1000, update_totals_and_flash)

    def reset_frame_colors(frame, color):
        """Reset frame to base colors"""
        frame.config(bg=color)
        for child in frame.winfo_children():
            child.config(bg=color)
    
    # Frames flash blue (gone but not forgotten)
    def flash_frame(frame, team_color):
        """Flash the total score section for the leading team"""
        global flash_state
        
        if not flash_active:
            return
        
        # Toggle the flash state
        flash_state = not flash_state
        
        # Set color based on flash state
        color = "blue" if flash_state else team_color
        frame.config(bg=color)
        for child in frame.winfo_children():
            child.config(bg=color)
    
        # Next flash
        root.after(FLASH_INTERVAL, lambda: flash_frame(frame, team_color))
    
    # Start the updates
    update_player_order()
    update_totals_and_flash()

    # Middle Area (Message Area)
    middle_frame = tk.Frame(main_frame, bg="black")
    middle_frame.grid(row=0, column=1, sticky="nsew")
    
    # Message display title
    tk.Label(middle_frame, text="Live Messages", font=("Arial", 16), bg="black", fg="white").pack(pady=10)
    
    # Create scrollable message area
    msg_container = tk.Frame(middle_frame, bg="black")
    msg_container.pack(fill=tk.BOTH, expand=True)
    
    # Create canvas and scrollbar
    canvas = tk.Canvas(msg_container, bg="black", highlightthickness=0)
    scrollbar = tk.Scrollbar(msg_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="black")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Add existing messages
    for message in globe.model.message_board_team:
        add_message(scrollable_frame, canvas, message) 
    
    # Add empty lines if needed
    for i in range(20 - len(globe.model.message_board_team)):
        add_message(scrollable_frame, canvas, "") 
    
     # Timer display
    timer_frame = tk.Frame(middle_frame, bg="#111111")
    timer_frame.pack(fill=tk.X, padx=20, pady=10)
    tk.Label(timer_frame, text="Time Remaining:", font=("Arial", 16), bg="#111111", fg="white", anchor="w").pack(side=tk.LEFT)
    time_label = tk.Label(timer_frame, textvariable=globe.model.gameplay_time_remaining, font=("Arial",16), bg="#111111", fg="white", anchor="e")
    time_label.pack(side=tk.RIGHT, expand=True, fill=tk.X)
    
    # Return to player entry button (initially disabled)
    return_button = tk.Button(middle_frame, text="Return to Player Entry", command=return_to_entry, state=tk.DISABLED)
    return_button.pack(pady=10)
    
    current_screen_active = True
    
    # Start the local timer
    start_gameplay_timer(time_label, scrollable_frame, canvas, return_button)

    # #testing cases for mark_base_hit function
    # mark_base_hit("red", 1,red_player_labels[1])
    # mark_base_hit("red", 2,red_player_labels[2])
    # mark_base_hit("green", 0,green_player_labels[0])
    # mark_base_hit("red", 4,red_player_labels[4])
    
    return main_frame, time_label, scrollable_frame, return_button, canvas
   
    
    
def add_message(message_frame, canvas, text):
    if not isinstance(canvas, tk.Canvas):
        print(f"Error: Expected Canvas widget, got {type(canvas)}")
        return None
    
    msg = tk.Label(message_frame, text=text, font=("Arial", 10), bg="black", fg="white", anchor="w", wraplength=300)
    msg.pack(fill=tk.X, padx=20, pady=2)
    
    try:
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)  # Scroll to bottom
    except AttributeError as e:
        print(f"Canvas scrolling error: {e}")
    
    return msg

def start_gameplay_timer(time_label, message_frame, canvas, return_button):
    global game_start_time, gameplay_timer_running
    
    # Reset timer completely
    game_start_time = time.time()
    gameplay_timer_running = True
    update_gameplay_timer(time_label, message_frame, canvas, return_button)

def update_gameplay_timer(time_label, message_frame, canvas, return_button):
    global gameplay_timer_running
    
    if not current_screen_active:
        gameplay_timer_running = False
        return
    
    current_time = time.time()
    elapsed = current_time - game_start_time
    remaining_time = max(0, game_duration - elapsed)
    
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    
    globe.model.gameplay_time_remaining.set(f"{minutes}:{seconds:02d}")
    
    if remaining_time <= 0:
        gameplay_timer_running = False
        add_message(message_frame, canvas, "GAME OVER!")
        for i in range(100):
            # transmit code 221 many times
            udp.udp_send(221)
            udp.udp_send(221)
            udp.udp_send(221)

        return_button.config(state=tk.NORMAL)
    else:
        time_label.after(1000, lambda: update_gameplay_timer(time_label, message_frame, canvas, return_button))

def cleanup_frame():
    """Call this when leaving the gameplay screen"""
    global gameplay_timer_running, current_screen_active
    current_screen_active = False
    gameplay_timer_running = False


    # # Should simulate adding game events but mid
    # if int(elapsed) % 5 == 0:  # (Add a message every 5 seconds for demo)
    #     add_message(message_frame, f"Game event at {int(elapsed)} seconds","")    

def return_to_entry():
    globe.essentials.gameState = globe.essentials.PLAYER_ENTRY
    
    cleanup_frame()
    music.stop_music()
    # Might need to reset all scores and messages too for reentry to this screen

def mark_base_hit(team: str, player_id: int, label: tk.Label):
    if team == 'red':
        globe.model.red_base_hit[player_id] = True
    elif team == 'green':
        globe.model.green_base_hit[player_id] = True
    else:
        return
