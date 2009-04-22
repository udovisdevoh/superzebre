#-*- coding: iso-8859-1 -*-
from Tkinter import *

class UseCaseForm(object):
    def __init__(self, root, title):
        self.initGraphicsComponents(root, title)
        self.tabTitle = []
        self.tabDefinition = []
        self.index = -1
    
    def initGraphicsComponents(self, root, title):
        root.minsize(800, 600)
        root.maxsize(800, 600)
        self.canvas = Canvas(root, width = 800, height = 600)
        self.useCaseTitle = Text(self.canvas, width = 50, height = 1)
        self.useCaseDefinition = Text(self.canvas, height = 10)
        self.useCaseTitle.pack(side=TOP, padx = 25, pady = 10, anchor = W)
        self.useCaseDefinition.pack(side=TOP, padx = 25, pady = 5)
        self.buttonPrevious = Button(self.canvas, text = "<<Précédent", command = self.previous)
        self.buttonNext = Button(self.canvas, text = "Suivant>>", command = self.next)
        self.buttonApply = Button(self.canvas, text = "Valider", command = self.apply)
        self.buttonPrevious.pack(side = LEFT)
        self.buttonNext.pack(side = LEFT)
        self.buttonApply.pack(side = LEFT)
        self.canvas.pack()
    
    def previous(self):
        if self.index != 0 and self.index != -1:
            self.index -= 1
            self.updateText()
    
    def next(self):
        self.index += 1
        if self.index == len(self.tabTitle):
            self.tabTitle.append(self.useCaseTitle.get(1.0, END))
            self.tabDefinition.append(self.useCaseDefinition.get(1.0, END))
            self.useCaseTitle.delete(1.0, END)
            self.useCaseDefinition.delete(1.0, END)        
        else:
            self.updateText() 
          
    def updateText(self):
        self.useCaseTitle.delete(1.0, END)
        self.useCaseDefinition.delete(1.0, END)
        self.useCaseTitle.insert(1.0, self.tabTitle[self.index])
        self.useCaseDefinition.insert(1.0, self.tabDefinition[self.index])
        
    def apply(self):
        pass
    
if __name__ == "__main__":
    root = Tk()
    useCaseForm = UseCaseForm(root, "test")
    useCaseForm.top = Toplevel(root)
    root.wait_window(useCaseForm.top)