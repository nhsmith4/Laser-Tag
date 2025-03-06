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

### Button calls
f1_label = tk.Label(fkeys_frame, text="F1\nEdit\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f2_label = tk.Label(fkeys_frame, text="F2\nGame\nParameters", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f3_label = tk.Label(fkeys_frame, text="F3\nStart\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f4_label = tk.Label(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f5_label = tk.Label(fkeys_frame, text="F5\nPreEntered\n Games", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f6_label = tk.Label(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f7_label = tk.Label(fkeys_frame, text="F7", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f8_label = tk.Label(fkeys_frame, text="F8\nView\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f9_label = tk.Label(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f10_label = tk.Label(fkeys_frame, text="F10\nFlick\nSync", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")
f11_label = tk.Label(fkeys_frame, text="", fg="white", bg="black", height=4, width=9, borderwidth=5)
f12_label = tk.Label(fkeys_frame, text="F12\nClear\nGame", fg="white", bg="black", height=4, width=9, borderwidth=5, relief="raised")

f1_label.pack(side="left", padx=5)
f2_label.pack(side="left", padx=5)
f3_label.pack(side="left", padx=5)
f4_label.pack(side="left", padx=5)
f5_label.pack(side="left", padx=5)
f6_label.pack(side="left", padx=5)
f7_label.pack(side="left", padx=5)
f8_label.pack(side="left", padx=5)
f9_label.pack(side="left", padx=5)
f10_label.pack(side="left", padx=5)
f11_label.pack(side="left", padx=5)
f12_label.pack(side="left", padx=5)

# Edit Game
def on_f1_click(event):
    pass

# Game Parameters
def on_f2_click(event):
    pass

# Start Game
def on_f3_click(event):
    pass

# PreEntered Games
def on_f5_click(event):
    pass

# N/A
def on_f7_click(event):
    pass

# View Game
def on_f8_click(event):
    pass

# Flick Sync
def on_f10_click(event):
    pass

# Clear Game
def on_f12_click(event):
    pass

f1_label.bind(on_f1_click)
f2_label.bind(on_f2_click)
f3_label.bind(on_f3_click)
f5_label.bind(on_f5_click)
f7_label.bind(on_f7_click)
f8_label.bind(on_f8_click)
f10_label.bind(on_f10_click)
f12_label.bind(on_f12_click)

root.mainloop()