#-*- coding: iso-8859-1 -*-
from Tkinter import *

class LoadProjectForm:
    def __init__(self, root, title, projectList, resultFunctionPointer):
        self.root = root
        self.projectList = projectList
        self.selectedProjectName = None
        self.initGraphicComponents(root,title)
        self.resultFunctionPointer = resultFunctionPointer
    
    def initGraphicComponents(self,root,title):
        for component in root.pack_slaves():
            component.destroy()
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
        
        self.listbox.bind("<Double-1>", self.doubleClick)
    
    def clear(self):
        self.canvas.destroy()
    
    def doubleClick(self, event):
        self.userClickLoad()
    
    def userClickLoad(self):
        try:
            selection = self.listbox.curselection()[0]
            self.selectedProjectName = self.listbox.get(int(selection), int(selection) + 1)[0]
            #self.selectedProjectName = self.listbox[self.listbox.curselection()[0]]
            self.resultFunctionPointer(self.selectedProjectName)
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