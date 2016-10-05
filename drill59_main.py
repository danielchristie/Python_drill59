#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.2
#
# Author:       Tranel Bland
#
# Purpose:      
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk
#from tkinter import filedialog

import drill59_gui
import drill59_func


# Frame is the Tkinter frame class that our own class will inherit from
class MainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(300,200) #(Width, Height)
        self.master.maxsize(400,200)
        # This CenterWindow method will center our app on the user's screen
        drill59_func.center_window(self,500,300)
        self.master.title("The File check & copy tool")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill59_func.ask_quit(self))
        arg = self.master

        # GUI widgets from a separate module
        drill59_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()
