#-*- coding: iso-8859-1 -*-

class MotsClasses(object):

    def __init__(self):
        self.noms=[]
        self.verbes=[]
        self.adjectifs=[]

    def ajouterNom(self, nom):
        self.noms.append(nom)

    def ajouterVerbe(self, ver):
        self.verbes.append(ver)

    def ajouterAdjectif(self, adj):
        self.adjectifs.append(adj)
