# -*- coding: cp1252 -*-

"""
File : WordCheck.py
Author : François Pelletier
Date Created : 20/04/09
Last Edited : 11/05/09
"""

from Tkinter import *

class WordCheck(object):
    """
    """
    def __init__(self, lists, texts, root):
        """
        When initialized, an object WordCheck requires a list of lists of strings (the strings have to be lowered),
        a list of Text Widgets it has to check and its TKinter root.
        """
        self.lists = lists
        self.texts = texts
        self.checkList = []
        self.textWords = []
        self.root = root
        self.status = None
    
    def activate(self):
        """
        This method checks if all the words of the lists have been used in the texts, if they have, it returns True,
        if not it calls showMessageBox() and return status (either True, False of None)
        """
        self.fillCheckList()
        self.fillTextWords()
        self.removeUsedWords()
        if len(self.checkList) > 0:
            self.showMessageBox()
            return self.status
        else:
            return True
                
    def fillCheckList(self):
        """
        """
        for currentList in self.lists:
            for currentElement in currentList:
                self.checkList.append(currentElement)
    
    def fillTextWords(self):
        """
        """
        for currentText in self.texts:
            text = currentText.get("1.0", END)
            text = text.splitlines()
            for line in text:
                line = line.strip(".,!?:;()$/\|#*&%_<>[]")
                line = line.split(" ")
                for word in line:
                    self.textWords.append(word)
    
    def removeUsedWords(self):
        """
        """
        usedWords = []
        for checkWord in self.checkList:
            for word in self.textWords:
                word = word.lower()
                if checkWord == word:
                    usedWords.append(word)
        if len(usedWords) > 0:
            for word in usedWords:
                word = word.lower()
                self.checkList.remove(word)
                
    def showMessageBox(self):
        """
        """
        self.toplevel = Toplevel(self.root, width = 300)
        self.toplevel.title("Mots Inutilisés")
        self.toplevel.iconbitmap("zebra.ico")
        
        text = "Certains mots de votre analyse textuelle sont inutilisés dans cette partie du projet. En voici la liste :\n"
        message = Message(self.toplevel, text = text, width = 300)
        message.pack()
        
        listbox = Listbox(self.toplevel, height = 3, width = 30)
        listbox.delete(0, END)
        for word in self.checkList:
            listbox.insert(END, word)
        listbox.pack()
        
        text = "\nSouhaitez-vous continuer et être avertit plus tard (section en jaune), ignorer ce message (section en vert) ou bien annuler pour ré-éditer cette partie du projet?\n"
        message = Message(self.toplevel, text = text, width = 300)
        message.pack()
        
        frameButton= Frame(self.toplevel)
        frameButton.pack()
        
        buttonContinue = Button(frameButton, text = "Continuer", command = self.actionContinue)
        buttonContinue.pack(side = LEFT)
        buttonIgnore = Button(frameButton, text = "Ignorer", command = self.actionIgnore)
        buttonIgnore.pack(side = LEFT)
        buttonCancel = Button(frameButton, text = "Annuler", command = self.actionCancel)
        buttonCancel.pack(side = LEFT)
        
    def actionContinue(self):
        """
        """
        self.toplevel.destroy()
        self.status = False
        
    
    def actionIgnore(self):
        """
        """
        self.toplevel.destroy()
        self.status = True
        
    def actionCancel(self):
        """
        """
        self.toplevel.destroy()
        self.status = None
        self.checkList = []
        self.textWords = []
    
if __name__ == "__main__":
    print "Testing the GUI..."
    root = Tk() 
    lists = [["banane","voiture"],["atomique","géant"],["bouger","finir"],["1","2","3","4","5","6","7","8","9","10"]]
    root.minsize(800,600)
    root.title("WordCheck Unit Test")
    root.iconbitmap("zebra.ico")
    root.text1 = Text(root, height = 10, width = 30)
    root.text1.pack()
    root.text2 = Text(root, height = 10, width = 30)
    root.text2.pack()
    wordCheck = WordCheck(lists, [root.text1,root.text2], root)
    b = Button(root, text="OK", command=wordCheck.activate)
    b.pack()
    root.mainloop()
    
