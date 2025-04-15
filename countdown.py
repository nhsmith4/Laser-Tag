# Charles Williams
# Software Engineering Project - Countdown Screen

from tkinter import *
from tkinter import ttk
import time
import globe
from PIL import Image, ImageTk
import subprocess
import music
from globe.view import omni_dir, WIDTH, HEIGHT
import model
import game_play

from tkinter import *
from PIL import Image, ImageTk

gCountdown = None
background_image_tk = None
original_image = None

def create_countdown_screen(root):
    global gCountdown, background_image_tk, original_image
    
    gCountdown = IntVar(root, value="") 
    
    # Create the container frame
    countdown_frame = Frame(root)
    countdown_frame.pack(fill=BOTH, expand=YES)
    
    # Load original image
    original_image = Image.open(omni_dir("background.jpg"))
    
    # Create initial background image
    bg_width = root.winfo_width() or 800  # Default if not visible
    bg_height = root.winfo_height() or 600
    resized_image = original_image.resize((bg_width, bg_height), Image.Resampling.LANCZOS)
    background_image_tk = ImageTk.PhotoImage(resized_image)
    
    # Background label fills the frame
    background_label = Label(countdown_frame, image=background_image_tk)
    background_label.image = background_image_tk 
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Center countdown label 
    countdown_label = Label(countdown_frame, textvariable=gCountdown, font=("Arial", 100, "bold"), fg="yellow", bg="black")
    countdown_label.place(relx=0.5, rely=0.545, anchor=CENTER)
 
    def resize_background(event):
        try:
            # Only resize if we have valid dimensions
            if event.width > 1 and event.height > 1:
                resized_image = original_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
                new_image_tk = ImageTk.PhotoImage(resized_image)
                background_label.config(image=new_image_tk)
                background_label.image = new_image_tk  
        except Exception as e:
            print(f"Error resizing background: {e}")
    
    # Bind resize
    countdown_frame.bind("<Configure>", resize_background)
    
    return countdown_frame

def update_countdown(count, callback=None):
    global gCountdown
    if count > 0:
        gCountdown.set(str(count))
        root.after(1000, update_countdown, count - 1, callback)
    else:
        gCountdown.set("")
        if callback:
            callback()
        
        
if __name__ == '__main__':
    root = Tk()
    countdown = create_countdown_screen(root)
    
    # Run Tkinter main loop
    root.mainloop()
