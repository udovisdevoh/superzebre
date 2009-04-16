#-*- coding: iso-8859-1 -*-
from Tkinter import *
#avant appeler Création ProjetForm
class ProjetForm:
    #J'ai rajouter self au variable pour qu'il appartienne a l'object de la classe
    #pour pouvoir les appeller du controleur
    def __init__(self, master,type,title,texte):
        #rajouter le parent pour que le bouton puisse appeler le controleur
        self.master = master 
        # va chercher le root du parent
        self.tLevel = Toplevel(self.master.root)
        self.tLevel.title(title)
      # tLevel.resizable(width = False, height = False)
      
        self.l1 = Label(self.tLevel,text=texte)
        self.l1.pack(anchor=W, padx = 3)
        self.nom = Entry(self.tLevel,width=50)
        self.nom.pack(anchor=CENTER, padx = 3, pady = 10)
        #changer la méthode pour destroy pour que le toplevel arrete
        self.Cancel= Button(self.tLevel, text="Cancel", fg="red", command=self.tLevel.destroy)
        self.Cancel.pack(side=LEFT)
        #ne passe rien en parametre parceque la commande n'est pas supposer avoir de ()
        self.Ok = Button(self.tLevel, text="OK", command=self.selectionOK)
        self.Ok.pack(side=RIGHT)
        
        
    def selectionOK(self):
        #va chercher le texte pour le mettre dans la variable
        leNom = self.nom.get()
        #vérifie que le nom de projet ne sois pas vide
        if leNom != "":
            if type == "create": 
                #appelle la méthode du controleur pour créer un nouveau projet
                self.master.parent.createProject(leNom)
            if type == "load":
                #appelle la méthode du controleur pour loader un projet
                self.master.parent.loadProject(leNom) 
            #ferme le topLevel
            self.tLevel.destroy()

#Ajouter la commende suivant pour que le reste ne s'exécute pas si se n'est pas le main
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
