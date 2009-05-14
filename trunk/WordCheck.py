# -*- coding: cp1252 -*-

"""
File : WordCheck.py
Author : François Pelletier
Date Created : 20/04/09
Last Edited : 14/05/09
"""

from Tkinter import *

class WordCheck(object):
    """
    The WordCheck object is used on a list of TKinter Text Widgets and checks if all words from a list have been used in those
    texts if not, it informs the user and asks for what as to be done. It then returns the user's answer to its master.
    An Object WordCheck has the following methods :
    
    __init__(self, lists, texts, root)
    activate(self)
    fillCheckList(self)
    fillTextWords(self)
    removeUsedWords(self)
    showMessageBox(self)
    actionContinue(self)
    actionIgnore(self)
    actionCancel(self)
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
        if not it calls showMessageBox() and return status. The status is either True, False of None and indicates what
        the master of a WordCheck object has to do. If True, then destroy all widgets, and set this project part to green
        in the treeView, if False, same but with yellow treeView and if None, do nothing. This method also returns True if
        all the words from the lists have been used in the texts.
        """
        self.fillCheckList()
        self.fillTextWords()
        self.removeUsedWords()
        if len(self.checkList) > 0:
            self.showMessageBox()
            self.root.wait_window(self.toplevel)
            return self.status
        else:
            return True
                
    def fillCheckList(self):
        """
        This method is used to make checkList, a list of words, starting with a list of lists of words.
        """
        for currentList in self.lists:
            for currentElement in currentList:
                self.checkList.append(currentElement.lower())
    
    def fillTextWords(self):
        """
        This method is used to separate all the words used in the texts and put them into the new list textWords.
        """
        for currentText in self.texts:
            #text = currentText.get("1.0", END)
            text = currentText.splitlines()
            for line in text:
                line = line.strip(".,!?:;()$/\|#*&%_<>[]")
                line = line.split(" ")
                for word in line:
                    self.textWords.append(word.lower())
    
    def removeUsedWords(self):
        """
        This method is called by the activate method, it is used to remove the words from the checkList if they are in textWords.
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
        This method is called if some words in the lists were not used in the texts, it shows a toplevel window which asks
        the user if he wants to continue, ignore or cancel. All unused words are shown in a listbox.
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
        This method is called if the user presses the buttonContinue, it destroys the toplevel and sets the status to False,
        this will change the status to yellow in the treeView.
        """
        self.status = False
        self.toplevel.destroy()
    
    def actionIgnore(self):
        """
        This method is called if the user presses the buttonIgnore, it destroys the toplevel and sets the status to True,
        this will change the status to green in the treeView.
        """
        self.status = True
        self.toplevel.destroy()
        
    def actionCancel(self):
        """
        This method is called if the user presses the buttonCancel, it destroys the toplevel and sets the status to None
        so the user can continue editing the current page.
        """
        self.status = None
        self.checkList = []
        self.textWords = []
        self.toplevel.destroy()
    
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
    wordCheck = WordCheck(lists, [root.text1, root.text2], root)
    b = Button(root, text="OK", command=wordCheck.activate)
    b.pack()
    root.mainloop()
    
