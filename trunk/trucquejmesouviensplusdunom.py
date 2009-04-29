#-*- coding: iso-8859-1 -*-
from Tkinter import *

class CrcForm(object):
    def __init__(self, root, title):
        self.initGraphicsComponents(root, title)
        self.tabTitle = []
        self.tabResponsability = []
        self.index = 0
    
    def initGraphicsComponents(self, root, title):
        root.minsize(800, 600)
        root.maxsize(800, 600)
        self.canvas = Canvas(root, width = 700, height = 500, bg = "blue")
        self.crcTitle = Text(self.canvas, width = 50, height = 1)
        self.crcResponsability = Text(self.canvas, height = 10, width = 30)
        self.crcColaborators = Text(self.canvas, height = 10, width = 20)
        self.crcTitle.pack(side = TOP, padx = 25, pady = 10, anchor = W)
        self.crcResponsability.pack(side = TOP, padx = 5, pady = 5)
        self.crcColaborators.pack(side = TOP, pady = 5)
        self.buttonPrevious = Button(self.canvas, text = "<<Précédent", bd = 5, command = self.previous)
        self.buttonNext = Button(self.canvas, text = "Suivant>>", bd = 5, command = self.next)
        self.buttonApply = Button(self.canvas, text = "Valider", bd = 5, command = self.apply)
        self.buttonPrevious.pack(side = LEFT, padx = 25, ipadx = 16, ipady = 5)
        self.buttonNext.pack(side = LEFT, padx = 25, ipadx = 20, ipady = 5)
        self.buttonApply.pack(side = RIGHT, padx = 25, ipadx = 30, ipady = 5)
        self.canvas.pack(anchor = CENTER, padx = 25, pady = 25)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
    
    def next(self):
        if self.crcTitle.get(1.0,END)!="\n":
            if self.index == len(self.tabTitle):
                text = self.crcTitle.get(1.0, END)
                self.tabTitle.append(text[:-1])
                text =self.crcResponsability.get(1.0, END) 
                self.tabResponsability.append(text[:-1])        
            else:
                text = self.crcTitle.get(1.0, END)
                self.tabTitle[self.index] = text[:-1]
                text =self.crcResponsability.get(1.0, END)
                self.tabResponsability[self.index] = text[:-1]
            self.index += 1
            if self.index == len(self.tabTitle):
                self.crcTitle.delete(1.0, END)
                self.crcResponsability.delete(1.0, END)
            else:
                self.updateText()
        else:
            print "entrez un titre"
            
          
    def updateText(self):
        self.crcTitle.delete(1.0, END)
        self.crcResponsability.delete(1.0, END)
        self.crcTitle.insert(1.0, self.tabTitle[self.index])
        self.crcResponsability.insert(1.0, self.tabResponsability[self.index])
        
    def apply(self):
        self.tab = {}
        for i in range(len(self.tabTitle)+1):
            self.tab[self.tabTitle[i]] = self.tabResponsability[i]
        return self.tab
    
if __name__ == "__main__":
    root = Tk()
    crcForm = CrcForm(root, "test")
    crcForm.top = Toplevel(root)
    root.wait_window(crcForm.top)