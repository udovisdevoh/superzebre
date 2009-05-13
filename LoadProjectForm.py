#-*- coding: iso-8859-1 -*-
from Tkinter import *

class LoadProjectForm:
    def __init__(self, root, title, projectList):
        self.root = root
        self.projectList = projectList
        self.selectedProjectName = None
        self.initGraphicComponents(root,title)
    
    def initGraphicComponents(self,root,title):
        self.canvas = Canvas(self.root, width = 800, height = 600)
        self.canvas.pack(anchor="nw")
        projectNameLabel = Label(self.canvas, text=title, font=("Helvetica", 17))
        projectNameLabel.pack(anchor="nw")
        self.listbox = Listbox(self.canvas)
        self.listbox.pack()
        for item in self.projectList:
            self.listbox.insert(END, item)
        buttonLoad = Button(self.canvas, text="Charger", command=self.userClickLoad)
        buttonLoad.pack()
    
    def clear(self):
        self.canvas.destroy()
    
    def userClickLoad(self):
        try:
            selection = self.listbox.curselection()[0]
            self.selectedProjectName = self.listbox.get(int(selection), int(selection) + 1)[0]
            print self.selectedProjectName
            #self.selectedProjectName = self.listbox[self.listbox.curselection()[0]]
        except IndexError:
            pass
    
if __name__ == "__main__":
    root = Tk()
    root.minsize(800, 600)
    projectList = []
    projectList.append("mofo")
    projectList.append("tata")
    projectList.append("foo")
    projectList.append("bar")
    loadProjectForm = LoadProjectForm(root,"Charger un projet",projectList)
    root.mainloop() 