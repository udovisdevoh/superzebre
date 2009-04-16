#-*- coding: iso-8859-1 -*-
from Tkinter import *
import tkFileDialog

class FileForm:
    def __init__(self,master,title):
        self.master = master
        self.file = tkFileDialog.askopenfile(parent = master.root,filetypes=[("Text file","*.txt")],initialdir="c:\\",mode='rb',title=title)
        if self.file != None:
            texte = self.file.read()
            self.file.close()
            if title == "test":
                print texte
            else:
                self.master.parent.loadTexte(texte)
if __name__=="__main__":
    from Client import *
    from Gui import *
    c = Client()
    c.vue.test = FileForm(c.vue,"test")