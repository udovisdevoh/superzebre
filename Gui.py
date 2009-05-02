#-*- coding: iso-8859-1 -*-
import sys
from Client import * 
from Tkinter import *
from TextForm import *
from FileForm import *
from TextAnalysisForm import *
from UseCaseForm import *
from CrcForm import *

class Gui:
    def __init__(self, parentClient):
        self.parentClient = parentClient
        self.root = Tk()
        self.root.minsize(800,600)
        self.root.title("SuperZèbre")
        #self.showImage()
            
    def showMainMenu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.createNewProject)
        filemenu.add_command(label="Load...", command=self.loadProject)
        filemenu.add_command(label="Save", command=self.saveCurrentProject)
        filemenu.add_command(label="Importer un texte", command=self.loadText)
        filemenu.add_command(label="Faire/Modifier analyse textuelle", command=self.tryBeginPerformTextAnalysis)
        filemenu.add_command(label="Modifier les cas d'usage", command=self.tryEditUseCases)
        filemenu.add_command(label="Modifier les CRCs", command=self.tryEditCrcs)
        filemenu.add_command(label="SCRUM", command=self.tryEditScrums)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=sys.exit)
        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.showAboutWindow)
    
    def showImage(self):
        self.img = PhotoImage(file = "zebre.gif")
        self.imgLabel = Label(self.root,image=self.img)
        self.imgLabel.pack(side = TOP)
        
    def createNewProject(self):
        projectName = self.getInputDialog("Project name:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.createNewProject(projectName)
    
    def loadProject(self):
        projectName = self.getInputDialog("Project name:")
        if projectName.strip() == "":
            self.showMessage("Erreur","Vous devez entrer un nom valide")
            return
        self.parentClient.loadProject(projectName)
    
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
        self.showMessage("About","Fait par:\n\t-Guillaume Lacasse\n\t-Étienne-Joseph Charles\n\t-Frédérik Pion\n\t-François Pelletier\n\t-Kevin Melançon\n\n\tCopyright 2009\n")
        
    def showMessage(self,title,text):
        messageBox = Toplevel(self.root)
        messageBox.title(title)
        msg = Message(messageBox, text=text,width=300)
        msg.pack()
        button = Button(messageBox, text = "Fermer", command=messageBox.destroy)
        button.pack()
        
    def getSortedWordsFromTextAnalysisForm(self, text, sortedWords):
        textAnalysisForm = TextAnalysisForm(self.root, "Analyse Textuelle", text, sortedWords)
        return textAnalysisForm.sortedWords
    
    def getUseCaseListFromUseCaseForm(self,useCaseList):
        useCaseForm = UseCaseForm(self.root, "Cas d'usage", useCaseList)
        return useCaseForm.useCaseList
    
    def getCrcListFromCrcForm(self,crcList):
        crcForm = CrcForm(self.root,"CRC",crcList)
        return crcForm.crcList
    
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