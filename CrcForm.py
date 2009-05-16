#-*- coding: iso-8859-1 -*-
from Tkinter import *
from CrcList import *
from AutoCompleteWidget import *
from WordCheck import *

class CrcForm(object):
    def __init__(self, root, title, crcList,sortedWords, project, client):
        self.root = root
        self.client = client
        self.project = project
        self.crcList = crcList
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
        self.tabResponsability = []
        self.tabColaborators = []
        self.index = 0
        self.addToFields(crcList)
        self.updateText()
    
    def initGraphicsComponents(self, root, title,wordList):
        for i in root.pack_slaves():
            i.destroy()
        root.minsize(800, 600)
        root.title(title)
        self.canvas = Canvas(root, width = 700, height = 500)
        self.textFrame = Frame(self.canvas, width = 600, height = 400)
        self.crcClass = Text(self.textFrame, width = 50, height = 1)
        self.crcResponsability = Text(self.textFrame, height = 10, width = 30)
        self.crcColaborators = Text(self.textFrame, height = 10, width = 20)
        self.crcClass.pack(side = TOP, padx = 5, pady = 10, anchor = W)
        self.crcResponsability.pack(side = LEFT, padx = 5, pady = 5)
        self.crcColaborators.pack(side = LEFT, pady = 5)
        self.textFrame.pack(side = TOP, padx = 20, pady = 20)
        self.buttonPrevious = Button(self.canvas, text = "<<Précédent", bd = 5, command = self.previous)
        self.buttonNext = Button(self.canvas, text = "Suivant>>", bd = 5, command = self.next)
        self.buttonApply = Button(self.canvas, text = "Valider", bd = 5, command = self.apply)
        self.buttonPrevious.pack(side = LEFT, padx = 25, ipadx = 16, ipady = 5)
        self.buttonNext.pack(side = LEFT, padx = 25, ipadx = 20, ipady = 5)
        self.buttonApply.pack(side = RIGHT, padx = 25, ipadx = 30, ipady = 5)
        self.canvas.pack(anchor = CENTER, padx = 25, pady = 100)
        self.autoCompletionClass = AutoCompletion(root,wordList,True,self.crcClass,5,50)
        self.autoCompletionResponsability = AutoCompletion(root,wordList,True,self.crcResponsability,5,50)
        self.autoCompletionColaborators = AutoCompletion(root,wordList,True,self.crcColaborators,5,50)
        
    def addToFields(self,crcList):
        for currentCrc in crcList.crc:
            self.tabTitle.append(currentCrc.name)
            self.tabResponsability.append(currentCrc.responsibility)
            self.tabColaborators.append(currentCrc.collaboration)
    
    def previous(self):
        if self.index > 0:
            self.index -= 1
            self.updateText()
    
    def next(self):
        if self.index == len(self.tabTitle):
            text = self.crcClass.get(1.0, END)
            self.tabTitle.append(text[:-1])
            text = self.crcResponsability.get(1.0, END) 
            self.tabResponsability.append(text[:-1])
            text = self.crcColaborators.get(1.0, END)
            self.tabColaborators.append(text[:-1])       
        else:
            text = self.crcClass.get(1.0, END)
            self.tabTitle[self.index] = text[:-1]
            text = self.crcResponsability.get(1.0, END)
            self.tabResponsability[self.index] = text[:-1]
            text = self.crcColaborators.get(1.0, END)
            self.tabColaborators[self.index] = text[:-1]
        self.index += 1
        if self.index == len(self.tabTitle):
            self.crcClass.delete(1.0, END)
            self.crcResponsability.delete(1.0, END)
            self.crcColaborators.delete(1.0, END)
        else:
            self.updateText()
          
    def updateText(self):
        try:
            self.crcClass.delete(1.0, END)
            self.crcResponsability.delete(1.0, END)
            self.crcColaborators.delete(1.0, END)
            self.crcClass.insert(1.0, self.tabTitle[self.index])
            self.crcResponsability.insert(1.0, self.tabResponsability[self.index])
            self.crcColaborators.insert(1.0, self.tabColaborators[self.index])
        except IndexError:
            pass
        
    def apply(self):
        self.next()
        self.crcList.crc=[]
        i = 0
        for title in self.tabTitle:
            self.crcList.crc.append(Crc(title,"",self.tabResponsability[i],self.tabColaborators[i]))
            i += 1
            
        textList = []
        for element in self.crcList.crc:
            textList.append(element.name)
            textList.append(element.responsibility)
            textList.append(element.collaboration)
            
        wordCheck = WordCheck(self.checkList, textList, self.root)
        status = wordCheck.activate()
        if status != None:
            self.canvas.destroy()
            if status:
                self.project.colorCRC = self.project.colorOk
            else:
                self.project.colorCRC= self.project.colorPending
            self.client.tryShowTreeView()
            
if __name__ == "__main__":
    root = Tk()
    crcList = CrcList()
    crcList.add(Crc("boris","gfdfdg","365543654fdg2","fdghgfdd3w54uzhgfd"))
    crcList.add(Crc("moris","gfdfdggfhgfh","365543g2","fdghgfdj659uzhgfd"))
    crcForm = CrcForm(root, "Formulaire de CRC", crcList)
    crcForm.top = Toplevel(root)
    root.wait_window(crcForm.top)