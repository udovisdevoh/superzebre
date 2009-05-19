#-*- coding: iso-8859-1 -*-
from SortedWords import *
from CrcList import *
from ScrumList import *
from UseCaseList import *
from SprintList import *

class Project:
    def __init__(self,name):
        self.name = name
        self.sortedWords = SortedWords()
        self.crcList = CrcList()
        self.scrumList = ScrumList()
        self.useCaseList = UseCaseList()
        self.sprintList = SprintList()
        self.text = None
        self.colorOk = "#0F0"
        self.colorPending = "#FF0"
        self.colorNotOk = "#F00"
        self.colorOrange = "#FA0"
        self.colorTextAnalysis = self.colorNotOk
        self.colorUseCase = self.colorNotOk
        self.colorCRC = self.colorNotOk
        self.colorSCRUM = self.colorNotOk
        self.colorSprint = self.colorNotOk