#-*- coding: iso-8859-1 -*-
class SortedWords:
    def __init__(self):
        self.noms=[]
        self.verbes=[]
        self.adjectifs=[]
        
    def setWordsTypes(self,verbList,nounList,adjList):
        self.noms = nounList
        self.adjectifs = adjList
        self.verbes = verbList