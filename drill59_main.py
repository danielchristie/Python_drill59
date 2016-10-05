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

# Be sure to import our other modules 
# so we can have access to them
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

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        drill59_gui.load_gui(self)
        drill59_gui.load_gui(self)
        
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        #menubar = Menu(self.master)
        #filemenu = Menu(menubar, tearoff=0)
        #filemenu.add_separator()
        #filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: drill50_phonebook_func.ask_quit(self))
        #menubar.add_cascade(label="File", underline=0, menu=filemenu)
        #helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        #helpmenu.add_separator()
        #helpmenu.add_command(label="How to use this program")
        #helpmenu.add_separator()
        #helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        #menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        #"""
        #    Finally, we apply the config method of the widget to display the menu
        #    From here we could also pass in additional aprams for additional 
        #    functionalityor appearances such as a borderwidth.
        #"""
        #self.master.config(menu=menubar, borderwidth='1')



if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()
