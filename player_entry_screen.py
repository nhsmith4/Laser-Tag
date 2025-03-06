from tkinter import *
import tkinter as tk
#import model.py as model

root = tk.Tk()
root.state("zoomed")
root.title("Player Screen")

red_background = tk.Frame(root, bd=0, highlightthickness=0, background="red")
green_background = tk.Frame(root, bd=0, highlightthickness=0, background="green")
red_background.place(relx=0, rely=0, relwidth=0.5, relheight=1)
green_background.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

top_frame = tk.Frame(root, bg="black")
top_frame.pack(fill="x")

title_label = tk.Label(top_frame, text="Edit Current Game", fg="white", bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

main_frame = tk.Frame(root)
main_frame.pack(expand=True)

red_frame = tk.Frame(main_frame, bg="red")
red_frame.pack(side="left", expand=True, fill="both")

green_frame = tk.Frame(main_frame, bg="green")
green_frame.pack(side="left", expand=True, fill="both")

# Red side
red_ids = tk.Frame(red_frame)
red_ids.pack(side="left", expand=True, padx=10, pady=10)
red_nicks = tk.Frame(red_frame)
red_nicks.pack(side="left", expand=True, padx=10, pady=10)

label_red_ids = tk.Label(red_ids, text="RED IDS", fg="red", font=("Helvetica", 10, "bold"))
label_red_ids.pack(pady=10)
label_red_nicks = tk.Label(red_nicks, text="RED NICKNAMES", fg="red", font=("Helvetica", 10, "bold"))
label_red_nicks.pack(pady=10)

for i in range(20):
    tk.Label(red_ids, text=f"ID {i+1}", bg="gray30", fg="white", width=20).pack(pady=1)
    tk.Label(red_nicks, text=f"Nickname {i+1}", bg="gray30", fg="white", width=20).pack(pady=1)

# Green side
green_ids = tk.Frame(green_frame)
green_ids.pack(side="left", expand=True, padx=10, pady=10)
green_nicks = tk.Frame(green_frame)
green_nicks.pack(side="left", expand=True, padx=10, pady=10)

label_green_ids = tk.Label(green_ids, text="GREEN IDS", fg="green", font=("Helvetica", 10, "bold"))
label_green_ids.pack(pady=10)
label_green_nicks = tk.Label(green_nicks, text="GREEN NICKNAMES", fg="green", font=("Helvetica", 10, "bold"))
label_green_nicks.pack(pady=10)

for i in range(20):
    tk.Label(green_ids, text=f"ID {i+1}", bg="gray30", fg="white", width=20).pack(pady=1)
    tk.Label(green_nicks, text=f"Nickname {i+1}", bg="gray30", fg="white", width=20).pack(pady=1)

# Buttons at bottom of screen
bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack(fill="x")

game_mode_label = tk.Label(bottom_frame, text="Game Mode: Standard\npublic mode", fg="white", bg="black")
game_mode_label.pack(side="left", padx=10, pady=20)

fkeys_frame = tk.Frame(bottom_frame, bg="black")
fkeys_frame.pack(side="right")

# Edit Game
def on_f1_click():
    pass

# Game Parameters
def on_f2_click():
    pass

# Start Game
def on_f3_click():
    pass

# PreEntered Games
def on_f5_click():
    pass

# N/A
def on_f7_click():
    pass

# View Game
def on_f8_click():
    pass

# Flick Sync
def on_f10_click():
    pass

# Clear Game
def on_f12_click():
    pass

### Button calls
f1_button = tk.Button(fkeys_frame, text="F1\nEdit\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f1_click)
f2_button = tk.Button(fkeys_frame, text="F2\nGame\nParameters", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f2_click)
f3_button = tk.Button(fkeys_frame, text="F3\nStart\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f3_click)
f4_button = tk.Button(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f5_button = tk.Button(fkeys_frame, text="F5\nPreEntered\n Games", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f5_click)
f6_button = tk.Button(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f7_button = tk.Button(fkeys_frame, text="F7", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f7_click)
f8_button = tk.Button(fkeys_frame, text="F8\nView\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f8_click)
f9_button = tk.Button(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f10_button = tk.Button(fkeys_frame, text="F10\nFlick\nSync", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f10_click)
f11_button = tk.Button(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f12_button = tk.Button(fkeys_frame, text="F12\nClear\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised", command=on_f12_click)

f1_button.pack(side="left", padx=5)
f2_button.pack(side="left", padx=5)
f3_button.pack(side="left", padx=5)
f4_button.pack(side="left", padx=5)
f5_button.pack(side="left", padx=5)
f6_button.pack(side="left", padx=5)
f7_button.pack(side="left", padx=5)
f8_button.pack(side="left", padx=5)
f9_button.pack(side="left", padx=5)
f10_button.pack(side="left", padx=5)
f11_button.pack(side="left", padx=5)
f12_button.pack(side="left", padx=5)

'''f1_button.bind("<f1>", on_f1_click)
f2_button.bind("<f2>", on_f2_click)
f3_button.bind("<f3>", on_f3_click)
f5_button.bind("<f5>", on_f5_click)
f7_button.bind("<f7>", on_f7_click)
f8_button.bind("<f8>", on_f8_click)
f10_button.bind("<f10>", on_f10_click)
f12_button.bind("<f12>", on_f12_click)'''

root.mainloop()