#-*- coding: iso-8859-1 -*-
import sys
from Tkinter import *

class Gui(object):
    def __init__(self, parent):
        self.parent = parent
        self.projetActif = ""
        self.root = Tk()
        self.root.title("SuperZèbre")
        self.mainMenu()
        #self.addImage()
        
    def addImage(self):
        img = PhotoImage(file = "zebre.gif")
        imgLabel = Label(self.root,image=img)
        imgLabel.pack()
    
    def mainMenu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Load...", command=self.load)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Importer un texte", command=self.importText)
        filemenu.add_command(label="Modifier une Analyse", command=self.edit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.help)
    
    def help(self):
        about = Toplevel(self.root)
        about.title("About")

        msg = Message(about, text="Fait par:\n\t-Guillaume Lacasse\n\t-Étienne-Joseph Charles\n\t-Frédérik Pion\n\t-François Pelletier\n\t-Kevin Melançon\n\n\tCopyright 2009\n",width=300)
        msg.pack()
        
        button = Button(about, text = "Fermer", command=about.destroy)
        button.pack()
		
	def edit(self):
		self.parent.editAnalyseTextuelle()
    
	def importText(self):
		self.parent.loadText()
	
    def load(self):
        self.parent.loadProject()
    
    def save(self):
        self.parent.saveProject()
    
    def new(self):
        self.parent.createProject()
    
    def quit(self):
        sys.exit()
        
if __name__ == "__main__":
    g = GUI()
    g.root.mainloop()
    