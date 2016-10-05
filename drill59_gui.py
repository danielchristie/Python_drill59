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

import drill59_main
import drill59_func


def load_gui(self):

    self.lbl_title = tk.Label(self.master,text='File Check & Copy Tool')
    self.lbl_title.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0),sticky=N+W+E+S)
    self.lbl_strtPath = tk.Label(self.master,text='Start Folder:')
    self.lbl_strtPath.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_dstPath = tk.Label(self.master,text='Destination Folder:')
    self.lbl_dstPath.grid(row=1,column=1,padx=(27,0),pady=(10,0),sticky=N+W)

    self.txt_strtPath = tk.Entry(self.master,text='')
    self.txt_strtPath.insert(0, "<<start path>>")
    self.txt_strtPath.grid(row=2,column=0,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_dstPath = tk.Entry(self.master,text='')
    self.txt_dstPath.insert(0, "<<end path>>")
    self.txt_dstPath.grid(row=2,column=1,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    self.btn_strtPath = tk.Button(self.master,width=20,height=2,text='Select Source Folder',command=lambda: drill59_func.getStrtPath(self))
    self.btn_strtPath.grid(row=3,column=0,padx=(15,0),pady=(2,10),sticky=W)
    self.btn_dstPath = tk.Button(self.master,width=20,height=2,text='Select Destination',command=lambda: drill59_func.getDstPath(self))
    self.btn_dstPath.grid(row=3,column=1,padx=(15,0),pady=(2,10),sticky=W)
    self.btn_strtTool = tk.Button(self.master,width=12,height=2,text='START',command=lambda: drill59_func.copyTool(self))
    self.btn_strtTool.grid(row=4,column=0,rowspan=2,padx=(15,0),pady=(2,10))

if __name__ == "__main__":
    pass
