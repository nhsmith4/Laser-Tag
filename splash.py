# Charles Williams
# Software Engineering Project - Splash Screen

# Website referenced: https://www.geeksforgeeks.org/how-to-create-a-splash-screen-using-tkinter/?ref=ml_lbp

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

from globe.view import omni_dir, WIDTH, HEIGHT

def create_splash_screen(root, width=1, height=1, useFactor=True):
    # Get the screen dimensions
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    winWidth = (useFactor and screenWidth * width) or width
    winHeight = (useFactor and screenWidth * height) or height
    
    # Get the coordinates
    x = (screenWidth / 2) - (winWidth / 2)
    y = (screenHeight / 2) - (winHeight / 2)
    ## root.geometry(f'{int(winWidth)}x{int(winHeight)}+{int(x)}+{int(y)}')
    
    # Cover the whole screen
    
    # Create the splash screen frame
    splash = Frame(root, relief=SUNKEN)
    splash.pack(side=TOP, fill=BOTH, expand=YES)
    
    # Load and resize the image
    image = Image.open(omni_dir("logo.jpg"))
    image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    backgroundImage = ImageTk.PhotoImage(image)
    
    # Create and pack the image label
    imageLabel = Label(splash, image=backgroundImage)
    imageLabel.image = backgroundImage  
    imageLabel.pack(side=TOP, expand=YES)
    
    return splash

def startPlayerEntryScreen():
    subprocess.run(["python", "player_entry_screen.py"])  # Runs the player entry screen


if __name__ == '__main__':
    root = Tk()
    splash = create_splash_screen(root)
    
    # Splash screen lasts 3 seconds
    root.after(3000, lambda: (root.destroy(), startPlayerEntryScreen()))
    
    # Run Tkinter main loop
    root.mainloop()
