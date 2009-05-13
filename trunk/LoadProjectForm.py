#-*- coding: iso-8859-1 -*-
from Tkinter import *

class LoadProjectForm:
    def __init__(self, root, title, projectList):
        self.root = root
        self.projectList = projectList
        pass
    
if __name__ == "__main__":
    root = Tk()
    root.minsize(800, 600)
    projectList = []
    projectList.append("mofo")
    projectList.append("tata")
    projectList.append("foo")
    projectList.append("bar")
    loadProjectForm = LoadProjectForm(root,"test",projectList)
    root.mainloop() 