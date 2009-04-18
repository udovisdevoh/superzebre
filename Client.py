#-*- coding: iso-8859-1 -*-
import xmlrpclib
from Gui import *
from Projet import *
from AnalyseTextuelle import *

class Client:
    def __init__(self):
        self.vue = Gui(self)
        self.projetCourant = ""
        self.analyseTexte = AnalyseTextuelle()
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
        self.vue.message("Projet " + nomProject,"Le projet "+ nomProject +" a bien �t� cr�er")
    def saveProject(self):
        self.serv.save(self.projetCourant,self.nomProjet)
    def loadProject(self):
        self.projetCourant = self.serv.load(self.nomProjet)
    def editAnalyseTextuelle(self):
        tmp = self.analyseTexte.getMotsClasses()
        self.projetCourant.motsClasses.noms =tmp.noms[:]
        self.projetCourant.motsClasses.verbes =tmp.verbes[:]
        self.projetCourant.motsClasses.adjectifs =tmp.adjectifs[:]      
    def loadTexte(self,texte):
        self.projetCourant.texte = texte
        self.vue.message("Projet " + self.projetCourant.nomProjet,"Le texte a bien �t� charger sur le projet")
    def ajouterMots(self,mot,type):
        self.analyseTexte.classerMot(mot,type)
if __name__ == "__main__":
    s = xmlrpclib.ServerProxy('http://localhost:8006')
    c = Client()
    c.connect(s)
    c.deconnect()
    print c.numClient

    

