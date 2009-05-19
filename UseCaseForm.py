#-*- coding: iso-8859-1 -*-
from Tkinter import *
from UseCaseList import *
from AutoCompleteWidget import *
from WordCheck import *

class UseCaseForm:
    def __init__(self, root, title, useCaseList,sortedWords, project, client):
        self.client = client
        self.root = root
        self.project = project
        self.useCaseList = useCaseList;
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
        self.initGraphicsComponents(root, title,wordList)
        self.tabTitle = []
        self.tabDefinition = []
        self.index = 0
        self.addToFields(useCaseList)
        self.updateText()
    
    def initGraphicsComponents(self, root, title,wordList):
        for i in root.pack_slaves():
            i.destroy()
        root.minsize(800, 600)
        root.title(title)
          
        self.canvas = Canvas(root, width = 600, height = 400)
        self.frameTop = Frame(self.canvas)
        self.frameBottom = Frame(self.canvas)
        self.frameTop.pack(side=TOP,anchor = W, pady = 20)
        self.frameBottom.pack(side=BOTTOM, anchor= W)
        self.labelTitre = Label (self.frameTop, text= "Le titre du cas d'usage")
        self.useCaseTitle = Text(self.frameTop, width = 50, height = 1)
        self.labelTitre.pack(side = TOP, anchor = W )
        self.useCaseTitle.pack(side= BOTTOM,  pady = 10, anchor = W)
        self.labelScenario = Label(self.frameBottom, text = "Le scenario d'utilisation") 
        self.useCaseDefinition = Text(self.frameBottom, height = 10)
        self.labelScenario.pack(side=TOP, anchor = W)
        self.useCaseDefinition.pack(side=TOP,pady = 10, anchor = W)
        self.buttonPrevious = Button(self.frameBottom, text = "<<Précédent", bd = 5, command = self.previous)
        self.buttonNext = Button(self.frameBottom, text = "Suivant>>", bd = 5, command = self.next)
        self.buttonApply = Button(self.frameBottom, text = "Valider", bd = 5, command = self.apply)
        self.buttonPrevious.pack(side = LEFT, padx = 25, ipadx = 16, ipady = 5)
        self.buttonNext.pack(side = LEFT, padx = 25, ipadx = 20, ipady = 5)
        self.buttonApply.pack(side = RIGHT, padx = 25, ipadx = 30, ipady = 5)
        self.canvas.pack(anchor = CENTER, padx = 100, pady = 100)
        self.autoCompletionTitle = AutoCompletion(root,wordList,True,self.useCaseTitle,5,50)
        self.autoCompletionDefinition = AutoCompletion(root,wordList,True,self.useCaseDefinition,5,50)
        
    
    def addToFields(self,useCaseList):
        for currentUseCase in useCaseList.useCase:
            self.tabTitle.append(currentUseCase.name)
            self.tabDefinition.append(currentUseCase.description)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
    
    def next(self):
        if self.index == len(self.tabTitle):
            text = self.useCaseTitle.get(1.0, END)
            self.tabTitle.append(text[:-1])
            text =self.useCaseDefinition.get(1.0, END) 
            self.tabDefinition.append(text[:-1])        
        else:
            text = self.useCaseTitle.get(1.0, END)
            self.tabTitle[self.index] = text[:-1]
            text =self.useCaseDefinition.get(1.0, END)
            self.tabDefinition[self.index] = text[:-1]
        self.index += 1
        if self.index == len(self.tabTitle):
            self.useCaseTitle.delete(1.0, END)
            self.useCaseDefinition.delete(1.0, END)
        else:
            self.updateText()
          
    def updateText(self):
        try:
            self.useCaseTitle.delete(1.0, END)
            self.useCaseDefinition.delete(1.0, END)
            self.useCaseTitle.insert(1.0, self.tabTitle[self.index])
            self.useCaseDefinition.insert(1.0, self.tabDefinition[self.index])
        except IndexError:
            pass
        
    def apply(self):
        
        self.next()
        self.useCaseList.useCase=[]
        
        i = 0
        for title in self.tabTitle:
            self.useCaseList.useCase.append(UseCase(title,self.tabDefinition[i]))
            i += 1
        textList = []
        for element in self.useCaseList.useCase:
            textList.append(element.name)
            textList.append(element.description)
            
        wordCheck = WordCheck(self.checkList, textList, self.root)
        status = wordCheck.activate()
        if status != 0:
            self.canvas.destroy()
            if status == 1:
                self.project.colorUseCase = self.project.colorOk
            elif status == 2:
                self.project.colorUseCase = self.project.colorPending
            elif status == 3:
                self.project.colorUseCase = self.project.colorOrange
            self.client.tryShowTreeView()
                
    
if __name__ == "__main__":
    root = Tk()
    useCaseList = UseCaseList()
    useCaseList.add(UseCase("fdgfdg","fdhgfhgfhgfhgf"))
    useCaseList.add(UseCase("fdgfdg2","fdhgfhgfhgfhgf2"))
    useCaseForm = UseCaseForm(root, "test", useCaseList,)
    useCaseForm.top = Toplevel(root)
    root.wait_window(useCaseForm.top)