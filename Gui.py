#-*- coding: iso-8859-1 -*-
import sys
from Client import * 
from Tkinter import *
from TextForm import *
from FileForm import *
from TextAnalysisForm import *
from UseCaseForm import *

class Gui:
    def __init__(self, parentClient):
        self.parentClient = parentClient
        self.root = Tk()
        self.root.minsize(800,600)
        self.root.title("SuperZèbre")
        
    def showMainMenu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        filemenu = Menu(self.menu , tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouveau", command=self.createNewProject)
        filemenu.add_command(label="Charger", command=self.loadProject)
        filemenu.add_command(label="Enregistrer", command=self.saveCurrentProject)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=sys.exit)
        
        editmenu = Menu(self.menu , tearoff=0)
        self.menu.add_cascade(label="Modifier", menu=editmenu)
        editmenu.add_command(label="Importer un texte", command=self.loadText)
        editmenu.add_command(label="Faire/Modifier l'analyse textuelle", command=self.tryBeginPerformTextAnalysis)
        editmenu.add_command(label="Faire/Modifier les cas d'usages", command=self.tryBeginPerformUseCase)

        helpmenu = Menu(self.menu , tearoff=0)
        self.menu.add_cascade(label="Aide", menu=helpmenu)
        helpmenu.add_command(label="À propos...", command=self.showAboutWindow)
        
        self.menu.entryconfig(2,state = DISABLED)
    
    def createNewProject(self):
        projectName = self.getInputDialog("Project name:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.createNewProject(projectName)
        self.menu.entryconfig(2,state = ACTIVE)
        self.root.title("SuperZèbre - " + projectName)

    
    def loadProject(self):
        projectName = self.getInputDialog("Project name:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.loadProject(projectName)
        self.menu.entryconfig(2,state = ACTIVE)
        self.root.title("SuperZèbre - " + projectName)

    
    def saveCurrentProject(self):
        self.parentClient.saveCurrentProject()
    
    def loadText(self):
        self.parentClient.tryLoadTextFileIntoProject()
    
    def tryBeginPerformTextAnalysis(self):
        self.parentClient.tryPerformTextAnalysis()
        
    def tryBeginPerformUseCase(self):
        self.parentClient.tryPerformUseCase()
    
    def showAboutWindow(self):
        self.showMessage("À propos","Fait par:\n\t-Guillaume Lacasse\n\t-Étienne-Joseph Charles\n\t-Frédérik Pion\n\t-François Pelletier\n\t-Kevin Melançon\n\n\tCopyright 2009\n")
        
    def showMessage(self,title,text):
        messageBox = Toplevel(self.root)
        messageBox.title(title)
        msg = Message(messageBox, text=text,width=300)
        msg.pack()
        button = Button(messageBox, text = "Fermer", command=messageBox.destroy)
        button.pack()
        
    def getSortedWordsFromTextAnalysisForm(self, projectName, text, sortedWords):
        textAnalysisForm = TextAnalysisForm(self.root, "Analyse Textuelle - "+projectName, text, sortedWords)
        return textAnalysisForm.sortedWords
    
    def getUseCaseFromUseCaseForm(self, projectName, useCaseTab):
        useCaseForm = UseCaseForm(self.root , "Cas D'Usage - "+projectName,useCaseTab)
        return useCaseForm.useCaseTab
    
    def getInputDialog(self,message):
        textForm = TextForm(self.root,message)
        self.root.wait_window(textForm.top)
        return textForm.outputValue
        
    def getFileContentFromDialog(self,title,fileType,fileExtension):
        fileForm = FileForm(self.root,title,fileType,fileExtension)
        try:
            return fileForm.fileContent
        except AttributeError:
            return None
        
if __name__ == "__main__":
    print "Testing the GUI..."
    gui = Gui(None)
    gui.showMainMenu()
    gui.root.mainloop()