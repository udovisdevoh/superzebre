from Tkinter import *
class TextForm:
    def __init__(self, parent, message):
        self.outputValue = ""
        top = self.top = Toplevel(parent)
        Label(top, text=message).pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.outputValue = self.e.get()
        self.top.destroy()

if __name__ == "__main__":
    root = Tk()
    textForm = TextForm(root,"Question")
    root.wait_window(textForm.top)