#-*- coding: iso-8859-1 -*-
from Tkinter import *
from SprintList import *
from Date import *

class SprintForm:
    def __init__(self,root,title,sprintList):
        self.sprintList = sprintList
        self.root = root
        self.initGraphicComponents(root,title)
        self.index = 0

    def initGraphicComponents(self,root,title):
        for i in root.pack_slaves():
            i.destroy()
        root.title(title)
        
        self.frameGlobal = Frame()
        self.frameDate = Frame(self.frameGlobal)
        self.frameDateName= Frame(self.frameGlobal)
        self.frameButton = Frame(self.frameGlobal)
        
        self.startingDateLabel = Label(self.frameDateName,text="Date de commencement")
        self.endingDateLabel = Label(self.frameDateName,text="Date de fin          ")
        
        self.description = Text(self.frameGlobal,height = 10)
        if len(self.sprintList.sprint)>0:
            self.description.insert(1.0,self.sprintList.sprint[index].description)
        self.startingDate = Date(self.frameDate,LEFT)
        self.endingDate = Date(self.frameDate,RIGHT)
        self.buttonPrevious = Button(self.frameButton, text = "<<Précédent", bd = 5, command = self.previous)
        self.buttonNext = Button(self.frameButton, text = "Suivant>>", bd = 5, command = self.next)
        self.buttonApply = Button(self.frameButton, text = "Valider", bd = 5, command = self.apply)
        
        self.startingDateLabel.pack(side=LEFT)
        self.endingDateLabel.pack(side=RIGHT)
        self.frameDateName.pack(side=TOP,ipadx=168)
        self.buttonPrevious.pack(side = LEFT, ipadx = 16, ipady = 5)
        self.buttonNext.pack(side = LEFT, padx = 25, ipadx = 20, ipady = 5)
        self.buttonApply.pack(side = RIGHT, ipadx = 30, ipady = 5)
        self.frameDate.pack(side=TOP,ipadx=100)
        self.description.pack(side = TOP,pady=20)
        self.frameButton.pack(side = TOP,ipadx = 100)
        self.frameGlobal.pack(side = TOP,pady=160)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
            
    def next(self):
        if self.index == len(self.sprintList.sprint):
            sprint = Sprint()
            text = self.description.get(1.0, END)
            sprint.description = text[:-1]
            self.sprintList.add(sprint)
        else:
            text = self.description.get(1.0, END)
            self.sprintList.sprint[self.index].description = text[:-1]
        self.index += 1
        if self.index == len(self.sprintList.sprint):
            self.description.delete(1.0, END)
        else:
            self.updateText()
    
    def updateText(self):
        try:
            self.description.delete(1.0, END)
            self.description.insert(1.0, self.sprintList.sprint[self.index].description)
        except IndexError:
            pass
    def apply(self):
        self.next()
        for i in root.pack_slaves():
            i.destroy()
    
if __name__ == "__main__":
    root = Tk()
    root.minsize(800, 600)
    sprintList = SprintList()
    sprintForm = SprintForm(root,"test",sprintList)
    root.mainloop()        