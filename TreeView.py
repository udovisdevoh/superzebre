from Tkinter import *
from Project import *

class TreeView:
    def __init__(self,root,project):
        self.root = root
        self.project = project
    
    def show(self):
        self.root.minsize(800, 600)
        self.showTitle(self.project.name)
        self.showSortedWords(self.project.sortedWords)
    
    def showTitle(self,title):
        projectNameLabel = Label(self.root, text=title, font=("Helvetica", 16))
        projectNameLabel.pack();
        
    def showSortedWords(self,sortedWords):
        pass
    
if __name__ == "__main__":
    root = Tk()
    project = Project("Dummy project")
    treeView = TreeView(root, project)
    treeView.show()
    root.mainloop()
    