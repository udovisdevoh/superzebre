#-*- coding: iso-8859-1 -*-
from MotsClasses import *

class AnalyseTextuelle(object):

    def __init__(self):
        self.vue = AnalyseTextuelleForm()
        self.motsClasses = MotsClasses()

    def getMotsClasses(self):
        return motsClasses

    def classerMot(self, mot, genre):     
        if genre == 1:
            motsClasses.ajouterNom(mot)
        elif genre == 2:
            motsClasses.ajouterVerbe(mot)
        elif genre == 3:
            motsClasses.ajouterAdjectif(mot)
        else:
            print "Erreur lors du classement du mot, genre erron�"
            
               
if __name__ == "__main__":
    analyse = AnalyseTextuelle()
