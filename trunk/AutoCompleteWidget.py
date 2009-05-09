# -*- coding: cp1252 -*-

"""
File : AutoCompleteWidget.py
Author : François Pelletier
Date Created : 20/04/09
Last Edited : 03/05/09
"""

from Tkinter import *

class AutoCompletion(object):
    """
    The AutoCompletion object is used on a TKinter TextBox and suggests to the user the use of 
    specific words through a ListBox filled with words matching the prefix the user entered.
    An Object AutoCompletion has the following methods :
    
    __init__(self, root, lists, textBox)
    getWordStart(self)
    getWordEnd(self)
    findPrefix(self)
    completeWord(self)
    fillCompletionBox(self, event)
    showAllWords(self, event)
    removeCompletionBox(self, event)
    """
    def __init__(self, root, lists, symbols, textBox, height, width):
        """
        When initialized, an object AutoCompletion requires its TKinter root, a list (or list of lists)
        of strings (the strings have to be lowered), the symbols argument has to be True if symbols have
        been inserted into the lists, if not, it has to be False, it needs the Text Widget to which it
        is assigned and the height and width of the Listbox Widget.
        """
        self.root = root
        self.lists = lists
        self.symbols = symbols
        self.textBox = textBox
        self.ignoreKey = 0
        self.completionBox = Listbox(self.root, height = height, width = width)
        self.textBox.bind("<Control-space>", self.showAllWords)
        self.textBox.bind("<KeyRelease>", self.fillCompletionBox)
        self.textBox.bind("<ButtonRelease-1>", self.fillCompletionBox)
        self.completionBox.bind("<Double-1>",self.completeWord)
        self.completionBox.bind("<Return>",self.completeWord)
        self.completionBox.bind("<FocusOut>", self.removeCompletionBox)
            
    def getWordStart(self):    
        """
        This method is called by the method findPrefix() and is used to get the index of
        the beginning letter of the word the insert index is currently in.
        """   
        insertIndex = self.textBox.index(INSERT)   
        text = self.textBox.get("1.0", END)
        separator = "1.0"
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
            if char in [" ", "\t"]:
                separator = currentPosition
            if currentPosition == insertIndex:
                return separator
        return "1.0"
    
    def getWordEnd(self):
        """
        This method is called by the method completeWord() and is used to get the index 
        of the end letter of the word the insert index is currently in, in case the user
        wants to complete a word while in the middle of another one.
        """
        insertIndex = self.textBox.index(INSERT)
        text = self.textBox.get(insertIndex, END)
        separatorList = [" ", "\n", "\t", ".", ",", "!", "?", ":", ";", "(", ")", "$"]
        separator = insertIndex
        partition = insertIndex.partition(".")
        row = int(partition[0])
        col = int(partition[2])
        for char in text:
            col += 1
            if char in separatorList:
                return str(row) + "." + str(col - 1)
        return END
     
    def findPrefix(self):
        """
        This method is called by the methods fillCompletionBox or completeWord, it is
        used to determine what the user is currently typing and return it as a prefix.
        If there is no prefix, the method returns False.
        """
        wordStart = self.getWordStart()
        prefix = self.textBox.get(wordStart, INSERT)
        if prefix == "":
            return False
        else:
            return prefix.lower()
        
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
        if self.symbols:
            partition = select.partition(" - ")
            if not prefix:
                self.textBox.insert(INSERT, partition[2])
            else:
                suffix = partition[2].split(prefix)
                self.textBox.insert(INSERT, suffix[len(suffix) - 1])
        else:
            if not prefix:
                self.textBox.insert(INSERT, select)
            else:
                suffix = select.split(prefix)
                self.textBox.insert(INSERT, suffix[len(suffix) - 1])
        self.completionBox.pack_forget()
        self.textBox.focus_set()
 
    def fillCompletionBox(self, event):
        """
        This method is called whenever the user types a key while in the textBox, it then checks
        if any of the words in the lists fits the prefix, if so they are added to the completionBox,
        if none fit, then there is no use for the completionBox.
        """
        if self.ignoreKey in [1,2]:
            self.ignoreKey -= 1
        else:
            self.completionBox.pack()
            self.completionBox.delete(0, END)
            prefix = self.findPrefix()
            if not prefix:
                self.completionBox.pack_forget()
            else:
                empty = True
                for currentList in self.lists:
                    for currentElement in currentList:
                        if self.symbols:
                            if currentList.index(currentElement) == 0:
                                symbol = currentElement
                            elif currentElement.startswith(prefix):
                                empty = False
                                self.completionBox.insert(END, symbol + " - " + currentElement)
                        elif currentElement.startswith(prefix):
                                empty = False
                                self.completionBox.insert(END, currentElement)            
                if empty:
                    self.completionBox.pack_forget()
    
    def showAllWords(self, event):
        """
        This method is called by a <Control-space> event in the textBox. It is used to show all the words
        of the lists in the completionBox. Since a <Control-space> event also generates two <KeyRelease>
        event, it sets the ignoreKey to 2 else, the fillCompletionBox would cancel the effects of this method.
        """
        self.ignoreKey = 2
        self.completionBox.pack()
        self.completionBox.delete(0, END)
        for currentList in self.lists:
            for currentElement in currentList:
                if self.symbols:
                    if currentList.index(currentElement) == 0:
                        self.symbol = currentElement
                    else:
                        self.completionBox.insert(END, self.symbol + " - " + currentElement)
                else:
                    self.completionBox.insert(END, currentElement)
    
    def removeCompletionBox(self, event):
        """
        This method is called when the completionBox lost the focus, this means that the user first clicked on the
        completionBox and then clicked elsewhere, probably in the textBox, then there is no use for the completionBox.
        Since an event binding calls a method with the event as parameters, it was essential to call this method
        instead of the unpacking method directly.
        """
        self.completionBox.pack_forget()
    
if __name__ == "__main__":
    print "Testing the GUI..."
    root = Tk() 
    list1 = [["nom","banane","voiture"],["adjectif","atomique","géant"],["verbe","bouger","finir"],["#","1","2","3","4","5","6","7","8","9","10"]]
    list2 = [["banane","voiture"],["atomique","géant"],["bouger","finir"],["1","2","3","4","5","6","7","8","9","10"]]
    root.minsize(800,600)
    root.title("AutoCompletion Unit Test")
    root.text = Text(root, height = 10, width = 30)
    root.text.pack()
    autoCompletion = AutoCompletion(root, list1, True, root.text, 5, 50)
    
    root.text2 = Text(root, height = 10, width = 30)
    root.text2.pack()
    autoCompletion = AutoCompletion(root, list2, False, root.text2, 5, 50)
    root.mainloop()
