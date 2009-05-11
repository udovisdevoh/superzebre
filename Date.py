#-*- coding: iso-8859-1 -*-
from Tkinter import *
from datetime import timedelta
import time
import datetime  
import os

class Date:
    def __init__(self,root,side):
        self.date = datetime.date.today()
        self.frame = Frame(root)
        self.buttonWeekBack = Button(self.frame, text = "<<", bd = 5, command = self.weekBack)
        self.buttonBack = Button(self.frame, text = "<", bd = 5, command = self.back)
        self.buttonWeekNext = Button(self.frame, text = ">>", bd = 5, command = self.weekNext)
        self.buttonNext = Button(self.frame, text = ">", bd = 5, command = self.next)
        self.dateText = Text(self.frame,height=1,width = 10)
        self.dateText.insert(1.0, self.date)
        self.buttonWeekBack.pack(side=LEFT,padx=2)
        self.buttonBack.pack(side=LEFT,padx=2)
        self.dateText.pack(side=LEFT,padx=2)
        self.buttonNext.pack(side=LEFT,padx=2)
        self.buttonWeekNext.pack(side=LEFT,padx=2)
        self.frame.pack(side=side)
        
    def weekBack(self):
        self.date=self.date - timedelta(weeks=1)
        self.updateDate()
    
    def back(self):
        self.date=self.date - timedelta(days=1)
        self.updateDate()
    
    def weekNext(self):
        self.date=self.date + timedelta(weeks=1)
        self.updateDate()
    
    def next(self):
        self.date=self.date + timedelta(days=1)
        self.updateDate()
    
    def updateDate(self):
        self.dateText.delete(1.0,END)
        self.dateText.insert(1.0,self.date)
    
if __name__ == "__main__":
    root = Tk()
    d=Date(root,TOP)
    root.mainloop()