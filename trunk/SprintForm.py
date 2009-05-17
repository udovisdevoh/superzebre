#-*- coding: iso-8859-1 -*-
from Tkinter import *
from SprintList import *
from Date import *
from datetime import timedelta
import time
import datetime  
from WordCheck import *


class SprintForm:
    def __init__(self,root,title,sprintList, sortedWords, project, client):
        self.client = client
        self.project = project
        self.sprintList = sprintList
        self.root = root
        self.index = 0
        
        wordList = []
        self.checkList = []
        listName = sortedWords.noms[:]
        self.checkList.append(listName[:])
        listName.insert(0,"Noms")
        wordList.append(listName)
        listName = sortedWords.adjectifs[:]
        self.checkList.append(listName[:])
        listName.insert(0,"Adjectif")
        wordList.append(listName)
        listName = sortedWords.verbes[:]
        self.checkList.append(listName[:])
        listName.insert(0,"Verbes")
        wordList.append(listName)
        
        self.initGraphicComponents(root,title, wordList)
        
    def initGraphicComponents(self,root,title, wordList):
        for i in self.root.pack_slaves():
            i.destroy()
        root.title(title)
        
        self.frameGlobal = Frame()
        self.frameDate = Frame(self.frameGlobal)
        self.frameDateName= Frame(self.frameGlobal)
        self.frameButton = Frame(self.frameGlobal)
        
        self.startingDateLabel = Label(self.frameDateName,text="Date de commencement")
        self.endingDateLabel = Label(self.frameDateName,text="Date de fin          ")
        
        self.startingDate = Date(self.frameDate,LEFT)
        self.endingDate = Date(self.frameDate,RIGHT)
        self.endingDate.next()
        
        self.description = Text(self.frameGlobal,height = 10)
        if len(self.sprintList.sprint)>0:
            self.description.insert(1.0,self.sprintList.sprint[self.index].description)
            self.startingDate.setDate(self.sprintList.sprint[self.index].startingDate)
            self.endingDate.setDate(self.sprintList.sprint[self.index].endingDate)
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
        
        self.autoCompletionDescription = AutoCompletion(root,wordList,True,self.description,5,50)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
            
    def next(self):
        if self.index == len(self.sprintList.sprint):
            sprint = Sprint()
            text = self.description.get(1.0, END)
            sprint.description = text[:-1]
            sprint.startingDate = self.startingDate.getDate()
            sprint.endingDate = self.endingDate.getDate()
            self.sprintList.add(sprint)
        else:
            text = self.description.get(1.0, END)
            self.sprintList.sprint[self.index].description = text[:-1]
        self.index += 1
        if self.index == len(self.sprintList.sprint):
            self.description.delete(1.0, END)
            self.startingDate.setDate(self.endingDate.getDate()+ timedelta(days=1))
            self.endingDate.next()
            self.endingDate.next()
        else:
            self.updateText()
    
    def updateText(self):
        try:
            self.description.delete(1.0, END)
            self.description.insert(1.0, self.sprintList.sprint[self.index].description)
            self.startingDate.setDate(self.sprintList.sprint[self.index].startingDate)
            self.endingDate.setDate(self.sprintList.sprint[self.index].endingDate)
        except IndexError:
            pass
    def apply(self):
        self.next()
        
        textList = []
        for element in self.sprintList.sprint:
            textList.append(element.description)
            
        wordCheck = WordCheck(self.checkList, textList, self.root)
        status = wordCheck.activate()
        if status != None:
            for i in self.root.pack_slaves():
                i.destroy()
            if status:
                self.project.colorSprint = self.project.colorOk
            else:
                self.project.colorSprint = self.project.colorPending
            self.client.tryShowTreeView()
    
if __name__ == "__main__":
    root = Tk()
    root.minsize(800, 600)
    sprintList = SprintList()
    sprintList.add(Sprint(datetime.date.today(),datetime.date.today()+ timedelta(days = 1),"Keven est épais"))
    sprintForm = SprintForm(root,"test",sprintList)
    root.mainloop()        