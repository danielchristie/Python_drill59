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


#import drill50_phonebook_main
#import drill50_phonebook_func
import drill59_main
import drill59_func


def load_gui(self):

    self.lbl_title = tk.Label(self.master,text='File Check & Copy Tool')
    self.lbl_title.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0),sticky=N+W+E+S)
    self.lbl_strtPath = tk.Label(self.master,text='Start Folder:')
    self.lbl_strtPath.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_dstPath = tk.Label(self.master,text='Destination Folder:')
    self.lbl_dstPath.grid(row=1,column=1,padx=(27,0),pady=(10,0),sticky=N+W)


#    self.lbl_email = tk.Label(self.master,text='Email Address:')
#    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
#    self.lbl_info = tk.Label(self.master,text='Information:')
#    self.lbl_info.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    self.txt_strtPath = tk.Entry(self.master,text='')
    self.txt_strtPath.insert(0, "<<start path>>")
    self.txt_strtPath.grid(row=2,column=0,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_dstPath = tk.Entry(self.master,text='')
    self.txt_dstPath.insert(0, "<<end path>>")
    self.txt_dstPath.grid(row=2,column=1,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    
#    self.txt_phone = tk.Entry(self.master,text='')
#    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
#    self.txt_email = tk.Entry(self.master,text='')
#    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
#    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
#    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
#    self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
#    self.scrollbar1.config(command=self.lstList1.yview)
#    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
#    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    self.btn_strtPath = tk.Button(self.master,width=20,height=2,text='Select Source Folder',command=lambda: drill59_func.getStrtPath(self))
    self.btn_strtPath.grid(row=3,column=0,padx=(15,0),pady=(2,10),sticky=W)
    self.btn_dstPath = tk.Button(self.master,width=20,height=2,text='Select Destination',command=lambda: drill59_func.getDstPath(self))
    self.btn_dstPath.grid(row=3,column=1,padx=(15,0),pady=(2,10),sticky=W)
    self.btn_strtTool = tk.Button(self.master,width=12,height=2,text='START',command=lambda: drill59_func.copyTool(self))
    self.btn_strtTool.grid(row=4,column=0,rowspan=2,padx=(15,0),pady=(2,10))
#    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: drill50_phonebook_func.ask_quit(self))
#    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    #drill50_phonebook_func.create_db(self)
    #drill50_phonebook_func.onRefresh(self)

    



if __name__ == "__main__":
    pass
