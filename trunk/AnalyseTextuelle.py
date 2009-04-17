#-*- coding: iso-8859-1 -*-
from MotsClasses import *

class AnalyseTextuelle(object):

    def __init__(self):
        self.motsClasses = MotsClasses()

    def getMotsClasses(self):
        return self.motsClasses

    def classerMot(self, mot, genre):     
        if genre == 1:
            self.motsClasses.ajouterNom(mot)
        elif genre == 2:
            self.motsClasses.ajouterVerbe(mot)
        elif genre == 3:
            self.motsClasses.ajouterAdjectif(mot)
        else:
            print "Erreur lors du classement du mot, genre erroné"
            
               
if __name__ == "__main__":
    analyse = AnalyseTextuelle()
