# Charles Williams
# Software Engineering Project - Countdown Screen

from tkinter import *
from tkinter import ttk
import time
import globe
from PIL import Image, ImageTk
import subprocess

from globe.view import omni_dir, WIDTH, HEIGHT
import model

gCountdown = None

def create_countdown_screen(root, width=1, height=1, useFactor=True):
    global gCountdown
    gCountdown = IntVar(root)
    # Get the screen dimensions
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    winWidth = (useFactor and screenWidth * width) or width
    winHeight = (useFactor and screenWidth * height) or height
    
    # Get the coordinates
    x = (screenWidth / 2) - (winWidth / 2)
    y = (screenHeight / 2) - (winHeight / 2)
    ##root.geometry(f'{int(winWidth)}x{int(winHeight)}+{int(x)}+{int(y)}')
    
    # Cover the whole screen
    ##root.overrideredirect(True)
    ##root.lift()
    
    # Create the countdown screen frame
    countdown = Frame(root)
    countdown.pack(side=TOP, fill=BOTH, expand=YES)
    
    # Load and resize the image
    # image = Image.open("background.jpg")
    image = Image.open(omni_dir("background.jpg"))
    image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    backgroundImage = ImageTk.PhotoImage(image)
    
    # Create and pack the image label
    imageLabel = Label(countdown, image=backgroundImage)
    imageLabel.image = backgroundImage  
    imageLabel.pack(side=TOP, expand=YES)

    # Create countdown label
    label = Label(countdown, textvariable=gCountdown, font=("Arial", 100, "bold"), fg="yellow", bg="black")
    label.place(relx=0.5, rely=0.545, anchor=CENTER)
    return countdown

def update_countdown(label, count, root):
    if count > 0:
        label.config(text=str(count))
        root.after(1000, update_countdown, label, count - 1, root)
    else:
        root.destroy()
        
if __name__ == '__main__':
    root = Tk()
    countdown = create_countdown_screen(root)
    
    # Start 30-second countdown
    #update_countdown(countdown.label, 30, root)
    
    # Run Tkinter main loop
    root.mainloop()
