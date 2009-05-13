#-*- coding: iso-8859-1 -*-
from SortedWords import *
from CrcList import *
from ScrumList import *
from UseCaseList import *

class Project:
    def __init__(self,name):
        self.name = name
        self.sortedWords = SortedWords()
        self.crcList = CrcList()
        self.scrumList = ScrumList()
        self.useCaseList = UseCaseList()
        self.sprintList = SprintList()
        self.text = None