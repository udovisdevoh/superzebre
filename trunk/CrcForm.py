class CrcForm:
    def __init__(self, root,title,sortedWords, crcList, useCaseList):
        self.crcList = crcList
        self.sortedWords = sortedWords
        self.useCaseList = useCaseList
        self.initGraphicComponents(root)
        #if crcList == None:
        #    self.generateCrcs(sortedWords, useCaseList)
    
    def initGraphicComponents(self,root,title):
        self.fermer()
        root.title(title)