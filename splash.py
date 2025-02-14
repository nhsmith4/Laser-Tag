# Charles Williams
# Software Engineering Project - Splash Screen

# Website referenced: https://www.geeksforgeeks.org/how-to-create-a-splash-screen-using-tkinter/?ref=ml_lbp

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class SplashScreen(Frame):
    def __init__(self, master=None, width=1, height=1, useFactor=True):
        super().__init__(master)
        
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # Get screen dimensions
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        width = (useFactor and screenWidth * width) or width
        height = (useFactor and screenWidth * height) or height
        
        # Get the coordinates
        x = (screenWidth / 2) - (width / 2)
        y = (screenHeight / 2) - (height / 2)
        self.master.geometry(f'{int(width)}x{int(height)}+{int(x)}+{int(y)}')
       
        # Cover whole screen
        self.master.overrideredirect(True)
        self.lift()
        
# Might need to use update or something in order to link with player entry screen
def main():
    # Create the main window
    splashScreen = Tk()
    
    # Load and resize image
    image = Image.open("logo.jpg")

    image = image.resize((int(splashScreen.winfo_screenwidth()), int(splashScreen.winfo_screenheight())), Image.Resampling.LANCZOS)
    backgroundImage = ImageTk.PhotoImage(image)

    # Creates the splash screen and image
    splash = SplashScreen(splashScreen)
    imageLabel = Label(splash, image=backgroundImage)
    imageLabel.image = backgroundImage
    imageLabel.pack(side=TOP, expand=YES)
    
    # Splash screen lasts 3 seconds
    splashScreen.after(3000, lambda: (splashScreen.destroy(), splashScreen.quit()))

    # Run Tkinter main loop
    splashScreen.mainloop()

if __name__ == '__main__':
    main()

# Leads into player select screen presumably
