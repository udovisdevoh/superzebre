#-*- coding: iso-8859-1 -*-
from Tkinter import *

class AnalyseTextuelleForm:
    def __init__(self, parent, title):
        self.parent = parent
        self.master = parent.root
        self.master.title(title)
        self.frameTop = Frame(self.master)
        self.frameBouton= Frame(self.master)
        self.frameSaute = Frame(self.master)
        self.frameBottom = Frame(self.master)
        self.frameBoutonValide = Frame(self.master)
        
        self.verbe = Text(self.frameBottom,height=25,width=30)
        self.verbe.pack(side=LEFT)
        self.verbebar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.verbe.yview)
        self.verbebar.pack(side = LEFT , fill = Y)
        self.verbe.configure(yscrollcommand = self.verbebar.set)
        self.nom = Text(self.frameBottom,height=25,width=30)
        self.nom.pack(side=LEFT)
        self.nombar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.nom.yview)
        self.nombar.pack(side = LEFT , fill = Y)
        self.nom.configure(yscrollcommand = self.nombar.set)
        self.adj = Text(self.frameBottom,height=25,width=30)
        self.adj.pack(side=LEFT)
        self.adjbar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.adj.yview)
        self.adjbar.pack(side = LEFT , fill = Y)
        self.adj.configure(yscrollcommand = self.adjbar.set)
          
    
        self.button = Button(self.frameBoutonValide, text="QUIT", fg="red", command=self.frameBottom.quit)
        self.button.pack(side=RIGHT)
        
        self.frameTop.pack(side=TOP,pady=40)
        self.frameSaute.pack(side = TOP)
        self.frameBouton.pack(side = TOP,pady = 10)
        self.frameBottom.pack(side = TOP,padx = 10)
        self.frameBoutonValide.pack(side = TOP , pady = 15)
        
         
        self.bVerbe = Button(self.frameBouton,text="Verbes",width=36,command=self.addVerbe)
        self.bNom = Button(self.frameBouton,text="Noms",width=36,command=self.addNom)
        self.bAdj = Button(self.frameBouton,text="Adjectifs",width=36,command=self.addAdj)
        self.bSaute= Button(self.frameSaute,text="Sauter un mot",width=36)
        
        self.texte = Text(self.frameTop,height=10)
        self.texte.insert(END, self.parent.parent.projetCourant.texte)
        self.texte.pack(side=LEFT)
        self.textebar = Scrollbar(self.frameTop, orient=VERTICAL , command=self.texte.yview)
        self.textebar.pack(side = LEFT , fill = Y)
        self.texte.configure(yscrollcommand = self.textebar.set,state=DISABLED)
           
        self.bVerbe.pack(side = LEFT,) 
        self.bNom.pack(side = LEFT) 
        self.bAdj.pack(side = LEFT)
        
        self.bSaute.pack(side=BOTTOM,anchor=W)
    
    def addVerbe(self):
        verbe = self.texte.get("sel.first", "sel.last")
        self.verbe.insert(END, verbe+"\n")
        self.parent.parent.ajouterMots(verbe,2)
    def addNom(self):
        nom = self.texte.get("sel.first", "sel.last")
        self.nom.insert(END, nom+"\n")
        self.parent.parent.ajouterMots(nom,1)
    def addAdj(self):
        adj = self.texte.get("sel.first", "sel.last")
        self.adj.insert(END, adj+"\n")
        self.parent.parent.ajouterMots(adj,3)       



    
if __name__=="__main__":
    from Client import *
    from Gui import *
    c = Client()
    c.projetCourant=Projet()
    c.projetCourant.texte = "kev stun gros debile"
    c.vue.imgLabel.destroy()
    c.vue.test = AnalyseTextuelleForm(c.vue,"test")      
    c.vue.test.master.mainloop()