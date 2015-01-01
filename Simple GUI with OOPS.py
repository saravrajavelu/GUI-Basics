#How to use a class with Tkinter

from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create 3 buttons that do nothing. """
        #create first button

        self.button1 = Button(self,text = "Button 1")
        self.button1.grid()

        #create the second button
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "Button 2")

        #create third button
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "Button 3"


root = Tk()
root.title("Insert title")
root.geometry("200x100")

app = Application(root)

root.mainloop()
