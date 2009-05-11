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
    def __init__(self, lists, texts):
        """
        When initialized, an object WordCheck requires a list (or list of lists) of strings (the strings have to be lowered),
        and a list of Text Widgets it has to check.
        """
        self.checkList = []
        self.wordList = []
        
        fillCheckList(lists)
        fillWordList(texts)
        
    
    def fillCheckList(self, lists):
        for currentList in lists:
            for currentElement in currentList:
                self.checkList.append(currentElement)
    
    def fillWordList(self, texts):
        for currentText in texts:
            text = currentText.get("1.0", END)
            text = text.splitlines()
            for line in text:
                line = line.strip(".,!?:;()$/\|#*&%_<>[]")
                line = line.split(" ")
                for word in line:
                    self.wordList.append(word)
    
    def compareLists(self):
        for check in self.checkList:
            for word in self.wordList:
                if check == word:
                    self.checkList.remove(check)
                    
    
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
