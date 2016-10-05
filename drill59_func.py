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


import shutil
import datetime
#import pytz
import os
import os.path
import sys
from datetime import datetime
from datetime import date 
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
#import sqlite3


# Be sure to import our other modules 
# so we can have access to them
#import drill59_main
#import drill59_gui

#strtPath = ''
#dstPath = ''

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)




def getStrtPath(self):
    #strtPath = raw_input('Enter start path\\folder: ')
    #self.txt_strtPath.delete(0, END)
    #self.txt_strtPath.insert(0, "<<start path>>")
    global strtPath
    strtPath =  filedialog.askdirectory(initialdir = "/")
    self.txt_strtPath.delete(0, END)
    self.txt_strtPath.insert(0, strtPath)
    return strtPath
    
    


def getDstPath(self):
    #dstPath = raw_input('Enter destination path\\folder: ')
    global dstPath
    dstPath =  filedialog.askdirectory(initialdir = "/")
    self.txt_dstPath.delete(0, END)
    self.txt_dstPath.insert(0, dstPath)
    return dstPath

def copyTool(self):
    tday = datetime.today()
    t01_Year = int(str(tday)[:4])
    #print "t01_Year is {}".format(t01_Year)
    t01_Month = int(str(tday)[5:7])
    #print "t01_Month is {}".format(t01_Month)
    t01_Day = int(str(tday)[8:10])
    #print "t01_Day is {}".format(t01_Day)
    t01_date = date(t01_Year, t01_Month, t01_Day)
    dirs = os.listdir(strtPath)
    
    
    for var in dirs:
        #for i in list:
        varN = strtPath + '\\' + var
        #varFLT = float(varN)
        #print varN
            
    
        #total_path = dirs + var
        print ("#"*20)
        ##print tb_test
        #print var
        #print dirs
        #print type(dirs)
        fileCTime = os.path.getctime(varN)
        whats_fileCTime = type(fileCTime)
        #print "The fileCTime var is a {} and looks like {}".format(whats_fileCTime,fileCTime)
        #print "The fileCTime var is {}".format(fileCTime)
        standardCtime = datetime.fromtimestamp(fileCTime).strftime('%Y-%m-%d %H:%M:%S')
        print ("The created time of {} is {}".format(var, standardCtime))
        fileMTime = os.path.getmtime(varN)
        standardMtime = datetime.fromtimestamp(fileCTime).strftime('%Y-%m-%d %H:%M:%S')
        print ("The modified time of {} is {}".format(var, standardMtime))
        dataList = [var,standardCtime,standardMtime,varN]
        cYear = int(dataList[1][:4])
        #print 'cYear = {}'.format(cYear)
        cMonth = int(dataList[1][5:7])
        #print 'cMonth = {}'.format(cMonth)
        cDay = int(dataList[1][8:10])
        #print 'cDay = {}'.format(cDay)
        f_date = date(cYear, cMonth,cDay)
        mYear = int(dataList[2][:4])
        mMonth = int(dataList[2][5:7])
        mDay = int(dataList[2][8:10])
        m_date = date(mYear, mMonth,mDay)
        
        #print "f_date looks like this -> {} and is {}".format(f_date, type(f_date))
        if f_date >= t01_date and m_date >= t01_date:
            print ("====>>>Copied {} to {}<<<=====".format(var,dstPath))
            shutil.copy(varN, dstPath)
        elif f_date <= t01_date:
            print ("====>>>The f_date of {} is older than today's date<<<=====".format(dataList[0]))
        elif m_date <= t01_date:
            print ("====>>>The m_date of {} is older than today's date<<<=====".format(dataList[0]))
        else:
            print ("<<<=====  huh? Moving on... =====>>>")
            pass
    
   


if __name__ == "__main__":
    pass
