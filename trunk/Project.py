#-*- coding: iso-8859-1 -*-
from SortedWords import *
from UseCaseList import *
class Project:
    def __init__(self,name):
        self.name = name
        self.sortedWords = SortedWords()
        self.useCase = UseCaseList()
        self.text = None
        