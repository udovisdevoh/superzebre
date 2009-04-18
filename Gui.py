#-*- coding: iso-8859-1 -*-
import sys
from Tkinter import *
from ProjetForm import *
from FileForm import *
from AnalyseTextuelleForm import *

class Gui(object):
    def __init__(self, parent):
        self.parent = parent
        self.projetActif = ""
        self.root = Tk()
        self.root.title("SuperZèbre")
        self.mainMenu()
        self.addImage()
        
    def addImage(self):
        self.img = PhotoImage(file = "zebre.gif")
        self.imgLabel = Label(self.root,image=self.img)
        self.imgLabel.pack(side = TOP)
    
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
        self.imgLabel.destroy()
        self.parent.analyseTexte.motsClasses.verbes = self.parent.projetCourant.motsClasses.verbes[:]
        self.parent.analyseTexte.motsClasses.noms = self.parent.projetCourant.motsClasses.noms[:]
        self.parent.analyseTexte.motsClasses.adjectifs = self.parent.projetCourant.motsClasses.adjectifs[:]
        self.analyseTextuelleForm = AnalyseTextuelleForm(self, "SuperZèbre-Analyse Textuelle")
    def importText(self):
        self.fileForm = FileForm(self,"Importer un texte")
    def load(self):
        self.projetForm = ProjetForm(self,'l',"Récupération de projet","Veuillez entrer le nom du Projet : ")    
    def save(self):
        self.parent.saveProject()
    
    def new(self):
        self.projetForm = ProjetForm(self,'c',"Creation de projet","Veuillez entrer le nom de votre Projet : ")    
    def quit(self):
        sys.exit()
    def message(self,title,text):
        mes= Toplevel(self.root)
        mes.title(title)
        msg = Message(mes, text=text, width=600,padx = 50, pady=20)   
        msg.pack()
        button = Button(mes, text = "Ok", command=mes.destroy,width = 10)
        button.pack()   
if __name__ == "__main__":
    from Client import *
    from Gui import *
    c = Client()
    c.vue.mainMenu()
    c.vue.root.mainloop()
    