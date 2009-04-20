#-*- coding: iso-8859-1 -*-
from Tkinter import *

class UseCaseForm(object):
    def __init__(self, root, title):
        self.initGraphicsComponents(root, title)
        
    def initGraphicsComponents(self, root, title):
        root.minsize(800,600)
        root.title(title)
        self.canvas = Canvas(root, width = 800, height = 600)
        self.frame = Frame(self.canvas)
        self.useCaseTitle = Text(self.frame, width = 50, height = 1)
        self.useCaseDefinition = Text(self.frame, height = 10)
        self.buttonApply = Button(self.frame, text = "Valider")
        self.scrollCanvas = Scrollbar(root, orient = VERTICAL, command = self.canvas.yview)
        self.canvas.config(scrollregion = self.canvas.bbox("all"))
        self.canvas.create_window(0, 0, window = self.frame)
        self.packGrapihics()
        
    def packGrapihics(self):
        self.useCaseTitle.pack(side=TOP, pady = 10, anchor = W)
        self.useCaseDefinition.pack(side=TOP, padx = 5, pady = 5)
        self.scrollCanvas.pack(side = RIGHT, fill = Y)
        self.frame.pack()
        self.canvas.pack()
        self.buttonApply.pack(anchor = E)
        
if __name__ == "__main__":
    root = Tk()
    useCaseForm = UseCaseForm(root, "test")
    useCaseForm.top = Toplevel(root)
    root.wait_window(useCaseForm.top)
        