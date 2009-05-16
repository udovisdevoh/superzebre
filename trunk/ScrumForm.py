from Tkinter import *
from ScrumList import *
from AutoCompleteWidget import *
import time
import datetime  
import os
from WordCheck import *

class ScrumForm: 
    def __init__(self,root,title,scrumList, sortedWords,project, client):
        self.project = project
        self.client = client
        self.scrumList = scrumList
        self.root = root
        self.today = datetime.date.today()
        
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
        
        self.initGraphicComponents(root,title)
        self.graphicalScrumList = self.getGraphicalScrumList(scrumList)
        self.loadbyDate()
    
    def initGraphicComponents(self,root,title):
        for i in root.pack_slaves():
            i.destroy()
        root.title(title)
        self.frameTop = Frame()
        self.frameMiddle = Frame()
        self.frameButtons = Frame()
        self.frameBottom = Frame()
        self.frameDate = Frame()
        self.frameDate.pack(side=TOP, fill= X,pady=20)
        self.frameTop.pack(side=TOP, pady = 10, padx =10)
        self.frameMiddle.pack(pady = 10)
        self.frameBottom.pack(side=TOP, pady = 10)
        self.frameButtons.pack(side=TOP, pady = 20, fill=BOTH)
        self.buttonOk = Button(self.frameButtons,text = "OK", command=self.commandApply, width = 10)
        self.buttonPrecedent= Button(self.frameButtons,text = "Precedent", command=self.commandPrecedent,width = 10)
        self.buttonSuivant = Button(self.frameButtons,text = "Suivant", command=self.commandSuivant,width = 10)
        self.buttonOk.pack()# low priotity Changer le packing... just ici en creant un nouveau frame pour ... mieux packer
        self.buttonSuivant.pack(side= RIGHT, anchor=E,padx=10)
        self.buttonPrecedent.pack(side = LEFT,anchor=W,padx=10)
        self.labelDate = Label(self.frameDate, text= "Date")
        self.laDate = Text(self.frameDate, height = 1,width=20,)
        self.laDate.insert(INSERT, self.today)
        self.laDate.pack(anchor=W,padx=10,side=BOTTOM,)
        self.labelAppliquer = Label(self.frameButtons, text = " Les changements ont ete appliques!", fg = "blue")
        self.labelDate.pack(anchor=W,padx=7,)
        self.laDate.config(state=DISABLED)
        self.textTop = Text(self.frameTop,height = 5, width = 75)
        self.labTop = Label(self.frameTop, text="Taches accomplies")
        self.labTop.pack(anchor=W)
        self.textTop.pack()
        self.textTop.focus_force()
        self.textMiddle = Text(self.frameMiddle,height = 5, width = 75)
        self.labMiddle = Label(self.frameMiddle, text="Taches a accomplir" )
        self.labMiddle.pack(anchor=W)
        self.textMiddle.pack()
        self.textBottom = Text(self.frameBottom,height = 5, width = 75)
        self.labBottom = Label(self.frameBottom, text="Problemes ")
        self.labBottom.pack(anchor=W)
        self.textBottom.pack()
    
    def getGraphicalScrumList(self,scrumList):
        graphicalScrumList = []
        for currentScrum in scrumList.scrum:
            currentScrumData = []
            currentScrumData.append(currentScrum.date)
            currentScrumData.append(currentScrum.done)
            currentScrumData.append(currentScrum.todo)
            currentScrumData.append(currentScrum.problem)
            graphicalScrumList.append(currentScrumData)
        return graphicalScrumList
    
    def getScrumListFromGraphicalScrumList(self, graphicalScrumList):
        self.scrumList.scrum = []
        for currentGraphicalScrum in graphicalScrumList:
            currentScrum = Scrum(currentGraphicalScrum[0],"",currentGraphicalScrum[2],currentGraphicalScrum[1],currentGraphicalScrum[3])
            self.scrumList.scrum.append(currentScrum)
        return self.scrumList
    
    def commandApply(self):
        self.addToScrumList()
        self.labelAppliquer.pack()
        self.scrumList = self.getScrumListFromGraphicalScrumList(self.graphicalScrumList)

        textList = []
        for element in self.scrumList.scrum:
            textList.append(element.todo)
            textList.append(element.done)
            textList.append(element.problem)
            
        wordCheck = WordCheck(self.checkList, textList, self.root)
        status = wordCheck.activate()
        if status != None:
            for i in self.root.pack_slaves():
                i.destroy()
            if status:
                self.project.colorSCRUM = self.project.colorOk
            else:
                self.project.colorSCRUM = self.project.colorPending
            self.client.tryShowTreeView()
        
    def loadbyDate(self):
        for scrum in self.graphicalScrumList:
            date = str(scrum[0]).strip()
            laDateDeCeJour = str(self.laDate.get(1.0, END)[:-1])
            if date == str(self.laDate.get(1.0, END)[:-1]):
                date = str(date).strip()
                tachesDone = str(scrum[1]).strip()
                tachesToBeMade = str(scrum[2]).strip()
                problems = str(scrum[3]).strip()
                self.textTop.insert(INSERT, tachesDone)
                self.textMiddle.insert(INSERT, tachesToBeMade)
                self.textBottom.insert(INSERT, problems)
                break
         
    def addToScrumList(self):
        list = []
        textT  = str(self.textTop.get(1.0, END)[:-1])
        textM  =str( self.textMiddle.get(1.0, END)[:-1])
        textB = str(self.textBottom.get(1.0, END)[:-1])
        textDate = str(self.laDate.get(1.0, END)[:-1])
        list.append(textDate)
        list.append(textT)
        list.append(textM)
        list.append(textB)
        if len (self.graphicalScrumList) == 0 :
            self.graphicalScrumList.append(list)
        else : 
            listFound = False
            for i , scrum in enumerate (self.graphicalScrumList): 
                if textDate == str(scrum[0]).strip():
                    list.append(textDate)
                    list.append(textT)
                    list.append(textM)
                    list.append(textB)
                    self.graphicalScrumList.pop(i)
                    self.graphicalScrumList.insert(i,list)
                    listFound = True 
                    break; 
            if not listFound :
                self.graphicalScrumList.append(list)
                
    def commandPrecedent(self):
        self.addToScrumList()
        self.laDate.config(state=NORMAL)
        oneDay = datetime.timedelta(days=1)
        self.today -= oneDay
        self.laDate.delete(1.0, END)
        self.laDate.insert(INSERT, self.today)
        self.clearTextfields()
        self.laDate.config(state=DISABLED)
        self.textTop.focus_force()
        self.loadbyDate()
    
    def commandSuivant(self):
        self.addToScrumList()
        self.laDate.config(state=NORMAL)
        oneDay = datetime.timedelta(days=1)
        self.today += oneDay
        self.laDate.delete(1.0, END)
        self.laDate.insert(INSERT, self.today)
        self.clearTextfields()
        self.laDate.config(state=DISABLED)
        self.textTop.focus_force()
        self.loadbyDate()

    def clearTextfields(self):
        self.textTop.delete(1.0, END)
        self.textMiddle.delete(1.0, END)
        self.textBottom.delete(1.0, END)
                
if __name__ == "__main__":
    scrumList = ScrumList();
    scrumList.scrum.append(Scrum("2009-05-01","dfggd","sdfgdfgas","dfgdgf","ghsdafdfh"))
    scrumList.scrum.append(Scrum("2009-05-02","dgd","sdfgfdsdfgdfgas","dfgf","gdafdfh"))
    root = Tk()
    root.config(width =600, height = 800)
    root.title("Formulaire de Scrum") 
    scrumForm = ScrumForm(root,scrumList)
    root.mainloop()