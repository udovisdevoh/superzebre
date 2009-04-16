#-*- coding: iso-8859-1 -*-
from Tkinter import *

class AnalyseTextuelleForm:
    def __init__(self, parent, title):
        self.parent = parent
        self.master = parent.root
        self.master.title(title)
        self.frameTop = Frame(self.master)
        self.frameBottom= Frame(self.master)
        self.frameCentre = Frame(self.master)
        
        self.canvas = Canvas(self.frameBottom, width=800, height=400)
        self.canvas.create_rectangle(4,4,266,400,width=2,fill="white")
        self.canvas.create_rectangle(269,4,532,400,width=2,fill="white")
        self.canvas.create_rectangle(535,4,800,400,width=2,fill="white")  
    
        self.button = Button(self.frameBottom, text="QUIT", fg="red", command=self.frameBottom.quit)
        self.button.pack(side=BOTTOM,anchor=E)
        
        self.frameTop.pack(side=TOP)
        self.frameBottom.pack(side = BOTTOM)
        self.frameCentre.pack()
         
        self.bVerbe = Button(self.frameCentre,text="Verbes",width=20)
        self.bNom = Button(self.frameCentre,text="Noms",width=20)
        self.bAdj = Button(self.frameCentre,text="Adjectifs",width=20)
        self.bSaute= Button(self.frameCentre,text="Sauter un mot",width=20)
        
        self.texte = Text(self.frameTop,height=10)
        self.texte.insert(END, "hello, ")
           
        self.bVerbe.pack(anchor=E,) 
        self.bNom.pack(anchor=CENTER) 
        self.bAdj.pack(anchor=W)
        
        self.bSaute.pack(side=BOTTOM,anchor=W,pady=20)
        
        self.texte.pack(side=TOP,pady=50)
        self.canvas.pack(side=BOTTOM,pady=20)  
          
    
if __name__=="__main__":
    from Client import *
    from Gui import *
    c = Client()
    c.vue.test = AnalyseTextuelleForm(c.vue,"test")      
    c.vue.test.master.mainloop()