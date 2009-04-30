# -*- coding: cp1252 -*-

"""
File : Autocompletion.py
Author : François Pelletier
Date Created : 20/04/09
Last Edited : 29/04/09
"""

from Tkinter import *

class Autocompletion(object):
    """
    The Autocompletion object is used on a TKinter TextBox and suggests to the user the use of 
    specific words through a ListBox filled with words matching the prefix the user entered.
    An Object Autocompletion has the following methods :
    
    __init__(self, root, lists, textBox)
    
    getWordStart(self)
    getWordEnd(self)
    findPrefix(self)
    completeWord(self)
    fillCompletionBox(self, event)
    checkFocus(self, event)
    """
    def __init__(self, root, lists, textBox):
        """
        When initialized, an object Autocompletion requires its TKinter root, a list
        (or list of lists) of strings and the TKinter TextBox to which it is assigned.
        """
        self.root = root
        self.lists = lists
        self.textBox = textBox
        self.completionBox = Listbox(self.root, borderwidth = 0, height = 3, width = 25)
        
        #self.root.bind("<FocusOut>", self.checkFocus)
        #self.textBox.bind("<Control-space>", self.)
        self.textBox.bind("<KeyRelease>", self.fillCompletionBox)
        self.completionBox.bind("<Double-1>",self.completeWord)
        self.completionBox.bind("<Return>",self.completeWord)

    def getWordStart(self):
        """
        This method is called by the method findPrefix() and is used to get the index of
        the beginning letter of the word the insert index is currently in.
        """        
        insertIndex = self.textBox.index(INSERT)   
        text = self.textBox.get("1.0", END)
        separator = "0.0"
        row = 1
        col = 0
        for char in text:
            col += 1
            if char == "\n":
                row += 1
                col = 0
                currentPosition = str(row) + "." + str(col)
                separator = currentPosition
            currentPosition = str(row) + "." + str(col)
            if char == " ":
                separator = currentPosition
            if currentPosition == insertIndex:
                return separator
        return "0.0"

    def findPrefix(self):
        """
        This method is called by the methods fillCompletionBox or completeWord, it is
        used to determine what the user is currently typing and return it as a prefix.
        """
        wordStart = self.getWordStart()
        prefix = self.textBox.get(wordStart, INSERT)
        if prefix == "":
            return False
        else:
            return prefix.capitalize()
    
    def getWordEnd(self):
        """
        This method is called by the method completeWord() and is used to get the index 
        of the end letter of the word the insert index is currently in, in case the user
        wants to complete a word while in the middle of another one.
        """
        insertIndex = self.textBox.index(INSERT)
        text = self.textBox.get(insertIndex, END)
        separators = [" ", "\n", ".", ",", "!", "?", ":", ";", "(", ")", "$"]
        separator = insertIndex
        partition = insertIndex.partition(".")
        row = int(partition[0])
        col = int(partition[2])
        for char in text:
            col += 1
            if char in separators:
                return str(row) + "." + str(col - 1)
        return END
           
    def completeWord(self, event):
        """
        This method is called when the user double clicks in the completionBox, the word
        the user was typing is then completed with the chosen suffix. If the suffix is inserted
        in the middle of a word, the part of the word following the insertIndex is deleted.
        """
        wordEnd = self.getWordEnd()
        self.textBox.delete(INSERT, wordEnd)
        
        prefix = self.findPrefix()
        select = self.completionBox.get(ACTIVE)
        partition = select.partition(" - ")
        suffix = partition[2].split(prefix)
        self.textBox.insert(INSERT, suffix[len(suffix) - 1])
        
        self.completionBox.pack_forget()   
         
    def fillCompletionBox(self, event):
        """
        This method is called whenever the user types a key while in the textBox, it then checks
        if any of the words in the lists fits the prefix, if so they are added to the completionBox,
        if none fit, then there is no use for the completionBox.
        """
        print event.getKeysym
        
        self.completionBox.pack()
        self.completionBox.delete(0, END)
        
        prefix = self.findPrefix()
        if not prefix:
            self.completionBox.pack_forget()
        else:
            empty = True
            for currentList in lists:
                for currentElement in currentList:
                    if currentList.index(currentElement) == 0:
                        symbol = currentElement
                    elif currentElement.startswith(prefix):
                        empty = False
                        self.completionBox.insert(END, symbol + " - " + currentElement)
            if empty:
                self.completionBox.pack_forget()
             
    def checkFocus(self, event):
        """
        This method is called when a widget, in the Autocompletion's root, loses focus,
        if the completionBox does not have the focus, it means the user is not using it
        
        monobjet=self.root.focus_get()
        print monobjet#.cget("text")
        
        if self.completionBox #DOESN'T HAVE FOCUS:
            self.completionBox.pack_forget()
        """         
        pass

if __name__ == "__main__":
    print "Testing the GUI..."
    root = Tk() 
    lists = [["Nom","Banane","Voiture"],["Adjectif","Atomique","Géant"],["Verbe","Bouger","Finir"],["#","1","2","3","4","5","6","7","8","9","10"]]
    root.minsize(800,600)
    root.title("Autocompletion Unit Test")
    root.text = Text(root)
    root.text.pack()
    
    autocompletion = Autocompletion(root, lists, root.text)
    root.mainloop()
