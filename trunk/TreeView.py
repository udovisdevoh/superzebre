#-*- coding: iso-8859-1 -*-
from Tkinter import *
from Project import *

class TreeView:
    def __init__(self,root,project, parentClient=""):
        self.root = root
        self.textSizeH1 = 14
        self.textSizeH2 = 13
        self.textSizeH3 = 9
        self.textSizeH4 = 8
        self.project = project
        self.parentClient = parentClient
        self.colorOk = "#0F0"
        self.colorPending = "#FF0"
        self.colorNotOk = "#F00"
    
    def show(self):
        for i in self.root.pack_slaves():
            i.destroy()
        self.root.minsize(800, 600)
        self.canvas = Canvas(self.root, width = 800, height = 600)
        self.canvas.pack(anchor="nw")
        self._showTitle(self.project.name)
        self._showSortedWords(self.project.sortedWords)
        self._showUseCaseList(self.project.useCaseList)
        self._showCrcList(self.project.crcList)
        self._showScrumList(self.project.scrumList)
        
    def hide(self):
        self.canvas.destroy();
    
    def _showTitle(self,title):
        projectNameLabel = Label(self.canvas, text=title, font=("Helvetica", self.textSizeH1))
        projectNameLabel.pack(anchor="nw")
        
    def _showSortedWords(self,sortedWords):
        if sortedWords == None:
            color = self.colorNotOk
        elif len(sortedWords.noms) < 4 or len(sortedWords.adjectifs) < 4 or len(sortedWords.verbes) < 4:
            color = self.colorPending
        else:
            color = self.colorOk
        buttonSortedWordsTitle = Button(self.canvas, text="Analyse Textuelle", font=("Helvetica", self.textSizeH2), justify="left", command=self.tryBeginPerformTextAnalysis, background=color)
        buttonSortedWordsTitle.pack(anchor="nw", padx=30)         
        self.__showSortedWordsForCategory("Noms", sortedWords.noms)
        self.__showSortedWordsForCategory("Adjectifs", sortedWords.adjectifs)
        self.__showSortedWordsForCategory("Verbes", sortedWords.verbes)
        
    def __showSortedWordsForCategory(self,categoryName,wordList):
        labelCategory = Label(self.canvas, text=categoryName, font=("Helvetica", self.textSizeH3), justify="left")
        labelCategory.pack(anchor="nw", padx=60) 
        words=""
        for word in wordList:
            words += word + ", "
        if words=="":
            words="liste vide"
        labelWord = Label(self.canvas, text = words, font=("Helvetica", self.textSizeH4), justify="left")
        labelWord.pack(anchor="nw", padx=90)
    
    def _showUseCaseList(self,useCaseList):
        if useCaseList == None:
            color = self.colorNotOk
        elif len(useCaseList.useCase) < 4:
            color = self.colorPending
        else:
            color = self.colorOk
        buttonTitle = Button(self.canvas, text="Cas d'usage", font=("Helvetica", self.textSizeH2), justify="left", command=self.tryEditUseCases, background=color)
        buttonTitle.pack(anchor="nw", padx=30)
        for useCase in useCaseList.useCase:
            self.__showUseCase(useCase)
    
    def __showUseCase(self,useCase):
        labelTitle = Label(self.canvas, text=useCase.name, font=("Helvetica", self.textSizeH3), justify="left")
        labelTitle.pack(anchor="nw", padx=60)
        labelText = Label(self.canvas, text=useCase.description, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)
    
    def _showScrumList(self,scrumList):
        if scrumList == None:
            color = self.colorNotOk
        elif len(scrumList.scrum) < 4:
            color = self.colorPending
        else:
            color = self.colorOk 
        buttonTitle = Button(self.canvas, text="Scrums", font=("Helvetica", self.textSizeH2), justify="left", command=self.tryEditScrum, background=color)
        buttonTitle.pack(anchor="nw", padx=30)
        for scrum in scrumList.scrum:
            self.__showScrum(scrum)
            
    def __showScrum(self, scrum):
        labelTitle = Label(self.canvas, text=scrum.date + ": " + scrum.user, font=("Helvetica", self.textSizeH3), justify="left")
        labelTitle.pack(anchor="nw", padx=60)
        labelText = Label(self.canvas, text=scrum.todo, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)
        labelText = Label(self.canvas, text=scrum.done, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)
        labelText = Label(self.canvas, text=scrum.problem, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)
        
    def _showCrcList(self,crcList):
        if crcList == None:
            color = self.colorNotOk
        elif len(crcList.crc) < 4:
            color = self.colorPending
        else:
            color = self.colorOk            
        buttonTitle = Button(self.canvas, text="CRCs", font=("Helvetica", self.textSizeH2), justify="left", command=self.tryEditCrcs, background=color)
        buttonTitle.pack(anchor="nw", padx=30)
        for crc in crcList.crc:
            self.__showCrc(crc)
    
    def __showCrc(self,crc):
        labelTitle = Label(self.canvas, text=crc.name, font=("Helvetica", self.textSizeH3), justify="left")
        labelTitle.pack(anchor="nw", padx=60)
        labelText = Label(self.canvas, text="Personne ressource: " + crc.ownerName, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)
        labelText = Label(self.canvas, text="Responsabilités: " + crc.responsibility, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90)        
        labelText = Label(self.canvas, text="Collaborations: " + crc.collaboration, font=("Helvetica", self.textSizeH4), justify="left")
        labelText.pack(anchor="nw", padx=90) 
        
    def  tryBeginPerformTextAnalysis(self):
        self.parentClient.tryPerformTextAnalysis()
    
    def tryEditUseCases(self):
        self.parentClient.tryEditUseCases()
    
    def foundUseCase(self):
        pass
    
    def tryEditScrum(self):
        self.parentClient.tryEditScrums()
    
    def foundScrum(self):
        pass
    
    def tryEditCrcs(self):
        self.parentClient.tryEditCrcs()

if __name__ == "__main__":
    root = Tk()
    project = Project("Dummy project")
    project.sortedWords.noms = []
    project.sortedWords.adjectifs = []
    project.sortedWords.verbes = []
    project.sortedWords.noms.append("gfdgfd")
    project.sortedWords.noms.append("gfdgf536trhd")
    project.sortedWords.adjectifs.append("gfdgfd")
    project.sortedWords.adjectifs.append("gfdgf536trhd")
    project.sortedWords.verbes.append("gfdgfd")
    project.sortedWords.verbes.append("gfdgf536trhd")
    project.useCaseList.add(UseCase("Lancer du nain","On lance le nain"))
    project.useCaseList.add(UseCase("Lancer du trefle","On lance le trefle"))    
    project.scrumList.scrum.append(Scrum("2009-01-02","Boris","Faire du café","Café fait","Il n'en restait plus"))
    project.crcList.crc.append(Crc("Tableau","Marcel","Contenir les cases","Case"))
    treeView = TreeView(root, project)
    treeView.show()
    root.mainloop()