from Tkinter import *
from Project import *

class TreeView:
    def __init__(self,root,project):
        self.root = root
        self.project = project
    
    def show(self):
        self.root.minsize(800, 600)
        self.canvas = Canvas(root, width = 800, height = 600)
        self.canvas.pack(anchor="nw")
        self._showTitle(self.project.name)
        self._showSortedWords(self.project.sortedWords)
        self._showUseCaseList(self.project.useCaseList)
        
    def hide(self):
        self.canvas.destroy();
    
    def _showTitle(self,title):
        projectNameLabel = Label(self.canvas, text=title, font=("Helvetica", 17))
        projectNameLabel.pack(anchor="nw")
        
    def _showSortedWords(self,sortedWords):
        sortedWordsTitleLabel = Label(self.canvas, text="Analyse Textuelle", font=("Helvetica", 15), justify="left")
        sortedWordsTitleLabel.pack(anchor="nw", ipadx=30)         
        self.__showSortedWordsForCategory("Noms", sortedWords.noms)
        self.__showSortedWordsForCategory("Adjectifs", sortedWords.adjectifs)
        self.__showSortedWordsForCategory("Verbes", sortedWords.verbes)
        
    def __showSortedWordsForCategory(self,categoryName,wordList):
        categoryLabel = Label(self.canvas, text=categoryName, font=("Helvetica", 13), justify="left")
        categoryLabel.pack(anchor="nw", ipadx=60) 
        words=""
        for word in wordList:
            words += word + ", "
        if words=="":
            words="liste vide"
        wordLabel = Label(self.canvas, text = words, font=("Helvetica", 9), justify="left")
        wordLabel.pack(anchor="nw", ipadx=90)
    
    def _showUseCaseList(self,useCaseList):
        titleLabel = Label(self.canvas, text="Cas d'usage", font=("Helvetica", 15), justify="left")
        titleLabel.pack(anchor="nw", ipadx=30)
        for useCase in useCaseList.useCase:
            self.__showUseCase(useCase)
    
    def __showUseCase(self,useCase):
        titleLabel = Label(self.canvas, text=useCase.name, font=("Helvetica", 13), justify="left")
        titleLabel.pack(anchor="nw", ipadx=60)
        
        textLabel = Label(self.canvas, text=useCase.description, font=("Helvetica", 9), justify="left")
        textLabel.pack(anchor="nw", ipadx=90)
        
        pass
    
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
    treeView = TreeView(root, project)
    treeView.show()
    root.mainloop()
    