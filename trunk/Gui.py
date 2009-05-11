#-*- coding: iso-8859-1 -*-
import sys
from Client import * 
from Tkinter import *
from TextForm import *
from FileForm import *
from TextAnalysisForm import *
from UseCaseForm import *
from CrcForm import *
from TreeView import *
from ScrumForm import *

class Gui:
    def __init__(self, parentClient):
        self.parentClient = parentClient
        self.root = Tk()
        self.root.minsize(800,600)
        self.root.title("SuperZèbre")
        self.root.iconbitmap("zebra.ico")
        self.showImage()
            
    def showMainMenu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        filemenu = Menu(self.menu,tearoff=0)
        editmenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=filemenu)
        self.menu.add_cascade(label="Édition", menu=editmenu)
        filemenu.add_command(label="Nouveau Projet", command=self.createNewProject)
        filemenu.add_command(label="Charger un Projet", command=self.loadProject)
        filemenu.add_command(label="Enregistrer un Projet", command=self.saveCurrentProject)
        editmenu.add_command(label="Importer un texte", command=self.loadText)
        editmenu.add_command(label="Faire/Modifier l'analyse textuelle", command=self.tryBeginPerformTextAnalysis)
        editmenu.add_command(label="Faire/Modifier les cas d'usage", command=self.tryEditUseCases)
        editmenu.add_command(label="Faire/Modifier les CRCs", command=self.tryEditCrcs)
        editmenu.add_command(label="Faire/Modifier les SCRUM", command=self.tryEditScrums)
        editmenu.add_command(label="Afficher l'information sur le projet", command=self.tryShowTreeView)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=sys.exit)
        helpmenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Aide", menu=helpmenu)
        helpmenu.add_command(label="À Propos...", command=self.showAboutWindow)
    
    def showImage(self):
        self.img = PhotoImage(file = "zebre2.gif")
        self.imgLabel = Label(self.root,image=self.img)
        self.imgLabel.pack(side = TOP)
    
    def tryShowTreeView(self):
        self.parentClient.tryShowTreeView()

    def createNewProject(self):
        projectName = self.getInputDialog("Nom du Projet:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.createNewProject(projectName)
        self.root.title("SuperZèbre - "+projectName)
    
    def loadProject(self):
        projectName = self.getInputDialog("Nom du Projet:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.loadProject(projectName)
        self.root.title("SuperZèbre - "+projectName)
        self.tryShowTreeView()
    
    def saveCurrentProject(self):
        self.parentClient.saveCurrentProject()
    
    def loadText(self):
        self.parentClient.tryLoadTextFileIntoProject()
    
    def tryBeginPerformTextAnalysis(self):
        self.parentClient.tryPerformTextAnalysis()
    
    def tryEditUseCases(self):
        self.parentClient.tryEditUseCases()
        
    def tryEditCrcs(self):
        self.parentClient.tryEditCrcs()
        
    def tryEditScrums(self):
        self.parentClient.tryEditScrums()
    
    def showAboutWindow(self):
        self.showMessage("À propos","Fait par:\n\t-Guillaume Lacasse\n\t-Étienne-Joseph Charles\n\t-Frédérik Pion\n\t-François Pelletier\n\t-Kevin Melançon\n\n\tCopyright 2009\n")
    
    def showTreeView(self,project):
        treeView = TreeView(self.root, project)
        treeView.show()    
    
    def showMessage(self,title,text):
        try:
            messageBox = Toplevel(self.root)
            messageBox.title(title)
            messageBox.iconbitmap("zebra.ico")
            msg = Message(messageBox, text=text,width=300)
            msg.pack()
            button = Button(messageBox, text = "Fermer", command=messageBox.destroy)
            button.pack()
        except TclError:
            pass
        
    def getSortedWordsFromTextAnalysisForm(self, projectName, text, sortedWords):
        textAnalysisForm = TextAnalysisForm(self.root, "Analyse Textuelle - "+projectName, text, sortedWords)
        return textAnalysisForm.sortedWords
    
    def getUseCaseListFromUseCaseForm(self,projectName,useCaseList,sortedWords):
        useCaseForm = UseCaseForm(self.root, "Cas d'usage - "+projectName, useCaseList,sortedWords)
        return useCaseForm.useCaseList
    
    def getCrcListFromCrcForm(self,projectName,crcList,sortedWords):
        crcForm = CrcForm(self.root,"CRC - "+projectName,crcList,sortedWords)
        return crcForm.crcList
    
    def getScrumListFromScrumForm(self,projectName,scrumList):
        scrumForm = ScrumForm(self.root,"SCRUMS - "+projectName,scrumList)
        return scrumForm.scrumList
        
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