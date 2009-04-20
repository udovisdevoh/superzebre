#-*- coding: iso-8859-1 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Gui import *
from Project import *
import xmlrpclib
import pickle

class Client:
    def __init__(self):
        self.server = xmlrpclib.ServerProxy('http://localhost:8006')
        self.gui = Gui(self)
        self.currentProject = None
        
    def start(self):
        self.gui.showMainMenu()
        self.gui.root.mainloop()
        
    def createNewProject(self,projectName):
        self.currentProject = Project(projectName)
        
    def loadProject(self,projectName):
        serializedProject = self.server.requestProjectLoad(projectName)
        if serializedProject == -1:
            #Project not found, create one
            self.createNewProject(projectName)
        else:
            self.currentProject = pickle.loads(serializedProject)
    
    def tryLoadTextFileIntoProject(self):
        if self.currentProject != None:
            self.currentProject.text = self.gui.getFileContentFromDialog("Ouvrir un fichier texte","Text file","*.txt")
        else:
            self.gui.loadProject()
            #self.gui.showMessage("Erreur","Vous devez charger ou créer un projet avant de charger le texte de l'analyse textuelle")

    def tryPerformTextAnalysis(self, howManyTry = 0):
        if self.currentProject != None and self.currentProject.text != None:
            text = self.currentProject.text
            sortedWords = self.currentProject.sortedWords
            self.currentProject.sortedWords = self.gui.getSortedWordsFromTextAnalysisForm(text, sortedWords)             
        elif self.currentProject != None and howManyTry == 0:
            self.tryLoadTextFileIntoProject()
            self.tryPerformTextAnalysis(1)
        elif self.currentProject != None and howManyTry == 1:
            self.gui.showMessage("Erreur","Vous devez charger le texte pour faire l'analyse textuelle")
        else:
            self.gui.loadProject()
            self.tryPerformTextAnalysis()
            #self.gui.showMessage("Erreur","Vous devez charger ou créer un projet avant de faire l'analyse textuelle")

    def saveCurrentProject(self):
        if self.currentProject != None:
            serializedProject = pickle.dumps(self.currentProject)
            self.server.sendProject(serializedProject)
        else:
            self.gui.showMessage("Erreur","Vous devez créer ou charger un projet pour le sauvegarder")

if __name__ == "__main__":
    print "Main program started"
    client = Client()
    client.start()