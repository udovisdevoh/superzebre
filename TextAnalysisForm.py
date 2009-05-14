#-*- coding: iso-8859-1 -*-
from Tkinter import *
from SortedWords import *

class TextAnalysisForm:
    def __init__(self, root, title, text, sortedWords, project, client):
        self.client = client
        self.project = project
        self.sortedWords = sortedWords       
        self.initGraphicComponents(root,title,text)
        self.fillWordTypeColumns()
        self.moveSelectionToNextWord()
    
    def initGraphicComponents(self,root,title,text):
        for i in root.pack_slaves():
            i.destroy()
        root.title(title)
        self.frameTop = Frame(root)
        self.frameBouton= Frame(root)
        self.frameSaute = Frame(root)
        self.frameBottom = Frame(root)
        self.frameBoutonValide = Frame(root)        
        self.verbe = Text(self.frameBottom,height=20,width=30)
        self.verbe.pack(side=LEFT)
        self.verbebar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.verbe.yview)
        self.verbebar.pack(side = LEFT , fill = Y)
        self.verbe.configure(yscrollcommand = self.verbebar.set)
        self.nom = Text(self.frameBottom,height=20,width=30)
        self.nom.pack(side=LEFT)
        self.nombar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.nom.yview)
        self.nombar.pack(side = LEFT , fill = Y)
        self.nom.configure(yscrollcommand = self.nombar.set)
        self.adj = Text(self.frameBottom,height=20,width=30)
        self.adj.pack(side=LEFT)
        self.adjbar = Scrollbar(self.frameBottom, orient=VERTICAL , command=self.adj.yview)
        self.adjbar.pack(side = LEFT , fill = Y)
        self.adj.configure(yscrollcommand = self.adjbar.set)
        self.cancel = Button(self.frameBoutonValide, text="Cancel", fg="red",command=self.fermer)
        self.valide = Button(self.frameBoutonValide, text="Valider", fg="green",command = self.valider)
        self.cancel.pack(side=LEFT)
        self.valide.pack(side=RIGHT)        
        self.frameTop.pack(side=TOP,pady=40)
        self.frameSaute.pack(side = TOP)
        self.frameBouton.pack(side = TOP,pady = 10)
        self.frameBottom.pack(side = TOP,padx = 10)
        self.frameBoutonValide.pack(side = TOP , pady = 15,ipadx = 345) 
        self.bVerbe = Button(self.frameBouton,text="Verbes",width=36,command=self.addVerbe)
        self.bNom = Button(self.frameBouton,text="Noms",width=36,command=self.addNom)
        self.bAdj = Button(self.frameBouton,text="Adjectifs",width=36,command=self.addAdj)
        self.bSaute= Button(self.frameSaute,text="Mot suivant",width=36,command=self.moveSelectionToNextWord)
        self.texte = Text(self.frameTop,height=10)
        self.texte.insert(END, text)
        self.texte.pack(side=LEFT)
        self.textebar = Scrollbar(self.frameTop, orient=VERTICAL , command=self.texte.yview)
        self.textebar.pack(side = LEFT , fill = Y)
        self.texte.configure(yscrollcommand = self.textebar.set,state=DISABLED)
        self.bVerbe.pack(side = LEFT,) 
        self.bNom.pack(side = LEFT) 
        self.bAdj.pack(side = LEFT)
        self.bSaute.pack(side=BOTTOM,anchor=W)
    
    def fillWordTypeColumns(self):
        for i in self.sortedWords.verbes:
            self.verbe.insert(END, i+"\n")
        for i in self.sortedWords.noms:
            self.nom.insert(END, i+"\n")
        for i in self.sortedWords.adjectifs:
            self.adj.insert(END, i+"\n")
    
    def addVerbe(self):
        self.tryAddSelectedWordToField(self.verbe)
    
    def addNom(self):
        self.tryAddSelectedWordToField(self.nom)
    
    def addAdj(self):
        self.tryAddSelectedWordToField(self.adj)
    
    def tryAddSelectedWordToField(self, wordField):
        try:
            word = str(self.texte.get("sel.first", "sel.last")).strip()
            word = word.lower()
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace("!","")
            word = word.replace("?","")
            word = word.replace(")","")
            word = word.replace("(","")
            word = word.replace("{","")
            word = word.replace("}","")
            word = word.replace("\"","")
            if self.wordFieldContainsWord(wordField, word) == 0 and len(word) > 0:
                wordField.insert("1.0", word+"\n")
        except TclError:
            pass
        self.moveSelectionToNextWord()
    
    def valider(self):
        verbList = self.getWordListFromTextField(self.verbe)
        nounList = self.getWordListFromTextField(self.nom)
        adjList = self.getWordListFromTextField(self.adj)        
        self.sortedWords.setWordsTypes(verbList, nounList, adjList)
        self.project.colorTextAnalysis = self.project.colorOk
        self.fermer()
        
    def fermer(self):
        try:
            #self.top.destroy()
            self.frameTop.destroy()
            self.frameBouton.destroy()
            self.frameSaute.destroy()
            self.frameBottom.destroy()
            self.frameBoutonValide.destroy()
            self.client.tryShowTreeView()
        except AttributeError:
            pass
        
    def moveSelectionToNextWord(self):
        try:
            self.texte.get("sel.first", "sel.last")
        except TclError:
            self.texte.tag_add(SEL, "1.0", self.getFirstWordEndPosition())
            self.texte.focus_set()
            return
        newSelectionBegin = self.getNextWordBeginPosition()
        newSelectionEnd = self.getNextWordEndPosition()
        self.texte.tag_remove(SEL, "1.0", END)
        self.texte.tag_add(SEL, newSelectionBegin, newSelectionEnd)
        if self.texte.get("sel.first", "sel.last").strip().find(" ") > -1:
            self.texte.tag_remove(SEL, "1.0", END)    
        self.texte.focus_set()
    
    def wordFieldContainsWord(self,wordField,word):
        fieldContent = self.getStringFromWordField(wordField)        
        fieldContent = fieldContent.replace("\n"," ")
        fieldContent = " " + fieldContent + " "
        if fieldContent.find(" " + word + " ") > -1:
            return 1
        else:
            return 0
    
    def getStringFromWordField(self,wordField):
        wordField.tag_add(SEL, "1.0", END)
        fieldContent = str(wordField.get("sel.first","sel.last")).strip()
        return fieldContent
    
    def getWordListFromTextField(self,wordField):
        fieldContent = self.getStringFromWordField(wordField)
        return fieldContent.split("\n")
    
    def getFirstWordEndPosition(self):
        textContent = self.texte.get("1.0", END)
        rowId = 1
        colId = 0
        for char in textContent:
            colId+=1
            if char == "\n":
                rowId+=1
                colId = 0
            if char == " ":
                return str(str(rowId) + "." + str(colId -1))
    
    def getNextWordBeginPosition(self):
        selectionStartPoint = self.texte.index("sel.first")
        selectionEndPoint = self.texte.index("sel.last")
        selectionStartCol = self.getColFromIndex(selectionStartPoint)
        selectionStartRow = self.getRowFromIndex(selectionStartPoint)
        selectionEndCol = self.getColFromIndex(selectionEndPoint)
        selectionEndRow = self.getRowFromIndex(selectionEndPoint)
        selectionStartCol = selectionEndCol + 1 
        return str(selectionStartRow) + "." + str(selectionStartCol) 
    
    def getNextWordEndPosition(self):
        selectionEndPoint = self.texte.index("sel.last")
        colId = self.getColFromIndex(selectionEndPoint) + 1
        rowId = self.getRowFromIndex(selectionEndPoint)
        textContent = self.texte.get(selectionEndPoint, END)
        textContent = textContent[1:]
        for char in textContent:
            colId+=1
            if char == "\n":
                rowId+=1
                colId = 0
            if char == " ":
                return str(str(rowId) + "." + str(colId -1))
        return self.texte.index(END)
    
    def getRowFromIndex(self,index):
        pointPos = int(index.find("."))
        return int(index[0:pointPos])
    
    def getColFromIndex(self,index):
        pointPos = int(index.find("."))
        return int(index[pointPos + 1:len(index)])
        
if __name__ == "__main__":
    root = Tk()
    textAnalysisForm = TextAnalysisForm(root,"Analyse Textuelle","quirstay as sont commend mes misectly wert cieforces",SortedWords())
    #textAnalysisForm = TextAnalysisForm(root,"Analyse Textuelle","quirstay as sont commend mes misectly wert cieforces par try scepty prity ifereld reatent frome evalition for the the lonere of aring fal the alsorm a actiound of ourehers sentordiareing es it ong aft and self it of he exotifer as posoper ot ing the phis ont a sompas esenthe so se exceadvothated truch it thow there",SortedWords())
    textAnalysisForm.top = Toplevel(root)
    root.wait_window(textAnalysisForm.top)