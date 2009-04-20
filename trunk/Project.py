#-*- coding: iso-8859-1 -*-
from SortedWords import *
class Project:
    def __init__(self,name):
        self.name = name
        self.sortedWords = SortedWords()
        self.text = None