#-*- coding: iso-8859-1 -*-
import xmlrpclib
from Gui import *
from Projet import *

class Client:
    def __init__(self):
        self.vue = Gui(self)
        self.projetCourant = ""
    def connect(self,serv):
        self.serv = serv
        self.numClient = self.serv.connect()
        self.vue.mainMenu()
        self.vue.root.mainloop()
    def deconnect(self):
        self.serv.deconnect(self.numClient)
    def afficherMenu(self):
        self.vueMenu.afficherMenu()
    def newProject(self):
        self.vue.initProjet()
        self.vue.projetForm.tLevel.mainloop()
    def createProject(self,nomProject):
        self.projetCourant = Projet()
        self.projetCourant.texte = ""
        self.projetCourant.nomProjet = nomProject
        #self.projetCourant.motClasses.verbe = ""
        #self.projetCourant.motClasses.nom = ""
        #self.projetCourant.motClasses.adjectif = ""
    def saveProject(self):
        self.serv.save(self.projetCourant,self.nomProjet)
    def loadProject(self):
        self.projetCourant = self.serv.load(self.nomProjet)
    def editAnalyseTextuelle(self):
        self.form.analyse()      
    def loadTexte(self,texte):
        self.projetCourant.texte = texte

if __name__ == "__main__":
    s = xmlrpclib.ServerProxy('http://localhost:8006')
    c = Client()
    c.connect(s)
    c.deconnect()
    print c.numClient

    

