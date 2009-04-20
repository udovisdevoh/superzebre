#-*- coding: iso-8859-1 -*-
from Tkinter import *

class UseCaseForm(object):
    def __init__(self, root, title):
        self.initGraphicsComponents(root, title)
        
    def initGraphicsComponents(self, root, title):
        root.minsize(800, 600)
        root.maxsize(800, 600)
        root.title(title)
        self.buttonApply = Button(root, text = "Valider", command = self.drawFrame)
        self.buttonApply.pack(anchor = E)
        self.scrollCanvas = Scrollbar(root, orient = VERTICAL)
        self.canvas = Canvas(root, width = 800, height = 600, yscrollcommand = self.scrollCanvas.set)
        self.scrollCanvas.config(command = self.canvas.yview)
        self.scrollCanvas.pack(side = RIGHT, fill = Y)
        self.mainFrame = Frame(self.canvas)
        self.mainFrame.pack()
        self.drawFrame()
        self.canvas.create_window(0, 0, window = self.mainFrame)
        self.canvas.config(scrollregion = self.canvas.bbox("all"))
        self.mainFrame.update_idletasks()
        self.canvas.pack()
        
    def drawFrame(self):
        frame = Frame(self.mainFrame)
        useCaseTitle = Text(frame, width = 50, height = 1)
        useCaseDefinition = Text(frame, height = 10)
        useCaseTitle.pack(side=TOP, pady = 10, anchor = W)
        useCaseDefinition.pack(side=TOP, padx = 5, pady = 5)
        frame.pack()
        self.mainFrame.update_idletasks()
        
if __name__ == "__main__":
    root = Tk()
    useCaseForm = UseCaseForm(root, "test")
    useCaseForm.top = Toplevel(root)
    root.wait_window(useCaseForm.top)
        