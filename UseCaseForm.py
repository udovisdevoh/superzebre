#-*- coding: iso-8859-1 -*-
from Tkinter import *
from UseCase import *
from UseCaseList import *

class UseCaseForm(object):
    def __init__(self, root, title,useCaseList):
        self.initGraphicsComponents(root, title)
        self.useCaseTab = useCaseList
        self.index=len(self.useCaseTab)
        

    def initGraphicsComponents(self, root, title):
        root.minsize(800, 600)
        root.maxsize(800, 600)
        self.canvas = Canvas(root, width = 600, height = 400, bg = "blue")
        self.useCaseTitle = Text(self.canvas, width = 50, height = 1)
        self.useCaseDefinition = Text(self.canvas, height = 10)
        self.useCaseTitle.pack(side=TOP, padx = 25, pady = 10, anchor = W)
        self.useCaseDefinition.pack(side=TOP, padx = 25, pady = 5)
        self.buttonPrevious = Button(self.canvas, text = "<<Précédent", bd = 5, command = self.previous)
        self.buttonNext = Button(self.canvas, text = "Suivant>>", bd = 5, command = self.next)
        self.buttonApply = Button(self.canvas, text = "Valider", bd = 5, command = self.apply)
        self.buttonPrevious.pack(side = LEFT, padx = 25, ipadx = 16, ipady = 5)
        self.buttonNext.pack(side = LEFT, padx = 25, ipadx = 20, ipady = 5)
        self.buttonApply.pack(side = RIGHT, padx = 25, ipadx = 30, ipady = 5)
        self.canvas.pack(anchor = CENTER, padx = 100, pady = 100)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
    
    def next(self):
        if self.useCaseTitle.get(1.0,END)!="\n":
            if self.index == len(self.useCaseTab):
                useCase = UseCase()
                useCase.name = (self.useCaseTitle.get(1.0, END))[:-1]
                useCase.description = (self.useCaseDefinition.get(1.0, END))[:-1]
                self.useCaseTab.append(useCase)        
            else:
                title = self.useCaseTitle.get(1.0, END)
                definition =self.useCaseDefinition.get(1.0, END)
                self.useCaseTab[self.index].name = title[:-1]
                self.useCaseTab[self.index].description = definition[:-1]
            self.index += 1
            if self.index == len(self.useCaseTab):
                self.useCaseTitle.delete(1.0, END)
                self.useCaseDefinition.delete(1.0, END)
            else:
                self.updateText()
        else:
            print "entrez un titre"
            
          
    def updateText(self):
        self.useCaseTitle.delete(1.0, END)
        self.useCaseDefinition.delete(1.0, END)
        self.useCaseTitle.insert(1.0, self.useCaseTab[self.index].name)
        self.useCaseDefinition.insert(1.0, self.useCaseTab[self.index].description)
        
    def apply(self):
        self.canvas.destroy()
        
if __name__ == "__main__":
    root = Tk()
    tab=[UseCase()]
    useCaseForm = UseCaseForm(root, "test",tab)
    useCaseForm.top = Toplevel(root)
    root.wait_window(useCaseForm.top)