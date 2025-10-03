#Main program file for the whole code
#importing the pythgui from AIApp
from pythgui import AIApp

#importing tkinter library for GUI
import tkinter as tk




#Main function for the program
if __name__ == "__main__":
    #Creating the main window
    root=tk.Tk()
    #Creating AIAPP instance and passing root as master
    app=AIApp(master=root)

    #main to keep the window open 
    app.mainloop() 