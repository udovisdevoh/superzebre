#-*- coding: iso-8859-1 -*-
from Tkinter import *
from Client import *
from Gui import *
import tkFileDialog

class FileForm:
    def __init__(self,root,title,fileType,fileExtension):
        #self.file = tkFileDialog.askopenfile(parent = root,filetypes=[(fileType,fileExtension)],initialdir="c:\\",mode='rb',title=title)
        self.file = tkFileDialog.askopenfile(parent = root,filetypes=[(fileType,fileExtension)],mode='rb',title=title)
        self.file.iconbitmap("zebra.ico")
        if self.file != None:
            self.fileContent = self.file.read()
            self.fileContent = str(self.fileContent)
            self.fileContent = self.fileContent.replace("\r"," ")
            self.fileContent = self.fileContent.replace("\n"," ")
            self.fileContent = self.fileContent.replace("\t"," ")
            
            while self.fileContent.find("  ") != -1:
                self.fileContent = self.fileContent.replace("  "," ")
            
            self.file.close()
            
if __name__ == "__main__":
    root = Tk()
    fileForm = FileForm(root,"File input","Fichier texte","*.txt")
    print fileForm.fileContent