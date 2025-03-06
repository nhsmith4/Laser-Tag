# Charles Williams
# Software Engineering Project - Countdown Screen

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def create_countdown_screen(root, width=1, height=1, useFactor=True):
    # Get the screen dimensions
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    winWidth = (useFactor and screenWidth * width) or width
    winHeight = (useFactor and screenWidth * height) or height
    
    # Get the coordinates
    x = (screenWidth / 2) - (winWidth / 2)
    y = (screenHeight / 2) - (winHeight / 2)
    root.geometry(f'{int(winWidth)}x{int(winHeight)}+{int(x)}+{int(y)}')
    
    # Cover the whole screen
    root.overrideredirect(True)
    root.lift()
    
    # Create the countdown screen frame
    countdown = Frame(root)
    countdown.pack(side=TOP, fill=BOTH, expand=YES)
    
    # Load and resize the image
    image = Image.open("background.jpg")
    image = image.resize((int(screenWidth), int(screenHeight)), Image.Resampling.LANCZOS)
    backgroundImage = ImageTk.PhotoImage(image)
    
    # Create and pack the image label
    imageLabel = Label(countdown, image=backgroundImage)
    imageLabel.image = backgroundImage  
    imageLabel.pack(side=TOP, expand=YES)
    
    # Create countdown label
    countdown_label = Label(countdown, text="30", font=("Arial", 100, "bold"), fg="yellow", bg="black", highlightthickness=0, bd=0)
    countdown_label.place(relx=0.5, rely=0.545, anchor=CENTER)
    
    return countdown, countdown_label

def update_countdown(label, count, root):
    if count > 0:
        label.config(text=str(count))
        root.after(1000, update_countdown, label, count - 1, root)
    else:
        root.destroy()
        
if __name__ == '__main__':
    root = Tk()
    countdown, countdown_label = create_countdown_screen(root)
    
    # Start 30-second countdown
    update_countdown(countdown_label, 30, root)
    
    # Run Tkinter main loop
    root.mainloop()
